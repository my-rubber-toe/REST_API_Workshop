from bson import objectid


class MovieModel:
    def __init__(self, **kwargs):

        # Dynamically set  properties of the movie if the key exists
        self.id = str(kwargs['_id']) if kwargs.get('_id') else None
        self.title = kwargs['title'] if kwargs.get('title') else None
        self.year = kwargs['year'] if kwargs.get('year') else None
        self.age = kwargs['age'] if kwargs.get('age') else None
        self.imdb = kwargs['imdb'] if kwargs.get('imdb') else None
        self.rotten_tomatoes = kwargs['rotten_tomatoes'] if kwargs.get('rotten_tomatoes') else None
        self.netflix = kwargs['netflix'] if kwargs.get('netflix') else None
        self.hulu = kwargs['hulu'] if kwargs.get('hulu') else None
        self.prime_video = kwargs['prime_video'] if kwargs.get('prime_video') else None
        self.disney_plus = kwargs['disney_plus'] if kwargs.get('disney_plus') else None
        self.directors = kwargs['directors'] if kwargs.get('directors') else None
        self.genres = kwargs['genres'] if kwargs.get('genres') else None
        self.country = kwargs['country'] if kwargs.get('country') else None
        self.language = kwargs['language'] if kwargs.get('language') else None
        self.runtime = kwargs['runtime'] if kwargs.get('runtime') else None

        # Best solution: Attributes must be accessed as the database attributes
        # for k in kwargs.keys():
        #     self.__setattr__(k, kwargs[k])

    def to_json(self):
        return {
            "_id": str(self.id),
            "title": self.title,
            "year": self.year,
            "age": self.age,
            "imdb": self.imdb,
            "rotten_tomatoes": self.rotten_tomatoes,
            "netflix": self.netflix,
            "hulu": self.hulu,
            "prine_video": self.prime_video,
            "disney_plus": self.disney_plus,
            "directors": self.directors,
            "genres": self.genres,
            "country": self.country,
            "language": self.language,
            "runtime": self.runtime
        }

    def __str__(self):
        return f"<MovieModel('_id':{self.id})>"
