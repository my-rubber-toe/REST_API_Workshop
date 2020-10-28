from bson import objectid


class MovieModel:
    def __init__(self, **kwargs):

        # Extract the keys from the database model
        dictionary_keys = kwargs.keys()

        # Dynamically set  properties of the movie if the key exists
        self.id = str(kwargs['_id']) if dictionary_keys.__contains__('_id') else None
        self.title = kwargs['title'] if dictionary_keys.__contains__('title') else None
        self.year = kwargs['year'] if dictionary_keys.__contains__('year') else None
        self.age = kwargs['age'] if dictionary_keys.__contains__('age') else None
        self.imdb = kwargs['imdb'] if dictionary_keys.__contains__('imdb') else None
        self.rotten_tomatoes = kwargs['rotten_tomatoes'] if dictionary_keys.__contains__('rotten_tomatoes') else None
        self.netflix = kwargs['netflix'] if dictionary_keys.__contains__('netflix') else None
        self.hulu = kwargs['hulu'] if dictionary_keys.__contains__('hulu') else None
        self.prime_video = kwargs['prime_video'] if dictionary_keys.__contains__('prime_video') else None
        self.disney_plus = kwargs['disney_plus'] if dictionary_keys.__contains__('disney_plus') else None
        self.directors = kwargs['directors'] if dictionary_keys.__contains__('directors') else None
        self.genres = kwargs['genres'] if dictionary_keys.__contains__('genres') else None
        self.country = kwargs['country'] if dictionary_keys.__contains__('country') else None
        self.language = kwargs['language'] if dictionary_keys.__contains__('language') else None
        self.runtime = kwargs['runtime'] if dictionary_keys.__contains__('runtime') else None

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
