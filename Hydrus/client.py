import requests
import pdb
'''
A basic client implementation to communicate with the server
'''

# NOTE: Make sure all dependencies in requirements.txt are installed and then perform the execute commands
# export FLASK_APP=views.py
# export FLASK_DEBUG=1
# flask run --host=127.0.0.1 --port=8000

EntryPoint_url = "http://127.0.0.1:8000/demo-api/"
response = requests.get(EntryPoint_url)
print(response.status_code)
print(response.headers["Content-type"])
print(response.json())

EntryPoint_context_url = "http://127.0.0.1:8000/demo-api/contexts/EntryPoint.jsonld"
response = requests.get(EntryPoint_context_url)
print(response.status_code)
print(response.headers["Content-type"])
print(response.json())

Vocab_url = "http://127.0.0.1:8000/demo-api/vocab"
print(response.status_code)
print(response.headers["Content-type"])
print(response.json())
