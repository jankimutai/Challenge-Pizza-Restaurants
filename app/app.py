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
class RestaurantResourceById(Resource):
    def get(self,id):
        restaurant= Restaurant.query.filter_by(id=id).first()
        if restaurant:
            # pizzas = Pizza.query.filter_by(id=id).all()
            restaurant_dict = {
                "id":restaurant.id,
                "name":restaurant.name,
                "address":restaurant.address,
                "pizzas": [{
                    "id":pizza_restaurant.pizza.id,
                    "name":pizza_restaurant.pizza.name,
                    "ingredients":pizza_restaurant.pizza.ingredients
                } for pizza_restaurant in restaurant.pizzas]
            }
            # restaurant_dict = restaurant.to_dict()
            response = make_response(jsonify(restaurant_dict),200)
            return response
        else:
            return {"error": "Restaurant not found"}, 404
api.add_resource(RestaurantResourceById,'/restaurants/<int:id>')
api.add_resource(RestaurantResource,'/restaurants')
if __name__ == '__main__':
    app.run(port=5555, debug=True)