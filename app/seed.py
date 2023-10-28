
from random import randint, choice,random

from faker import Faker

from app import app
from models import db, Pizza, Restaurant, PizzaRestaurant

fake = Faker()

with app.app_context():
    Pizza.query.delete()
    Restaurant.query.delete()
    PizzaRestaurant.query.delete()
    print("Seeding Restaurants \U0001F374")
    restaurant_names = [
    "GARDEN CHINESE",
    "ME. NICK'S",
    "SABOR LATINO RESTAURANT",
    "$1.25 PIZZA",
    "1001 NIGHTS CAFE",
    "1 2 3 BURGER SHOT BEER",
    "(LIBRARY)  FOUR & TWENTY BLACKBIRDS",
    "1 EAST 66TH STREET KITCHEN",
    "100 FUN"
    ]
    for name in restaurant_names:
        restaurant = Restaurant(name=name, address=fake.address())
        db.session.add(restaurant)
    
    print("Seeding Pizza \U0001F355")
    pizza_names = [
    "Cheese",
    "Pepperoni",
    "Margherita",
    "Hawaiian",
    "Meat Lovers",
    "Veggie",
    "BBQ Chicken",
    "Buffalo Chicken",
    "Supreme",
    "White Pizza"
    ]
    for name in pizza_names:
        pizza = Pizza(name=name, ingredients=fake.sentence())
        db.session.add(pizza)

    print("Seeding Pizza\U0001F355Restaurants\U0001F374")

    pizza_ids = [pizza.id for pizza in Pizza.query.all()]
    for restaurant in Restaurant.query.all():
        pizza_restaurant = PizzaRestaurant(price = randint(7,30),pizza_id = choice(pizza_ids),restaurant_id = restaurant.id)
        db.session.add(pizza_restaurant)
    db.session.commit()
    print("Done Seeding \U0001F44D")

