from bson import objectid


class MovieModel:
    def __init__(self, **kwargs):

        # Extract the keys from the database model
        dictionary_keys = kwargs.keys()

        # Dynamically set  properties of the movie if the key exists
        self.id = str(kwargs['_id']) if dictionary_keys.__contains__('_id') else None
        self.title = kwargs['Title'] if dictionary_keys.__contains__('Title') else None
        self.year = kwargs['Year'] if dictionary_keys.__contains__('Year') else None
        self.age = kwargs['Age'] if dictionary_keys.__contains__('Age') else None
        self.imdb = kwargs['IMDb'] if dictionary_keys.__contains__('IMDb') else None
        self.rotten_tomatoes = kwargs['Rotten Tomatoes'] if dictionary_keys.__contains__('Rotten Tomatoes') else None
        self.netflix = kwargs['Netflix'] if dictionary_keys.__contains__('Netflix') else None
        self.hulu: int = kwargs['Hulu'] if dictionary_keys.__contains__('Hulu') else None
        self.prime_video: int = kwargs['Prime Video'] if dictionary_keys.__contains__('Prime Video') else None
        self.disney_plus: int = kwargs['Disney+'] if dictionary_keys.__contains__('Disney+') else None
        self.type = kwargs['Type'] if dictionary_keys.__contains__('Type') else None
        self.directors: list = kwargs['Directors'] if dictionary_keys.__contains__('Directors') else None
        self.genres: list = kwargs['Genres'] if dictionary_keys.__contains__('Genres') else None
        self.country: str = kwargs['Country'] if dictionary_keys.__contains__('Country') else None
        self.language: str = kwargs['Language'] if dictionary_keys.__contains__('Language') else None
        self.runtime: int = kwargs['Runtime'] if dictionary_keys.__contains__('Runtime') else None

        # Best solution: Attributes must be accessed as the database attributes
        # for k in kwargs.keys():
        #     self.__setattr__(k, kwargs[k])

    def to_json(self):
        return {
            "_id": str(self.id),
            "Title": self.title,
            "Year": self.year,
            "Age": self.age,
            "IMDb": self.imdb,
            "Rotten Tomatoes": self.rotten_tomatoes,
            "Netflix": self.netflix,
            "Hulu": self.hulu,
            "Prime Video": self.prime_video,
            "Disney+": self.disney_plus,
            "Type": self.type,
            "Directors": self.directors,
            "Genres": self.genres,
            "Country": self.country,
            "Language": self.language,
            "Runtime": self.runtime
        }

    def __str__(self):
        return f"<MovieModel('_id':{self.id})>"
