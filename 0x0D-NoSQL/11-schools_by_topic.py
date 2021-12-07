#!/usr/bin/env python3
"""module with pymongo function"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of schools having a specific topic"""
    return mongo_collection.find({"topics": topic})


if __name__ == "__main__":
    schools_by_topic(mongo_collection, topic)
