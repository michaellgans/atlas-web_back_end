#!/usr/bin/env python3
""" Task 10 - Change school topics """


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a document by name.

    Arguments:
     - mong_collection: the collection
     - name: name of school
     - topic: subject at school

    Returns:
     - Key: Value pairs
    """
    results_cursor = mongo_collection.update_many({"name": name},\
                     {"$set": {"topics": topics}})

    return results_cursor.modified_count
