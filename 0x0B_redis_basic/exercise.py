#!/usr/bin/env python3
""" Task 0 - Writing Strings to Redis """

import redis
import uuid
from typing import Union


class Cache():
    """ Redis Client Class """
    def __init__(self):
        """ Creates Redis Client as private variable """
        self._redis = redis.Redis()
        self._redis.ping()
        self._redis.flushdb()

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
