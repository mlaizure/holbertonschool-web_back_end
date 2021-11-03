#!/usr/bin/env python3
"""
Basic authentication module for API
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """basic authentication handling"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns Base64 part of the Authorization header for basic auth"""
        if authorization_header is None or type(authorization_header) != str \
           or authorization_header[0:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns decoded value of Base64 str base64_authorization_header"""
        if base64_authorization_header is None or \
           type(base64_authorization_header) != str:
            return None
        try:
            decoded_header = base64.b64decode(base64_authorization_header)
        except base64.binascii.Error:
            return None
        return decoded_header.decode('utf-8')
