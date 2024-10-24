#!/usr/bin/env python3
"""Inserts a document"""
import pymongo
from pymomgo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """Returns mongo collection"""
    return mongo_collection.insert(kwargs)
