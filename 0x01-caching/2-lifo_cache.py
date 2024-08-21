#!/usr/bin/python3
""" 0x01. Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''inherits from BaseCaching and is a caching system'''
    last_process = ''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''Add a new process to cache'''
        if not key or not item:
            return
        if len(self.cache_data.items()) >= BaseCaching.MAX_ITEMS\
           and not self.cache_data.get(key):
            l_key = LIFOCache.last_process
            del self.cache_data[l_key]
            print(f'DISCARD: {l_key}')
        self.cache_data[key] = item
        LIFOCache.last_process = key

    def get(self, key):
        '''Gets a process from the cache'''
        if not key or not self.cache_data.get(key):
            return
        return self.cache_data.get(key)
