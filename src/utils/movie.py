from bson import objectid


class MovieModel:
    def __init__(self, **kwargs):
        self.id: objectid = kwargs['_id']
        self.title: str = kwargs['Title']
        self.year: int = kwargs['Year']
        self.age: int = kwargs['Age']
        self.imdb: float = kwargs['IMDb']
        self.rotten_tomatoes: str = kwargs['Rotten Tomatoes']
        self.netflix: int = kwargs['Netflix']
        self.hulu: int = kwargs['Hulu']
        self.prime_video: int = kwargs['Prime Video']
        self.disney_plus: int = kwargs['Disney+']
        self.type = kwargs['Type']
        self.directors: list = kwargs['Directors']
        self.genres: list = kwargs['Genres']
        self.country: str = kwargs['Country']
        self.language: str = kwargs['Language']
        self.runtime: int = kwargs['Runtime']

    def to_json(self):
        
        return {
            "_id": self.id,
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
        return f"<MovieModel('Title':{self.title})>"
