# -*- coding: utf-8 -*-

from flask import jsonify

def get_entrypoint(ctype="application/ld+json", status=200):
    response = jsonify(
        {
            "@context": "/demo-api/contexts/EntryPoint.jsonld",
            "@id": "/demo-api/",
            "@type": "EntryPoint",
            "Satellite_Device": "/demo-api/Satellite_Device",
            "GroundToOrbitVehicle": "/demo-api/GroundToOrbitVehicle",
            "InformationGatheringDevice": "/demo-api/InformationGatheringDevice",
            "AstronomicalSatellite": "/demo-api/AstronomicalSatellite",
            "WeatherSatellite": "/demo-api/WeatherSatellite",
            "EarthRemoteSensingSatellite": "/demo-api/EarthRemoteSensingSatellite",
            "SpaceProbe": "/demo-api/SpaceProbe"
        }
    )
    response.status_code = status
    response.headers["Content-type"] = ctype
    return response

def not_allowed(ctype="text/html", status=403):
    response = jsonify({})
    response.headers["Content-type"] = ctype
    response.status_code = status
    return response

def get_vocab(ctype="application/ld+json", status=200):
    response = jsonify(json.loads(open("vocab.jsonld","r")))
    response.status_code = status
    response.headers["Content-type"] = ctype
    return response
