"""
DAL : Data Access Layer

This module contains code to retrieve and store data (data manipulation)
"""

import json


def load_db():
    file_path = "/Users/prashant/PICT/VELOCITY 10Sep/test_flask_v2/models/flashcard_db.json"
    with open(file_path, "r") as foo:
        return json.load(foo)

db = load_db()
