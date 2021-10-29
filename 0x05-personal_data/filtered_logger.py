#!/usr/bin/env python3
"""contains filter_datum function"""
from typing import List
import re
import logging

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_logger() -> logging.Logger:
    """returns a logging.Logger object with specified configuration"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(console_handler)
    return logger


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns log message with obfuscated elements"""
    for field in fields:
        regex = f"{field}([^{separator}]*{separator})"
        message = re.sub(regex, f"{field}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filters values in log records"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
