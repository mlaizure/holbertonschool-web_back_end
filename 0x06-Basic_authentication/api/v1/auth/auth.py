#!/usr/bin/env python3
"""
Authentication module for API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """authentication handling"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """determines if authorization required"""
        if path is None or len(excluded_paths) == 0 or excluded_paths is None:
            return True
        if path[-1] == '/':
            alt_path = path[:-1]
        else:
            alt_path = path + '/'
        if path in excluded_paths or alt_path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns authorization header"""
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """returns current user"""
        return None
