from imdbpresenter import ROOT_PATH
import os
import json

JSON_URL = os.path.join(ROOT_PATH, "src/imdbpresenter/static", "imdb_movie.json")

class Movie:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @classmethod
    def all(cls):
        all_movies = []
        with open(JSON_URL) as f:
            for json_obj in f:
                movie_dict = json.loads(json_obj)
                movie = Movie(**movie_dict)
                all_movies.append(movie)
        return all_movies

    def to_json(self):
        return dict(title=self.title, genres=self.genres)

    @classmethod
    def first(cls):
        return cls.all()[0]