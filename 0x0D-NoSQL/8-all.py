#!/usr/bin/env python3
"""module with pymongo function"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    return mongo_collection.find() or []


if __name__ == "__main__":
    list_all(mongo_collection)
