from flask import Flask, Blueprint, jsonify, render_template
import os
import json
from imdbpresenter import ROOT_PATH
from imdbpresenter.models.movie import Movie

movies_blueprint = Blueprint("movies", __name__)

@movies_blueprint.route("/movies")
def index():
    all_movies = Movie.all()
    import ipdb

    ipdb.set_trace()

    file_data = []

    for line in file_data:
        count += 1
        _images = line["image"]
        images_urls = line["image_urls"]
        if len(_images) > 0:
            first_item_images = _images [0]
            image_url = "media/full/" + first_item_images["path"]
            line["images"] = image_url
            first_item_image_url = images_urls [0]
            line["image_urls"] = first_item_image_url
            file_data[count] = line

    return render_template("templates/movies/index.html", file_data = file_data)
