#!/usr/bin/env python3
'''Class Model - FIFOCache class'''
from typing import Any
from basecache import BaseCaching


class FIFOCache(BaseCaching):
    '''First-In First-Out cache system implements queue algorithm
    where the data that firstly comes in is evicted first in
    case of full memory in the system to save incoming data'''

    def __init__(self):
        '''Intitalization'''
        super().__init__()

    def put(self, key, item):
        '''Populate the cache system'''
        if key is None or item is None:
            return

        self.cache_data.update({key: item})
        first_item = list(self.cache_data.keys())[0]
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print(f"DISCARD: {first_item}")
            self.cache_data.pop(first_item)

    def get(self, key) -> Any:
        '''Get a value from the cache system with a key'''
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
