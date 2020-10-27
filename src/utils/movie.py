from bson import objectid


class MovieModel:
    def __init__(self, **kwargs):
        self.id: objectid = kwargs['_id']
        self.title: str = kwargs['Title']
        self.year: int = kwargs['Year']
        self.age: int = kwargs['Age']
        self.imdb: float = kwargs['IMDb']
        self.rotten_tomatoes = kwargs['Rotten Tomatoes']
        self.netflix = kwargs['Netflix']
        self.hulu = kwargs['Hulu']
        self.prime_video = kwargs['Prime Video']
        self.disney_plus = kwargs['Disney+']
        self.type = kwargs['Type']
        self.directors: list = kwargs['Directors']
        self.genres: list = kwargs['Genres']
        self.country: str = kwargs['Country']
        self.language: str = kwargs['Language']
        self.runtime: int = kwargs['Runtime']
