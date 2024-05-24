#!/usr/bin/env python3
""" Task 6 - Basic Authorization """

from api.v1.auth.auth import Auth
import base64


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
