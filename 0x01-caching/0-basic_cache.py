#!/usr/bin/env python3
'''Class Model - BasicCache class'''
BaseCaching = __import__('basecache').BaseCaching


class BasicCache(BaseCaching):
    '''BasicCache System. BaseCaching subclass'''

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
