#!/usr/bin/env python3
"""module for basic redis operations"""
import redis
from typing import Union, Callable, Optional
from uuid import uuid4
from functools import wraps


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs for a method"""
    @wraps(method)
    def wrapper(self, *args) -> bytes:
        """wrapper function for call_history function"""
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        output = method(self, *args)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """decorator to increment count each time method is called"""
    @wraps(method)
    def wrapper(self, *args) -> bytes:
        """wrapper function for count_calls function"""
        self._redis.incr(method.__qualname__)
        return method(self, *args)
    return wrapper


class Cache():
    """basic redis cache"""
    def __init__(self):
        """initialization method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates key using uuid4 and stores data in Redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """gets data from redis and converts to desired format"""
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """gets data and converts data to str"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """gets data and converts data to int"""
        return self.get(key, int)
