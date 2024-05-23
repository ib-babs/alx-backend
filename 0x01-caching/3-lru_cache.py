#!/usr/bin/env python3
'''Class Model - LRUCache class'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''Last Recently Used cache system where the the least
    access item is evicted first in case of full memory
    in the system to save incoming data'''

    def __init__(self):
        '''Init'''
        super().__init__()
        self.static_keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if key in self.static_keys:
            self.static_keys.remove(key)
        self.static_keys.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = self.static_keys.pop(0)
            del self.cache_data[discard_key]
            print(f"DISCARD: {discard_key}")

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.static_keys:
            return
        self.static_keys.remove(key)
        self.static_keys.append(key)
        return self.cache_data.get(key)
