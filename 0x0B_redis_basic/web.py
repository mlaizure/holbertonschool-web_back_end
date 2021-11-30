#!/usr/bin/env python3
"""module with get_page function"""
import redis
import requests
from functools import wraps
from typing import Callable


r = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """decorator to count times a URL was accessed in the last 10 sec"""
    @wraps(method)
    def wrapper(self, *args) -> str:
        """wrapper function for count_calls function"""
        key = f'count:{args[0]}'
        r.incr(key)
        r.expire(key, 10)
        return method(*args)
    return wrapper


@count_calls
def get_page(url: str) -> str:
    """returns html content of a url"""
    res = requests.get(url)
    return res.text
