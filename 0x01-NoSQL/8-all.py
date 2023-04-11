#!/usr/bin/env python3
"""List all documents in python"""


def list_all(mongo_collection):
    result = []

    cur = db.mongo_collection.find()
    for doc in cur:
        result.append(doc)

    return result
