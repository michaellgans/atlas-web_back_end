#!/usr/bin/env python3
""" Task 0 """

from base_caching import BaseCaching


class BaseCache(BaseCaching):
    """ Child class of BaseCaching """
    def __init__(self):
        """ Initializes variables """
        super().__init()

    def put(self, key, item):
        """ Puts items in the cache """
        
        
