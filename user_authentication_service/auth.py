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
    return str(uuid.uuid4())


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

    def create_session(self, email: str) -> str:
        """ Task 10 - Gets the session ID """
        try:
            user_info = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user_info.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """ Task 11 - Gets the user from Session ID """
        if session_id is None:
            return None
        try:
            user_info = self._db.find_user_by(session_id=session_id)
            return user_info
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Task 13 - stops the current session """
        try:
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ Task 16 - Helps reset Password """
        try:
            user_info = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        reset_token = _generate_uuid()
        self._db.update_user(user_info.id, reset_token=reset_token)
        return reset_token
