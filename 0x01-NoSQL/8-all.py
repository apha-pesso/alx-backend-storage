#!/usr/bin/env python3
"""List all documents in python"""


def list_all(mongo_collection):
    '''List all'''
    result = []

    cur = mongo_collection.find()
    for doc in cur:
        result.append(doc)

    return result
