from app import db, ma
from marshmallow import fields
from .base import BaseModel
from .user import User

class Rating(db.Model, BaseModel):
    __tablename__ = 'ratings'

    rating = db.Column(db.Float, nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id'))
    meal = db.relationship('Meal', backref='ratings')

class RatingSchema(ma.ModelSchema):

    class Meta:
        model = Rating
