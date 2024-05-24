#!/usr/bin/env python3
""" Task 6 - Basic Authorization """

from api.v1.auth.auth import Auth


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
