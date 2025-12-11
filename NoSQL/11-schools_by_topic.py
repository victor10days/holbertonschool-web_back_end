#!/usr/bin/env python3
"""
Module that returns the list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic (string): the topic searched

    Returns:
        List of schools that have the specified topic
    """
    schools = list(mongo_collection.find({"topics": topic}))
    return schools
