from flask import request, session,jsonify,make_response
from flask_restful import Resource
from config import db,app,api
from models import db, Pizza, Restaurant, PizzaRestaurant


class RestaurantResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()

        restaurant_dict = [{
            "id":restaurant.id,
            "name":restaurant.name,
            "address":restaurant.address
        }for restaurant in restaurants]

        response = make_response(jsonify(restaurant_dict),200)
        return response
api.add_resource(RestaurantResource,'/restaurants')
if __name__ == '__main__':
    app.run(port=5555, debug=True)