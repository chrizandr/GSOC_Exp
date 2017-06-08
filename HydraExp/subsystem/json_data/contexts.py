"""Contexts related to SubSystems API."""

entrypoint_context = {
    "@context": {
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "vocab": "http://192.168.23.2:5000/api/vocab",
        "EntryPoint": "vocab:EntryPoint",
        "SubSystems": {
            "@id": "vocab:EntryPoint/SubSystems",
            "@type": "@id"
        },
        "SubSystem": {
            "@id": "vocab:EntryPoint/SubSystem",
            "@type": "@id"
        }
    }
}

subsystem_collection_context = {
    "@context": {
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "vocab": "http://192.168.23.2:5000/api/vocab",
        "SubSystemCollection": "vocab:SubSystemCollection",
        "members": "http://www.w3.org/ns/hydra/core#member"
    }
}

subsystem_context = {
    "@context": {
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "vocab": "http://192.168.23.2:5000/api/vocab",
        "SubSystem": "http://ontology.projectchronos.eu/subsystems",
        "name": "http://schema.org/name",
        "description": "http://schema.org/description",
        "price": "http://schema.org/price",
        "id": "http://schema.org/productID"

    }
}
