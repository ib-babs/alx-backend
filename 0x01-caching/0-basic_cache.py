#!/usr/bin/env python3
'''Class Model - BasicCache class'''
from basecache import BaseCaching
from typing import Any


class BasicCache(BaseCaching):
    '''BasicCache System. BaseCaching subclass'''

    def put(self, key, item) -> None:
        '''Populate the cache system'''
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key) -> Any:
        '''Get a value from the cache system with a key'''
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
