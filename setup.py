from setuptools import setup, find_packages

setup(
    name="imdbpresenter",
    version="0.0.1",
    description="imdbpresenter",
    author="Team",
    author_email="",
    # url="https://github.com/CleverSoftwareSolutions/fashion_flask/",
    package_dir={"": "src/"},
    packages=find_packages("src/"),
)