#!/usr/bin/env python3
"""
Insert a document in Python
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection"""
    return mongo_collection.insert(kwargs)
