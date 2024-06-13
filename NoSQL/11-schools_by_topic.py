#!/usr/bin/env python3
""" Task 11 - Where can I learn Python? """


def schools_by_topic(mongo_collection, topic):
    """
    List all documents in mongo_collection

    Arguments:
     - mong_collection: the collection
     - topic: subject taught at school

    Returns:
     - All documents in that collection
    """
    results_cursor = mongo_collection.find({"topics": topic})

    documents_found = []

    for document in results_cursor:
        documents_found.append(document)

    return documents_found
