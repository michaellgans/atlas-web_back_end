#!/usr/bin/env python3
""" Task 6 - Basic Authorization """

from api.v1.auth.auth import Auth
from api.v1.views.users import User
import base64
import binascii
from typing import TypeVar


class BasicAuth(Auth):
    """ Task 6 - Basic Authorization """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Task 7 - Base64 """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        header_snip = authorization_header[len("Basic "):]
        return header_snip

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Task 8 - Base64 Decode """
        base_header = base64_authorization_header

        if base_header is None:
            return None
        if not isinstance(base_header, str):
            return None

        try:
            decoded = base64.b64decode(base_header)
            decoded_utf8 = decoded.decode("utf-8")
            return decoded_utf8
        except binascii.Error:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Task 9 - User Credentials """
        decoded_header = decoded_base64_authorization_header

        if decoded_header is None:
            return None, None
        if not isinstance(decoded_header, str):
            return None, None
        if ":" not in decoded_header:
            return None, None

        email, password = decoded_header.split(":", 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Task 10 - User Object """
        if user_email is None:
            return None
        if not isinstance(user_email, str):
            return None
        if user_pwd is None:
            return None
        if not isinstance(user_pwd, str):
            return None

        users = User.search({"email": user_email})

        if not users:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None
