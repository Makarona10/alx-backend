#!/usr/bin/python3
""" 0x01. Caching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' inherits from BaseCaching and is a caching system '''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''Add a new process to cache'''
        if not key or not item:
            return
        if len(self.cache_data.items()) >= BaseCaching.MAX_ITEMS\
           and not self.cache_data.get(key):
            f_key = list(self.cache_data.keys())[0]
            del self.cache_data[f_key]
            print(f'DISCARD: {f_key}')
        self.cache_data[key] = item

    def get(self, key):
        '''Gets a process from the cache'''
        if not key or not self.cache_data.get(key):
            return
        return self.cache_data.get(key)
