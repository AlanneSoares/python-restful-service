from flask import Flask, jsonify, request, json
import scritp

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
@app.route("/api/restaurants/<int:restaurant_id>", methods=["GET"])
def find_by_id(restaurant_id: int):
    for restaurant in restaurants:
        if restaurant.get("id") == restaurant_id:
            return jsonify({"restaurant": restaurant}), 200
        else:
            return jsonify({"error": "Bad request"}), 400
    return jsonify({"error": "Internal server error"}), 500


## Find by postal code (with params)
@app.route("/api/restaurants/address", methods=["GET"])
def find_by_postal_code():
    postalcode = request.args.get("postalcode")
    for restaurant in restaurants:
        if restaurant.get("address").get("postalCode") == postalcode:
            return jsonify({"restaurant": restaurant}), 200
        else:
            return jsonify({"error": "Bad request"}), 400
    return jsonify({"error": "Internal server error"}), 500


## Find by street address
@app.route("/api/restaurants/address", methods=["GET"])
def find_by_street_address():
    streetaddress = request.args.get("streetaddress")
    print(streetaddress)
    for restaurant in restaurants:
        if restaurant.get("address").get("streetAddress") == streetaddress:
            return jsonify({"restaurant": restaurant}), 200
        else:
            return jsonify({"error": "Bad request"}), 400
    return jsonify({"error": "Internal server error"}), 500


## Find by address region
def find_by_address_region():
    addressregion = request.args.get("addressRegion")
    for restaurant in restaurants:
        if restaurant.get("address").get("addressRegion") == addressregion:
            return jsonify({"restaurant": restaurant}), 200
        else:
            return jsonify({"error": "Bad request"}), 400
    return jsonify({"error": "Internal server error"}), 500


## Find by address country
def find_by_address_country():
    addresscountry = request.args.get("addressCountry")
    for restaurant in restaurants:
        if restaurant.get("address").get("addressCountry") == addresscountry:
            return jsonify({"restaurant": restaurant}), 200
        else:
            return jsonify({"error": "Bad request"}), 400
    return jsonify({"error": "Internal server error"})


## Find by postal code (in the request body)
@app.route("/api/restaurants/address", methods=["POST"])
def find_by_postal_code_address():
    postalcode = request.json.get("postalCode")
    for restaurant in restaurants:
        if restaurant.get("address").get("postalCode") == postalcode:
            return jsonify({"restaurant": restaurant}), 200
        else:
            return jsonify({"error": "Bad request"}), 400
    return jsonify({"error": "Internal server error"}), 500


## Update address by id
@app.route("/api/restaurants/<int:restaurant_id>/address", methods=["PUT"])
def update_address_by_id(restaurant_id: int):
    changed_restaurant = request.json
    for index, restaurant in enumerate(restaurants):
        if restaurant.get("id") == restaurant_id:
            restaurants[index].update(changed_restaurant)
            return jsonify({"restaurant": restaurants[index]}), 200
        else:
            return jsonify({"error": "Bad request"}), 400
    return jsonify({"error": "Internal server error"}), 500


## Update postal code
def updatePostalCode(postalcode: str):
    postalcode = request.json.get("postalCode")


## Update street address
# def updateStreetAddress():

## Update address locality
# def updateAddressLocality():

## Update address region
# def updateAddressRegion():

## Update address country
# def updateAddressCountry():

## Delete by id
# def deleteById(id):


if __name__ == "__main__":
    app.run(HOST, PORT, debug=True)
