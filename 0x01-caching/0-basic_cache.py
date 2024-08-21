#!/usr/bin/python3
""" 0x01. Caching """

from BaseCacheClass import BaseCaching


class BasicCache(BaseCaching):
    '''BasicCache that inherits from BaseCaching and is a caching system'''
    def __init__(self):
        '''BasicCache initialization'''
        super().__init__()

    def put(self, key, item):
        '''Add a new process to cache'''
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''Gets a process from the cache'''
        if not key or not self.cache_data.get(key):
            return
        return self.cache_data.get(key)
