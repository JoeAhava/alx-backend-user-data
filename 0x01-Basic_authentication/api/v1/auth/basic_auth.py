#!/usr/bin/env python3
"""
Basic Auth module
"""

from base64 import b64decode, decode
from operator import contains
from re import split
from typing import Tuple
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
            # print(result)
            return result
        except Exception as e:
            # print(e)
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """Extract username
        and password
        """
        if (decoded_base64_authorization_header is None) or (
            not isinstance(
                decoded_base64_authorization_header, str)
        ) or (
            ':' not in decoded_base64_authorization_header
        ):
            return None
        return (
            split(":", decoded_base64_authorization_header)[0],
            split(":", decoded_base64_authorization_header)[1])


if __name__ == "__main__":
    a = BasicAuth()
    print(a.extract_user_credentials(None))
    print(a.extract_user_credentials(89))
    print(a.extract_user_credentials("Holberton School"))
    print(a.extract_user_credentials("Holberton:School"))
    print(a.extract_user_credentials("bob@gmail.com:toto1234"))
