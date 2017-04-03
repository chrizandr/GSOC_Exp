# Hydrus
A demo repository for the Hydra draft for GSOC

The vocabulary for the demo is defined in [vocab.jsonld](https://github.com/chrizandr/Hydrus/blob/master/vocab.jsonld)

It is based on the Engineering vocabulary present [here](https://github.com/chronos-pramantha/RDFvocab/blob/master/ld%2Bjson/)

The following API calls are available

`/demo-api` - Initial EntryPoint for a client **[GET]**

`/demo-api/vocab`  -  Hydra implementation for Engineering database **[GET]**

`/demo-api/contexts/EntryPoint.jsonld` - Returns the context for the EntryPoint **[GET]**

There are abstract definitions for the remaining classes in the vocabulary
These will be implemented once the final specifications are decided.

There is also a basic client in [client.py](https://github.com/chrizandr/Hydrus/blob/master/client.py)
Client can be used to query and check the server responses
