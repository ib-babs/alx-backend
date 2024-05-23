#!/usr/bin/env python3
'''Class Model - LRUCache class'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''Most Recently Used cache system where the the most
    accessing item is evicted first in case of cache memory full
    in the system to save incoming data'''

    def __init__(self):
        '''Init'''
        super().__init__()
        self.recent_key = ''

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) <= BaseCaching.MAX_ITEMS:
            self.recent_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.recent_key]
            print(f"DISCARD: {self.recent_key}")
            self.recent_key = key

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return
        self.recent_key = key
        return self.cache_data.get(key)
