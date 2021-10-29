#!/usr/bin/env python3
"""contains hash_password function"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns salted, hashed password as byte string"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
