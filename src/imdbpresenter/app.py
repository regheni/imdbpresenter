from flask import Flask, render_template
import json
import os
#import ipdb
from imdbpresenter.configuration import config

app = Flask(__name__, template_folder="static")
# app.config.update(config().as_dic())
from imdbpresenter.controllers.movies import movies_blueprint

app.register_blueprint(movies_blueprint)

if __name__ == "__main__":
    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True)
