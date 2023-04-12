#!/usr/bin/env python3
"""Basic Redis"""

import redis
from typing import Callable, Optional, Union
from uuid import uuid4


class Cache():
    """Cache class"""

    def __init__(self) -> None:
        """Inititalize redis cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
