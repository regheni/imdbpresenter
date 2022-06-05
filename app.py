from flask import Flask

app = Flask(__name__)


@app.route("/team/<int:post_id>")
def hello_world(post_id):
    if post_id != 0:
        print(1 / post_id)
    return "<p>Hello, World!</p>"


@app.route("/")
def hello_world2():
    return "<p>Hello sss</p>"

