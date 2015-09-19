from __future__ import absolute_import

from pymongo import MongoClient
from confpages.contrib.loaders import MongoLoader


class RealMongoLoader(MongoLoader):
    """MongoDB-based page loader."""

    #: The database instance
    database = MongoClient().test

    #: The collection name
    collection_name = 'page'
