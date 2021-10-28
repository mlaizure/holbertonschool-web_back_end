#!/usr/bin/env python3
"""contains filter_datum function"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns log message with obfuscated elements"""
    for field in fields:
        regex = f"{field}([^{separator}]*{separator})"
        message = re.sub(regex, f"{field}={redaction}{separator}", message)
    return message
