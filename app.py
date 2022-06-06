from flask import Flask, render_template
import json
import os
import ipdb
app = Flask(__name__, template_folder="static")


# def validate_input(number):
#     return number != 0


@app.route("/movies")
def movie_page():
    file_data = 0
    file_data = []
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "imdb_movie.json")
    with open(json_url) as f:
        for jsonObj in f:
            movie_dict = json.loads(jsonObj)
            file_data.append(movie_dict)
    f.close()
    count = -1
    for line in file_data:
        count += 1
        _images = line["images"]
        images_urls = line["image_urls"]
        if len(_images) > 0:
            first_item_images = _images[0]
            image_url = "media/" + first_item_images["path"]
            line["images"] = image_url
            first_item_image_url = images_urls[0]
            line["image_urls"] = first_item_image_url
            file_data[count] = line

    return render_template("templates/index.html", file_data=file_data)


if __name__ == "__main__":
    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True)