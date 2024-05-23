#!/usr/bin/env python3
""" Task 3 - Auth Class """

from flask import request
from typing import List, TypeVar


class Auth:
    """ Authorization Class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False for now """
        excluded_paths = []

        return False

    def authorization_header(self, request=None) -> str:
        """ Returns None - Requests """

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None - Requests """

        return None
