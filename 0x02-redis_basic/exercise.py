#!/usr/bin/env python3
"""Basic Redis"""

from functools import wraps
import redis
from typing import Callable, Optional, Union
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """Return number of times the cache methods are called"""
    @wraps(method)
    def count_wrapper(*args, **kwargs):
        """Count wrapper"""
        key = method.__qualname__
        func = method(*args, **kwargs)
        # self._redis.incr(key)
        args[0]._redis.incr(key)
        # return self._redis.get(key)
        return func
    return count_wrapper


def call_history(method: Callable) -> Callable:
    """Store history of inputs and outputs for a particular function"""
    @wraps(method)
    def history_wrapper(*args, **kwargs):
        """History Wrapper"""
        key = method.__qualname__
        wrapped_func = method(*args, **kwargs)
        inputs = args[0]._redis.rpush("{}:inputs".format(key), str(args[1:]))
        outputs = args[0]._redis.rpush(
            "{}:outputs".format(key), str(wrapped_func))
        return wrapped_func
    return history_wrapper


class Cache():
    """Cache class"""

    def __init__(self) -> None:
        """Inititalize redis cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method to store data"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float]:
        """Get method that calls a function on a key_value"""
        if not self._redis.get(key):
            return None

        if not fn:
            return self._redis.get(key)

        return fn(self._redis.get(key))

    def get_str(self, key: str) -> str:
        """return string_parametrized data"""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Return int-parametrized data"""
        return self.get(key, int)
