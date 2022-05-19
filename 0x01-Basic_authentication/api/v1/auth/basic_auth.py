#!/usr/bin/env python3
"""
Basic Auth
"""

from api.v1.auth.auth import Auth


class Basic_Auth(Auth):
    """
    Basic Auth class
    """

    def __init__(self) -> None:
        super().__init__()
