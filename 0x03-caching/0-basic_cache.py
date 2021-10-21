#!/usr/bin/python3
"""contains BasicCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """puts items into cache and gets items from cache, no limit"""

    def put(self, key, item):
        """puts item in cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """gets item from cache"""
        if key is None or key not in self.cache_data:
            return
        return self.cache_data.get(key)
