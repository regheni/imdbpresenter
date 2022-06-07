import os

PREFIX = "imdbpresenter"

def config():
    env = os.environ.get("imdbpresenter", "local")
    dict(env=env)
