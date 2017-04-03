from flask import Flask, request
import json

app = Flask(__name__)
linked_data = json.load(open("Spacecraft.json", "r"))
entrypoint = "/"

# Base url, serves api documentation and the entrypoint
@app.route('/demo-api/vocab')
def entrypoint():
    if request.method == "GET"
        return ()
