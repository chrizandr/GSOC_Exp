# Using http://www.markus-lanthaler.com/hydra/event-api/

# -*- coding: utf-8 -*-

from flask import Flask, jsonify, url_for, redirect, request
from flask_restful import Api, Resource
from json_data.contexts import *
from json_data.entrypoint import entrypoint
from json_data.vocab import vocab
import json
import sqlite3
import psycopg2 as psql
import pdb
from models import *
# from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)

db_credentials = "dbname='hydra' user='hydrus' host='localhost' password='hydra'"
keymap = {
    "COM" : "Spacecraft_Communication",
    "PROP": "Spacecraft_Propulsion",
    "DTR": "Spacecraft_Detector",
    "PPW": "Spacecraft_PrimaryPower",
    "BCK": "Spacecraft_BackupPower",
    "THR": "Spacecraft_Thermal",
    "STR":  "Spacecraft_Structure",
    "CDH": "Spacecraft_CDH",
    "AODCS": "Spacecraft_AODCS",
}

def set_response_headers(resp, ct="application/ld+json", status_code=200):
    """
    Sets the response headers
    Default : { Content-type:"JSON-LD", status_code:200}
    """
    resp.status_code = status_code
    resp.headers['Content-type'] = ct
    return resp


def gen_subsystem_json(sub_id, subsystem):

    template = {
        "@id": "/api/subsystem/*",
        "@type": "SubSystem",
    }

    template['@id'] = "/api/subsystem/{}".format(sub_id)
    for key in vars(subsystem).keys():
        template[key] = vars(subsystem)[key]
    return template


def hydrafy_subsystem(sub_id, subsystem):
    subsystem_data = gen_subsystem_json(sub_id, subsystem)
    # Adding context
    subsystem_data["@context"] = subsystem_context["@context"]
    return jsonify(subsystem_data)


def hydrafy_subsystems(subsystem_list):
    subsystem_collection_template = {
    "@id": "/api/subsystems",
    "@type": "SubSystemCollection",
    "members": []
    }

    members = []
    for sub_id, subsystem in subsystem_list:
        members.append(gen_subsystem_json(sub_id, subsystem))
    subsystem_collection_template["members"] = members

    subsystem_collection_template["@context"] = subsystem_collection_context["@context"]

    return subsystem_collection_template


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


class Subsystems(Resource):
    """Class for SubSystems Collection"""

    def get(self):
        # global db_credentials
        print("Connecting")
        conn = psql.connect(db_credentials)
        cur = conn.cursor()
        cur.execute("SELECT * FROM SubSystem")
        index = cur.fetchall()
        relations = set([x[2] for x in index])
        # pdb.set_trace()
        objects = list()
        for relation in relations:
            query = "SELECT * FROM SubSystem INNER JOIN {} ON SubSystem.ID={}.ID".format(relation, relation)
            cur.execute(query)
            rows = cur.fetchall()
            objects = objects + [(data[0], eval(keymap[relation])(data[1], *data[4:])) for data in rows]
        conn.close()

        return set_response_headers(jsonify(hydrafy_subsystems(objects)), 'application/ld+json', 200)

api.add_resource(Subsystems, "/api/subsystems", endpoint="subsystems")


class Subsystem(Resource):
    """All operations related to Product"""

    def get(self, sub_id):
        global db_credentials
        conn = psql.connect(db_credentials)
        cur = conn.cursor()
        if int(sub_id):
            cur.execute('SELECT * FROM SubSystem WHERE ID = %s', (sub_id,))
            sub_id, name, relation = cur.fetchone()
            query = "SELECT * FROM SubSystem INNER JOIN {} ON SubSystem.ID={}.ID WHERE SubSystem.ID = {}".format(relation, relation, sub_id)
            cur.execute(query)
            data = cur.fetchone()
            if not data:
                return set_response_headers(jsonify({"Error":"No data available"}), 'application/ld+json', 404)
            subsystem = eval(keymap[relation])(data[1], *data[4:])
        conn.close()
        return set_response_headers(hydrafy_subsystem(sub_id, subsystem), 'application/ld+json', 200)

    def post(self):
        pass

    def delete(self, sub_id):
        global db_credentials
        conn = psql.connect(db_credentials)
        cur = conn.cursor()
        if int(sub_id):
            cur.execute('SELECT * FROM SubSystem WHERE ID = %s', (sub_id,))
            sub_id, name, relation = cur.fetchone()
            if name:
                query = 'DELETE FROM {} ID = {}'.format(relation, sub_id)
                cur.execute(query)
                cur.execute('DELETE FROM SubSystem WHERE ID = %s', (sub_id,))
                conn.commit()
                output = {"Done":"Product with id {} successfully deleted.".format(int(sub_id))}
            else:
                output = {"Error":"No product with id {} available.".format(int(product_id))}
        return set_response_headers(jsonify(output), 'application/ld+json', 301)

api.add_resource(
    Subsystem, "/api/subsystem/<string:sub_id>", endpoint="subsystem")


class EntryPointContext(Resource):
    """Handles entrpoint contexts"""

    def get(self):
        return set_response_headers(jsonify(entrypoint_context), 'application/ld+json', 200)

api.add_resource(EntryPointContext, "/api/contexts/EntryPoint.jsonld",
                 endpoint="entrypoint_context")


class SubSystemCollectionContext(Resource):
    """Handles Product collection Contexts"""

    def get(self):
        return set_response_headers(jsonify(subsystem_collection_context), 'application/ld+json', 200)

api.add_resource(SubSystemCollectionContext, "/api/contexts/SubSystemCollection.jsonld",
                 endpoint="subsystem_collection_context")


class SubSystemContext(Resource):
    """ Handles Product contexts"""

    def get(self):
        return set_response_headers(jsonify(subsystem_context), 'application/ld+json', 200)

api.add_resource(
    SubSystemContext, "/api/contexts/SubSystem.jsonld", endpoint="subsystem_context")



if __name__ == "__main__":
    app.run(host = 'localhost', debug=True)
