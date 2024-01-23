#!/usr/bin/env python3
"""
List all documents
"""
import pymongo


def list_all(mongo_collection):
    """
    function to list all documents
    """
    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    return [post for post in documents]
