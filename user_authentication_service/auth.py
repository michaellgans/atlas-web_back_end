#!/usr/bin/env python3
""" Task 4 - Hash Password """

import bcrypt


def _hash_password(password: str) -> bytes:
    """ Task 4 - Salted Password """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
