#!/usr/bin/python3
"""contains LFUCache class"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """puts items in LFU order into and gets items from cache, limit 4"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """puts items into cache in LRU order"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                lfu_key = min(self.order, key=self.order.get)
                print("DISCARD: {}".format(lfu_key))
                del self.cache_data[lfu_key]
                del self.order[lfu_key]
        self.cache_data[key] = item
        if key in self.order:
            self.order[key] += 1
            self.order.move_to_end(key)
        else:
            self.order[key] = 1

    def get(self, key):
        """gets item from cache and updates order to represent usage"""
        if key is None or key not in self.cache_data:
            return None
        self.order[key] += 1
        self.order.move_to_end(key)
        return self.cache_data.get(key)
