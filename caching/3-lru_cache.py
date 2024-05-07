#!/usr/bin/env python3
""" Task 3 - LRU Caching
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Child class of BaseCaching """
    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.cache = self.cache_data

    def put(self, key, item):
        """ Puts items in the cache """
        if key is None or item is None:
            return None

        self.cache[key] = item

        if len(self.cache) > BaseCaching.MAX_ITEMS:
            LRU_entry = next(iter(self.cache))
            print(f"DISCARD: {LRU_entry}")
            del self.cache[LRU_entry]

    def get(self, key):
        """ Fetches items in the cache """
        if key is None:
            return None

        if key not in self.cache:
            return None
        else:
            value = self.cache.get(key)
            del self.cache[key]
            self.cache[key] = value
            return self.cache.get(key)
