from crypt import methods
from flask import Flask, request, render_template, url_for, redirect, abort
import os
import sqlite3
import pdb

app = Flask(__name__, static_url_path="/static", template_folder="./templates")


def get_movie():
    conn = sqlite3.connect("src/imdbpresenter/static/imdb.db")
    cur = conn.cursor()
    cur.execute("SELECT title, url, images from movies")
    rows = cur.fetchall()
    d = []
    for title, link, image in rows:
        d.append({"title": title, "url": link, "images": image})
    return d


db = get_movie()

movies = []
total_items = 0
for movie in db:
    for key, value in movie.items():
        total_items += 1
        tmp = []
        # I need to carry both key and value information
        tmp.extend([key, value])
        movies.append(tmp)

#    start_pos = 0 if page == 1 else items_per_page * (page - 1)
#   https://askdevz.com/question/423308-how-to-display-a-list-across-multiple-pages-in-flask
@app.route("/movies/", defaults={"page_nr": 1})
@app.route("/movies/page=<int:page_nr>&items=<int:item_nr>", methods=["GET", "POST"])
def movies_page(page_nr):
    total_items = movies
    items_per_page = request.args.get("items", 5, type=int) * 3
    current_page = request.args.get("page", 1, type=int)
    page_nr = current_page

    if page_nr == 1:
        page_possition = 0
    elif page_nr > 1 and page_nr <= len(total_items) // items_per_page:
        page_possition = items_per_page * (page_nr - 1)
    else:
        page_possition = 0

    return render_template(
        "movie.html",
        total_items=total_items[page_possition : page_possition + items_per_page],
        current_page=current_page,
    )


if __name__ == "__main__":
    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True)