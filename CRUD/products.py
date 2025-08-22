from flask import Flask, jsonify, request 
import json 
from flask_cors import CORS
app = Flask("Product Server")
CORS(app)


products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]

@app.route("/products/<id>", methods=["GET", "PUT", "DELETE"])
def product_methods(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    if request.method == "GET":
    	return jsonify(product)
    if request.method == "PUT":
        updated_product = json.loads(request.data)
        for key, value in updated_product.items():
            product[key] = value
        return '', 204
    if request.method == "DELETE":
        products.remove(product)
        return '', 204
@app.route("/products", methods=["GET", "POST"])
def products_methods(): 
    if request.method == "GET":
        return jsonify(products)
    if request.method == "POST":
        products.append(request.get_json())
        return '', 201
app.run(port=5000,debug=True)
