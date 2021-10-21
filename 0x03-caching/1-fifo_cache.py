#!/usr/bin/python3
"""contains FIFOCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """puts items in FIFO order into and gets items from cache, limit 4"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """puts items into cache in FIFO order"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                self.order.pop(0)
            if key in self.cache_data:
                self.order.remove(key)
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """gets item from cache"""
        if key is None or key not in self.cache_data:
            return
        return self.cache_data.get(key)
