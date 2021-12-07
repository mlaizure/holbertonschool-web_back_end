#!/usr/bin/env python3
"""module with pymongo function"""


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    return mongo_collection.aggregate([
        {"$unwind": {"path": "$topics"}},
        {"$group": {"_id": "$_id",
                    "name": {"$first": "$name"},
                    "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
