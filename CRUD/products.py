from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask("Product Server")
CORS(app)


products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]

@app.route("/products", method="["GET"])
def get_products():
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    return jsonify(products)





app.run(port=5000,debug=True)
