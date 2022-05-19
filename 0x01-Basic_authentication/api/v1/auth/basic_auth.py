#!/usr/bin/env python3
"""
Basic Auth module
"""

from base64 import b64decode, decode
import email
from operator import contains
from re import split
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


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
            return (None, None)
        return (
            split(":", decoded_base64_authorization_header)[0],
            split(":", decoded_base64_authorization_header)[1])

    def user_object_from_credentials(
            self,
            user_email: str, user_pwd: str) -> TypeVar('User'):
        """get user
        """
        # print(f"uemail: {user_email}, pwd: {user_pwd}")
        if (
            user_email is None
        ) or (
            not isinstance(user_email, str)
        ) or (
            not isinstance(user_pwd, str)
        ) or (
                user_pwd is None):
            return None
        user_db = User()
        results = user_db.search(attributes={
            'email': user_email,
        })
        if len(results) > 0:
            user = results[0]
            if user.is_valid_password(user_pwd):
                return user
            else:
                return None
        return None


if __name__ == "__main__":
    """ Create a user test """
    print("basic_auth")
