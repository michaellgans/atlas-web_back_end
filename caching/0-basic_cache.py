#!/usr/bin/env python3
""" Task 0 """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Child class of BaseCaching """

    def __init__(self):
        """ Initializes variables """
        super().__init__()
        self.cache = self.cache_data

    def put(self, key, item):
        """ Puts items in the cache """
        if key is None or item is None:
            pass
        self.cache[key] = item

    def get(self, key):
        """ Fetches items in the cache """
        if key is None:
            return None

        if key not in self.cache:
            return None
        else:
            return self.cache.get(key)
