#!/usr/bin/env python3
"""
Basic authentication module for API
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """basic authentication handling"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns Base64 part of the Authorization header for basic auth"""
        if authorization_header is None or type(authorization_header) != str \
           or authorization_header[0:6] != 'Basic ':
            return None
        return authorization_header[6:]
