#!/usr/bin/env python3
""" Task 0 - Writing Strings to Redis """

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Counts how many times Cache has been called

    Arguments:
     - method: what it's counting

    Returns:
     - Number of calls
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper Function """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Stores input and output when store is called

    Arguments:
     - method: What it's targetting

    Returns:
     - Input/Output
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Function Wrapper """
        input = f"{method.__qualname__}:inputs"
        output = f"{method.__qualname__}:outputs"
        self._redis.rpush(input, str(args))

        result = method(self, *args, **kwargs)
        self._redis.rpush(output, str(result))
        return result
    return wrapper


class Cache():
    """ Redis Client Class """
    def __init__(self):
        """ Creates Redis Client as private variable """
        self._redis = redis.Redis()
        self._redis.ping()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates Random UUID Key

        Arguments:
         - data: input data from Redis

        Returns:
         - UUID and data stored
        """
        data_id = str(uuid.uuid4())
        self._redis.set(data_id, data)

        return data_id

    def get(self, key: str, fn: Union[None, callable] = None) ->\
            Union[str, bytes, int, float]:
        """
        Returns data to origional format

        Arguments:
         - key: UUID key from store
         - func: optional

        Returns:
         - Data from Redis
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """
        Parameterizes with correct conversion

        Arguments:
         - data: data stored in Redis

        Returns:
         - Str version of bytes
        """
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """
        Parameterizes with correct conversion

        Arguments:
         - data: data stored in Redis

        Returns:
         - Int version of bytes
        """
        return int.from_bytes(data, byteorder="big")


def replay(method: Callable) -> None:
    """ Replays the inputs and outputs of a method """
    redis_instance = method.__self__._redis
    stored_inputs = f"{method.__qualname__}:inputs"
    stored_outputs = f"{method.__qualname__}:outputs"

    inputs = redis_instance.lrange(stored_inputs, 0, -1)
    outputs = redis_instance.lrange(stored_outputs, 0, -1)

    call_count = len(inputs)
    print(f"{method.__qualname__} was called {call_count} times:")

    for input_data, output_data in zip(inputs, outputs):
        in_data = input_data.decode("utf-8")
        out_data = output_data.decode("utf-8")
        print(f"{method.__qualname__}(*{in_data}) -> {out_data}")
