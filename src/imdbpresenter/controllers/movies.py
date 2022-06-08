from flask import Flask, Blueprint, jsonify, render_template
import os
import json
from imdbpresenter import ROOT_PATH
from imdbpresenter.models.movie import Movie
import ipdb

movies_blueprint = Blueprint("movies", __name__)

@movies_blueprint.route("/movies")
def index():
    all_movies = Movie.all()


    file_data = []
    count = 0

    for line in all_movies:

        # count += 1
        # print(line["images"])
        # imaages = line["images"]
        # images_urls = line["image_urls"]
        # if len(imaages) > 0:
        #     first_item_images = imaages [0]
        #     image_url = "media/full/" + first_item_images["path"]
        #     line["images"] = image_url
        #     first_item_image_url = images_urls [0]
        #     line["image_urls"] = first_item_image_url
        #     file_data[count] = line
        # ipdb.set_trace()
        return render_template("templates/movies/index.html", line = line.to_json())
