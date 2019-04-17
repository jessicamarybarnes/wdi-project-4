from app import db, ma
from marshmallow import fields
from .base import BaseModel
from .user import User

class Meal(db.Model, BaseModel):
    __tablename__ = 'meals'

    meal_name = db.Column(db.String(40), nullable=False)
    meal_image = db.Column(db.String(400), nullable=False)
    meal_price = db.Column(db.Float)
    taste_rating = db.Column(db.Float, nullable=False)
    more_info = db.Column(db.Text)
    restaurant_name = db.Column(db.String(40), nullable=False)
    restaurant_location = db.Column(db.String(40), nullable=False)
    experience_rating = db.Column(db.Float, nullable=False)
    restaurant_link = db.Column(db.String(400))
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    creator = db.relationship('User', backref='created_meals')


class MealSchema(ma.ModelSchema):
    creator = fields.Nested('UserSchema', only=('id', 'username'))
    ratings = fields.Nested('RatingSchema', many=True, only=('rating'))
    class Meta:
        model = Meal
