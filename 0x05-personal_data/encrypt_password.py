#!/usr/bin/env python3
"""contains hash_password and is_valid functions"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns salted, hashed password as byte string"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validates the provided password matches the hashed password"""
    return bcrypt.checkpw(password.encode(), hashed_password)
