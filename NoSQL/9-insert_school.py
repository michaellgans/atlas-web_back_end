#!/usr/bin/env python3
""" Task 9 - Insert a Document in Python """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a collection

    Arguments:
     - mong_collection: the collection

    Returns:
     - The inserted id (key: value)
    """
    results_cursor = mongo_collection.insert_one(kwargs)

    return results_cursor.inserted_id
