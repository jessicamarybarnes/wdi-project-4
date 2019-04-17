from flask import Blueprint, jsonify, request
from models.meal import Meal, MealSchema
from models.rating import Rating, RatingSchema

meals_schema = MealSchema(many=True)
one_meal_schema = MealSchema()

api = Blueprint('meals', __name__)

# INDEX ROUTE
@api.route('/meals', methods=['GET'])
def index():
    meals = Meal.query.all()
    return meals_schema.jsonify(meals, many=True), 200

# SHOW ROUTE
@api.route('/meals/<int:meal_id>', methods=['GET'])
def show(meal_id):
    meal = Meal.query.get(meal_id)
    return one_meal_schema.jsonify(meal), 200

# CREATE ROUTE
@api.route('/meals', methods=['POST'])
def create():
    data = request.get_json()
    meal, errors = one_meal_schema.load(request.get_json())
    if errors:
        return jsonify(errors, 422)
    meal.save()
    return one_meal_schema.jsonify(meal)

# EDIT ROUTE
@api.route('/meals/<int:meal_id>', methods=['PUT'])
def update(meal_id):
    meal = Meal.query.get(meal_id)
    meal, errors = one_meal_schema.load(request.get_json(), instance=meal, partial=True)
    if errors:
        return jsonify(errors), 422
    print()

    meal.save()
    return one_meal_schema.jsonify(meal)

# DELETE ROUTE
@api.route('/meals/<int:meal_id>', methods=['DELETE'])
def delete(meal_id):
    meal = Meal.query.get(meal_id)

    meal.remove()
    return '', 204

# ..............RATINGS......................
rating_schema = RatingSchema()

# CREATE ROUTE
@api.route('/meals/<int:meal_id>/rating', methods=['POST'])
def createRating(meal_id):
    meal = Meal.query.get(meal_id)
    data = request.get_json()
    rating, errors = rating_schema.load(request.get_json())
    if errors:
        return jsonify(errors, 422)
    rating.meal = meal
    rating.save()
    return rating_schema.jsonify(rating)
