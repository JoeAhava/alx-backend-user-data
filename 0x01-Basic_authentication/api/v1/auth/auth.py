#!/usr/bin/env python3
'''
auth handler
'''


from operator import eq
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
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        temp_path = path
        if temp_path[-1] != '/':
            temp_path += '/'

        if temp_path in excluded_paths:
            return False
        return True

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


if __name__ == '__main__':
    a = Auth()
    print(a.require_auth(None, None))
    print(a.require_auth(None, []))
    print(a.require_auth("/api/v1/status/", []))
    print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
    print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
    print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
    print(a.require_auth("/api/v1/users",
          ["/api/v1/status/", "/api/v1/stats"]))
