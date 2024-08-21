#!/usr/bin/python3
""" 0x01. Caching """

BaseCaching = __import__('BaseCacheClass').BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        super.__init__()

    def put(self, key, item):
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        if not key or not self.cache_data.get(key):
            return
        return self.cache_data.get(key)
