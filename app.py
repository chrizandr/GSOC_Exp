# Using http://www.markus-lanthaler.com/hydra/event-api/

# -*- coding: utf-8 -*-

from flask import Flask, jsonify, url_for, redirect, request
from flask_restful import Api, Resource
from contexts import entrypoint_context, product_collection_context, product_context
from entrypoint import entrypoint
from vocab import vocab
import os
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


def gen_dummy_product():
    return jsonify(
        {
            "@context": "/api/contexts/Product.jsonld",
            "@id": "/api/products/*",
            "@type": "Product",
            "name": "Coffee",
            "description": "This is Coffee, it tastes good",
        }

    )
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

api.add_resource(Index, "/api", endpoint="api")


class Vocab(Resource):
    """A general vocab for the API"""

    def get(self):
        return set_response_headers(jsonify(vocab), 'application/ld+json', 200)

api.add_resource(Vocab, "/api/vocab", endpoint="vocab")


class Products(Resource):
    """All operations related to Products Collection"""

    def get(self):
        return set_response_headers(gen_products(), 'application/ld+json', 200)

api.add_resource(Products, "/api/products", endpoint="products")


class Product(Resource):
    """All operations related to Product"""

    def get(self, product_id):
        return set_response_headers(gen_dummy_product(), 'application/ld+json', 200)

    def post(self):
        pass
        
    def put(self):
        pass

    def delete(self):
        pass

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
    app.run(host = '0.0.0.0')
