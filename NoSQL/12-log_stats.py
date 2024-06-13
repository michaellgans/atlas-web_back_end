#!/usr/bin/env python3
""" Task 12 - Log stats """

from pymongo import MongoClient


def log_stats():
    """
    Provides stats about Nginx logs

    Arguments:
     - None

    Returns:
     - Nginx Stats
    """
    client = MongoClient("mongodb://localhost:27017")

    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    get_status_count = collection.count_documents({"method:": "GET", "path": "/status"})
    print(f"{get_status_count} status check")
