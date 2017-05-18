## Contains all contexts related to the coffeeshop-api

entrypoint_context = {
    "@context": {
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "vocab": "http://192.168.23.2:5000/api/vocab",
        "EntryPoint": "vocab:EntryPoint",
        "products": {
            "@id": "vocab:EntryPoint/products",
            "@type": "@id"
        }
    }
}

product_collection_context = {
    "@context": {
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "vocab": "http://192.168.23.2:5000/api/vocab",
        "ProductCollection": "vocab:ProductCollection",
        "members": "http://www.w3.org/ns/hydra/core#member"
    }
}

product_context = {
    "@context": {
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "vocab": "http://192.168.23.2:5000/api/vocab",
        "Product": "http://schema.org/Product",
        "name": "http://schema.org/name",
        "description": "http://schema.org/description",
        "price": "http://schema.org/price",
        "id": "http://schema.org/productID"

    }
}
