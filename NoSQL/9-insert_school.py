#!/usr/bin/env python3
"""
Module that inserts a new document in a MongoDB collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs

    Args:
        mongo_collection: pymongo collection object
        **kwargs: keyword arguments representing the document fields

    Returns:
        The new _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
