#!/usr/bin/python3
""" 0x01. Caching """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''inherits from BaseCaching and is an MRU caching system'''

    MRU = []

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''Add a new process to cache'''
        if not key or not item:
            return
        p_key = None
        if len(self.cache_data.items()) >= BaseCaching.MAX_ITEMS\
           and not self.cache_data.get(key):
            if len(MRUCache.MRU) > 0:
                p_key = MRUCache.MRU.pop(0)
            else:
                p_key = list(self.cache_data.keys())[0]
            del self.cache_data[p_key]
            print(f'DISCARD: {p_key}')
        if key in MRUCache.MRU:
            MRUCache.MRU.remove(key)
        MRUCache.MRU.insert(0, key)
        self.cache_data[key] = item

    def get(self, key):
        '''Gets a process from the cache'''
        if not key or not self.cache_data.get(key):
            return
        if key in MRUCache.MRU:
            MRUCache.MRU.remove(key)
        MRUCache.MRU.insert(0, key)
        return self.cache_data.get(key)
