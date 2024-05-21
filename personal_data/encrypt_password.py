#!/usr/bin/env python3
""" Task 5 - Encrypting Passwords """

import bcrypt


def hash_password(password: str) -> bytes:
    """ Takes in a password and returns a hashed string """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)

    return hashed


def is_valid(hash_password: bytes, password: str) -> bool:
    """ Checks if the password given matches the hashed one """
    return bcrypt.checkpw(password.encode("utf-8"), hash_password)
