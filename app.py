from flask import Flask, request, jsonify
import requests
import uuid

app = Flask(__name__)

inventory = []

def find_item(item_id):
    return next((item for item in inventory if item["id"] == item_id), None)

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory), 200

@app.route('/inventory/<item_id>', methods=['GET'])
def get_item(item_id):
    item = find_item(item_id)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

@app.route('/inventory', methods=['POST'])
def add_item():
    data = request.json
    barcode = data.get("barcode")
    if barcode and not data.get("product_name"):
        url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
        response = requests.get(url).json()
        if response.get("status") == 1:
            product = response.get("product", {})
            data["product_name"] = product.get("product_name", "Unknown")
            data["brands"] = product.get("brands", "Unknown")
    new_item = {
        "id": str(uuid.uuid4())[:8], 
        "barcode": barcode,
        "product_name": data.get("product_name", "Unknown Product"),
        "brands": data.get("brands", "Unknown"),
        "price": data.get("price", 0.0),
        "stock": data.get("stock", 0)
    }

    inventory.append(new_item)
    return jsonify(new_item), 201

@app.route('/inventory/<item_id>', methods=['PATCH'])
def update_item(item_id):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    data = request.json
    item.update({k: v for k, v in data.items() if k in item})
    return jsonify(item), 200

@app.route('/inventory/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    inventory.remove(item)
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)