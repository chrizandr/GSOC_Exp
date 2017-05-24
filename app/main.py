# Using http://www.markus-lanthaler.com/hydra/event-api/

# -*- coding: utf-8 -*-

from flask import Flask, jsonify, url_for, redirect, request
from flask_restful import Api, Resource
from json_data.contexts import entrypoint_context, product_collection_context, product_context
from json_data.entrypoint import entrypoint
from json_data.vocab import vocab
import json
import sqlite3
# from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)
# CORS(app)


def set_response_headers(resp, ct="application/ld+json", status_code=200):
    """ Sets the response headers
        Default : { Content-type:"JSON-LD", status_code:200}"""
    resp.status_code = status_code
    resp.headers['Content-type'] = ct
    return resp


class Raw_Product(object):

    def __init__(self, pid, description, price, name):
        self.id = pid
        self.description = description
        self.price = price
        self.name = name

# Generate product json data from Raw_product


def gen_product_json(product):

    product_template = {
        "@id": "/api/products/*",
        "@type": "Product",
        "name": "Coffee",
        "description": "Coffee_description",
        "price": 1.0
    }

    product_template['@id'] = "/api/products/{}".format(product.id)
    product_template['description'] = product.description
    product_template['name'] = product.name
    product_template['price'] = float(product.price)

    return product_template


def hydrafy_product(product):
    product_data = gen_product_json(product)
    # Adding context
    product_data["@context"] = product_context["@context"]
    return jsonify(product_data)


def hydrafy_products(product_list):
    product_collection_template = {
        "@id": "/api/products",
        "@type": "ProductCollection",
        "members": []
    }

    members = []
    for product in product_list:
        members.append(gen_product_json(product))
    product_collection_template["members"] = members

    product_collection_template[
        "@context"] = product_collection_context["@context"]

    return product_collection_template

# For now I am using dummy data, later on we can switch to dynamic data


def gen_products():
    return jsonify({
        "@context": "/api/contexts/ProductCollection.jsonld",
        "@id": "/api/products",
        "@type": "ProductCollection",
        "members": [
            {
                "@id": "/api/products/80",
                "@type": "http://schema.org/Product"
            },
            {
                "@id": "/api/products/81",
                "@type": "http://schema.org/Product"
            },
            {
                "@id": "/api/products/83",
                "@type": "http://schema.org/Product"
            },
            {
                "@id": "/api/products/84",
                "@type": "http://schema.org/Product"
            },
            {
                "@id": "/api/products/85",
                "@type": "http://schema.org/Products"
            },
            {
                "@id": "/api/products/86",
                "@type": "http://schema.org/Product"
            },
            {
                "@id": "/api/products/87",
                "@type": "http://schema.org/Product"
            }
        ]
    }
    )


class Index(Resource):

    """A link to main entry point of the Web API"""

    def get(self):
        return set_response_headers(jsonify(entrypoint), 'application/ld+json', 200)

api.add_resource(Index, "/apii", endpoint="api")


class Vocab(Resource):
    """A general vocab for the API"""

    def get(self):
        return set_response_headers(jsonify(vocab), 'application/ld+json', 200)

api.add_resource(Vocab, "/api/vocab", endpoint="vocab")


class Products(Resource):
    """All operations related to Products Collection"""

    def get(self):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute('select * from products')
        products_data = cur.fetchall()
        raw_products = []
        for data in products_data:
            raw_products.append(Raw_Product(
                data[0], data[1], data[2], data[3]))
        # print(raw_products)
        conn.close()
        return set_response_headers(jsonify(hydrafy_products(raw_products)), 'application/ld+json', 200)

api.add_resource(Products, "/api/products", endpoint="products")


class Product(Resource):
    """All operations related to Product"""

    def get(self, product_id):
        # return set_response_headers(gen_dummy_product(),
        # 'application/ld+json', 200)
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        if int(product_id):
            cur.execute(
                'select * from products where P_id = {}'.format(int(product_id)))
            data = cur.fetchone()
            if not data:
                return set_response_headers(jsonify({"Error": "No product available"}), 'application/ld+json', 404)
            # print(data)
            # Create raw_product class instance
            product = Raw_Product(data[0], data[1], data[2], data[3])
        conn.close()
        return set_response_headers(hydrafy_product(product), 'application/ld+json', 200)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self, product_id):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        if int(product_id):
            cur.execute(
                'select * from products where P_id = {}'.format(int(product_id)))
            data = cur.fetchall()
            if len(data) > 0:
                cur.execute(
                    'delete from products where P_id = {}'.format(int(product_id)))
                conn.commit()
                output = {"Done": "Product with id {} successfully deleted.".format(
                    int(product_id))}
            else:
                output = {"Error": "No product with id {} available.".format(
                    int(product_id))}
        return set_response_headers(jsonify(output), 'application/ld+json', 301)

api.add_resource(
    Product, "/api/products/<string:product_id>", endpoint="product")


class EntryPointContext(Resource):
    """Handles entrpoint contexts"""

    def get(self):
        return set_response_headers(jsonify(entrypoint_context), 'application/ld+json', 200)

api.add_resource(EntryPointContext, "/api/contexts/EntryPoint.jsonld",
                 endpoint="entrypoint_context")


class ProductCollectionContext(Resource):
    """Handles Product collection Contexts"""

    def get(self):
        return set_response_headers(jsonify(product_collection_context), 'application/ld+json', 200)

api.add_resource(ProductCollectionContext, "/api/contexts/ProductCollection.jsonld",
                 endpoint="product_collection_context")


class ProductContext(Resource):
    """ Handles Product contexts"""

    def get(self):
        return set_response_headers(jsonify(product_context), 'application/ld+json', 200)

api.add_resource(
    ProductContext, "/api/contexts/Product.jsonld", endpoint="product_context")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)

# volume test 1
