import os
from pymongo import MongoClient


def get_db(app):
    client = MongoClient(_get_mongo_db_url())
    app.db = client.raizen


def _get_mongo_db_url() -> str:
    username = os.getenv('MONGO_USERNAME')
    password = os.getenv('MONGO_PASSWORD')
    hostname = os.getenv('MONGO_HOSTNAME')
    port = os.getenv('MONGO_PORT')

    return f"mongodb://{username}:{password}@{hostname}:{port}/"
