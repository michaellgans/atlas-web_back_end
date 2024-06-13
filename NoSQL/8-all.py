#!/usr/bin/env python3
""" Task 8 - Lists all documents in a collection """


def list_all(mongo_collection):
    """
    List all documents in mongo_collection

    Arguments:
     - mong_collection: the collection

    Returns:
     - All documents in that collection
    """
    results_cursor = mongo_collection.find({})

    documents_found = []

    for document in results_cursor:
        documents_found.append(document)

    return documents_found
