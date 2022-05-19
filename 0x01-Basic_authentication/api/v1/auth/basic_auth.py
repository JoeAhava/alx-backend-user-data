#!/usr/bin/env python3
"""
Basic Auth module
"""

from base64 import b64decode, decode
from re import split
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic Auth class
    """

    def __init__(self) -> None:
        """
        Initialize BasicAuth init
        """
        super().__init__()

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extract encoded string
        """
        if (authorization_header is None) or (
            not isinstance(authorization_header, str)) or (
                split(" ", authorization_header)[0] != 'Basic'):
            return None
        return split(" ", authorization_header)[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        decode base64
        """
        if (base64_authorization_header is None) or (
                not isinstance(base64_authorization_header, str)):
            return None
        try:
            result = b64decode(base64_authorization_header).decode('utf-8')
            print(result)
            return result
        except Exception as e:
            print(e)
            return None


if __name__ == "__main__":
    a = BasicAuth()
    print(a.decode_base64_authorization_header(None))
    print(a.decode_base64_authorization_header(89))
    print(a.decode_base64_authorization_header("Holberton School"))
    print(a.decode_base64_authorization_header("SG9sYmVydG9u"))
    print(a.decode_base64_authorization_header("SG9sYmVydG9uIFNjaG9vbA=="))
    print(a.decode_base64_authorization_header(
        a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA==")))
    print(a.extract_base64_authorization_header("Basic1234"))
