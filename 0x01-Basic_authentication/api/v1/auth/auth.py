#!/usr/bin/env python3
'''
auth handler
'''


from typing import List, TypeVar
from flask import request


class Auth:
    '''
    Auth handler class
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        require_auth
        '''
        return False

    def authorization_header(self, request=None) -> str:
        '''
        authorization_header
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        current_user
        '''
        return None