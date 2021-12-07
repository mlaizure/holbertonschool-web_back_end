#!/usr/bin/env python3
"""module with pymongo function"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collecciton based on kwargs"""
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id


if __name__ == "__main__":
    insert_school(mongo_collection, **kwargs)
