#!/usr/bin/env python3
""" Task 4 - Hash Password """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ Task 4 - Salted Password """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def _generate_uuid() -> str:
    """ Task 9 - Generate a UUID """
    return str(uuid.uuid4)


class Auth:
    """ Task 5 - requires email and password """
    def __init__(self):
        """ Private instance of DB """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Task 5 - adds email and password to user data """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """ Task 8 - Verify the login is valid """
        try:
            user_info = self._db.find_user_by(email=email)
            password_bytes = password.encode("utf-8")
            return bcrypt.checkpw(password_bytes, user_info.hashed_password)
        except NoResultFound:
            return False
