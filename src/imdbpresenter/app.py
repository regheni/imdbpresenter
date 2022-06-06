from flask import Flask, request, render_template, url_for, redirect, abort
import json
import os
import ipdb

app = Flask(__name__, template_folder="static", template_folder="./templates")


# def validate_input(number):
#     return number != 0


@app.route("/movies")
@app.route("/movies/page=<int:page_nr>&items=<int:item_nr>", methods=['GET', 'POST'])


def movie_page():
    file_data = 0
    file_data = []
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "imdb_movie.json")
    items_per_page = request.args.get("items", 5, type=int)
    current_page = request.args.get("page", 1, type=int)
    page_nr = current_page

    if page_nr == 1:
        page_position = 0
    elif page_nr > 1 and page_nr <= len(total_items) // items_per_page:
        page_position = items_per_page * (page_nr -1)
    else:
        page_position = 0

    return render_template("movie.html", total_items[page_position : page_position + items_per_page], current_page=current_page)


    with open(json_url) as f:
        for json_obj in f:
            movie_dict = json.loads(json_obj)
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
