#!/usr/bin/python3
"""
3. LRU Caching
"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    Class LRUCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        method initializer/constructor
        """
        super().__init__()
        self.Queue = list()

    def put(self, key, item):
        """
        Method that add key:value to the dictionary self.cache_data
        """
        if key and item:
            # print(self.Queue)
            if key in self.cache_data:
                self.cache_data[key] = item
                self.Queue.remove(key)
                self.Queue.append(key)
            else:
                if (len(self.cache_data) == self.MAX_ITEMS):
                    print("DISCARD: {}".format(self.Queue[0]))
                    del self.cache_data[self.Queue[0]]
                    del self.Queue[0]
                self.Queue.append(key)
                self.cache_data[key] = item

    def get(self, key):
        """
        Method that return the value of dict self.cahce_data linked to key
        """
        if key and key in self.cache_data:
            self.Queue.remove(key)
            self.Queue.append(key)
            return self.cache_data[key]
        return None
