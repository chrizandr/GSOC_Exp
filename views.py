# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import json
import pdb

from json_response import *

app = Flask(__name__)

@app.route('/demo-api', methods=["GET"])
def entrypoint():
    '''
        Application EntryPoint, allowing only GET requests for now
        Returning status code 405 [not allowed] for other requests
    '''
    if request.method == "GET":
        return get_entrypoint()

    else:
        return not_allowed()

@app.route('/demo-api/contexts/EntryPoint.jsonld', methods=["GET"])
def entrypoint_context():
    '''
        Returns the context for the EntryPoint
    '''
    response = jsonify(
        json.load(open("EntryPoint.jsonld","r"))
    )
    response.status_code = 200
    response.headers["Content-type"] = "application/ld+json"
    return response

@app.route('/demo-api/vocab', methods=["GET"])
def vocab():
    '''
        Returns the entire vocabulary of the server.
        Currently only able to create Hydra vocabulary for the Engineering concepts in  ​https://github.com/chronos-pramantha/RDFvocab/blob/master/ld%2Bjson/
    '''
    return get_vocab()

# NOTE: Following functions are incomplete and are based on the Engineering vocabulary in https://github.com/chronos-pramantha/RDFvocab/blob/master/ld%2Bjson/

@app.route('/demo-api/Satellite_Device', methods=["GET", "POST", "DELETE"])
def Satellite_Device():
    '''
        Modify the Satellite_Device class and objects as describe in vocab.jsonld
    '''
    pass

@app.route('/demo-api/GroundToOrbitVehicle', methods=["GET", "POST", "DELETE"])
def GroundToOrbitVehicle():
    '''
        Modify the GroundToOrbitVehicle class and objects as describe in vocab.jsonld
    '''
    pass

@app.route('/demo-api/InformationGatheringDevice', methods=["GET", "POST", "DELETE"])
def InformationGatheringDevice():
    '''
        Modify the InformationGatheringDevice class and objects as describe in vocab.jsonld
    '''
    pass

@app.route('/demo-api/AstronomicalSatellite', methods=["GET", "POST", "DELETE"])
def AstronomicalSatellite():
    '''
        Modify the AstronomicalSatellite class and objects as describe in vocab.jsonld
    '''
    pass

@app.route('/demo-api/WeatherSatellite', methods=["GET", "POST", "DELETE"])
def WeatherSatellite():
    '''
        Modify the WeatherSatellite class and objects as describe in vocab.jsonld
    '''
    pass

@app.route('/demo-api/EarthRemoteSensingSatellite', methods=["GET", "POST", "DELETE"])
def EarthRemoteSensingSatellite():
    '''
        Modify the EarthRemoteSensingSatellite class and objects as describe in vocab.jsonld
    '''
    pass

@app.route('/demo-api/SpaceProbe', methods=["GET", "POST", "DELETE"])
def SpaceProbe():
    '''
        Modify the SpaceProbe class and objects as describe in vocab.jsonld
    '''
    pass
