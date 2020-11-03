from marshmallow import Schema, fields, validate


class CreateMovieValidator(Schema):
    title = fields.String()
    year = fields.Integer(),
    age = fields.Integer(),
    imdb = fields.String(),
    rotten_tomatoes = fields.Float(),
    netflix =  fields.String(),
    hulu = fields.Integer(),
    prime_video = fields.Integer(),
    disney_plus = fields.Integer(),
    _type = fields.Integer(),
    directors = fields.String(),
    genres = fields.String(),
    country = fields.String(),
    language = fields.String(),
    runtime = fields.Integer()
