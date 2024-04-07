from flask import Flask, jsonify, request, json

app = Flask(__name__)
HOST = "localhost"
PORT = "4999"

## Open file datas
with open('datas/restaurants.json') as file:
    restaurants = json.load(file)

## Insert
@app.route("/restaurants", methods=["POST"])
def insert():
    restaurant = request.json
    restaurants.append(restaurant)
    return jsonify({"restaurant": restaurant}), 201


## Find all
@app.route("/restaurants", methods=["GET"])
def find_all():
    return jsonify({"restaurants": restaurants}), 200


## Find by id
@app.route("/api/restaurant/<int:restaurant_id>", methods=["GET"])
def find_by_id(restaurant_id: int):
    for restaurant in restaurants:
        if restaurant.get("id") == restaurant_id:
            return jsonify({"restaurant": restaurant}), 200
    return jsonify({"error": "Bad request"}), 400


## Find by postal code (with params)
@app.route("/api/restaurant/address", methods=["GET"])
def find_by_address_parameters():
    for restaurant in restaurants:
        if (restaurant.get("address").get("postalCode") == request.args.get("postalcode")
                or restaurant.get("address").get("streetAddress") == request.args.get("streetaddress")
                or restaurant.get("address").get("addressRegion") == request.args.get("addressRegion")
                or restaurant.get("address").get("addressCountry") == request.args.get("addressCountry")):
            return jsonify({"restaurant": restaurant}), 200
        else:
            return jsonify({"error": "Bad request"}), 400
    return jsonify({"error": "Internal server error"}), 500


## Find by postal code (in the request body)
@app.route("/api/restaurant/address", methods=["POST"])
def find_by_postal_code_address():
    postalcode = request.json.get("postalCode")
    for restaurant in restaurants:
        if restaurant.get("address").get("postalCode") == postalcode:
            return jsonify({"restaurant": restaurant}), 200
    return jsonify({"error": "Bad request"}), 400


## Update address by id
@app.route("/api/restaurant/<int:restaurant_id>", methods=["PUT"])
def update_by_id(restaurant_id: int):
    changed_restaurant = request.json
    for index, restaurant in enumerate(restaurants):
        if restaurant.get("id") == restaurant_id:
            restaurants[index].update(changed_restaurant)
            return jsonify({"restaurant": restaurants[index]}), 200
    return jsonify({"error": "Bad request"}), 400


## Delete by id
@app.route("/api/restaurant/<int:restaurant_id>", methods=["DELETE"])
def delete_by_id(restaurant_id: int):
    for index, restaurant in enumerate(restaurants):
        if restaurant.get("id") == restaurant_id:
            del restaurants[index]
            return jsonify({"restaurant": restaurants}), 200
        else:
            return jsonify({"restaurant": "Empty list"}), 200
    return jsonify({"error": "Bad request"}), 400


if __name__ == "__main__":
    app.run(HOST, PORT, debug=True)
