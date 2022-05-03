#!/usr/bin/python3
"""
0. Basic dictionary
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    Class BasicCache that inherits from BaseCaching and is a caching systemS
    """

    def put(self, key, item):
        """
        Method that add key:value to the dictionary self.cache_data.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Method that return the value of dict self.cahce_data linked to key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
