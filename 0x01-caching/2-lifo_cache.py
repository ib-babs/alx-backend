#!/usr/bin/python3
'''Class Model - LIFOCache class'''
from typing import Any
from basecache import BaseCaching


class LIFOCache(BaseCaching):
    '''Last-In First-Out cache system implements stack algorithm
    where the data that lastly comes in is evicted first in
    case of full memory in the system to save incoming data'''

    def __init__(self):
        '''Intitalization'''
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        '''Populate the cache system'''
        self.cache_data
        if key and item:
            self.cache_data.update({key: item})
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print(f"DISCARD: {self.last_key}")
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key) -> Any:
        '''Get a value from the cache system with a key'''
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
