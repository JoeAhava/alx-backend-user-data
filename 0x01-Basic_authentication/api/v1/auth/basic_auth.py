#!/usr/bin/env python3
"""
Basic Auth
"""

from re import split
from auth import Auth


class BasicAuth(Auth):
    """
    Basic Auth class
    """

    def __init__(self) -> None:
        super().__init__()

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extract string
        """
        if authorization_header is None or not isinstance(authorization_header, str) or split(" ", authorization_header)[0] != 'Basic':
            return None
        return split(" ", authorization_header)[1]


if __name__ == "__main__":
    a = BasicAuth()
    print(a.extract_base64_authorization_header(None))
    print(a.extract_base64_authorization_header(89))
    print(a.extract_base64_authorization_header("Holberton School"))
    print(a.extract_base64_authorization_header("Basic Holberton"))
    print(a.extract_base64_authorization_header("Basic SG9sYmVydG9u"))
    print(a.extract_base64_authorization_header(
        "Basic SG9sYmVydG9uIFNjaG9vbA=="))
    print(a.extract_base64_authorization_header("Basic1234"))
