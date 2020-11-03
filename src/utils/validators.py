from marshmallow import Schema, fields, validate


class CreateMovieValidator(Schema):
    title = fields.String(required=True)
    year = fields.Integer(required=True)
    age = fields.String(required=True)
    imdb = fields.Float(required=True)
    rotten_tomatoes = fields.String(required=True)
    netflix =  fields.Integer(required=True)
    hulu = fields.Integer(required=True)
    prime_video = fields.Integer(required=True)
    disney_plus = fields.Integer(required=True)
    directors = fields.String(required=True)
    genres = fields.String(required=True)
    country = fields.String(required=True)
    language = fields.String(required=True)
    runtime = fields.Integer(required=True)

class UpdateMovieValidator(Schema):
    title = fields.String()
    year = fields.Integer()
    age = fields.String()
    imdb = fields.Float()
    rotten_tomatoes = fields.String()
    netflix =  fields.Integer()
    hulu = fields.Integer()
    prime_video = fields.Integer()
    disney_plus = fields.Integer()
    directors = fields.String()
    genres = fields.String()
    country = fields.String()
    language = fields.String()
    runtime = fields.Integer()
