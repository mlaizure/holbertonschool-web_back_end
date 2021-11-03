#!/usr/bin/env python3
"""
Authentication module for API
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """authentication handling"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """determines if authorization required"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] == '/':
            alt_path = path[:-1]
        else:
            alt_path = path + '/'
        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path) or fnmatch.fnmatch(
                    alt_path, excluded_path):
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
