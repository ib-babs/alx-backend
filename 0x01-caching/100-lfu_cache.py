#!/usr/bin/env python3
'''Class Model - LFUCache class'''
from basecache import BaseCaching


def remove_min(dic):
    'Return min data from dict and it key'
    lss = min(dic.values())
    if dic:
        for k, v in dic.items():
            if lss == v:
                return (lss, k)
    return None


class LFUCache(BaseCaching):
    '''Least Frequently Used cache system where the the least
    frequent item is evicted first in case of cache memory full
    in the system to save incoming data'''

    def __init__(self):
        '''Init'''
        super().__init__()
        self.lsf = ''
        self.lfu_cnt = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.lsf = remove_min(self.lfu_cnt)[1]
            del self.cache_data[self.lsf]
            del self.lfu_cnt[self.lsf]
            print(f"Dicard {self.lsf}")

        # Confirm key existence
        if len(self.lfu_cnt) <= BaseCaching.MAX_ITEMS:
            if key in self.lfu_cnt:
                self.lfu_cnt[key] += 1
            else:
                self.lfu_cnt.update({key: 0})
            print(self.lfu_cnt)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.lfu_cnt:
            return
        self.lfu_cnt[key] += 1
        return self.cache_data.get(key)
