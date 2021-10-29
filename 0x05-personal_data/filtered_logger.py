#!/usr/bin/env python3
"""contains filter_datum function"""
from typing import List
import re
import logging
import os
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_db() -> mysql.connector.connection.MySQLConnection:
    """gets credentials from db and returns connection"""
    user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db = os.getenv('PERSONAL_DATA_DB_NAME')
    cnx = mysql.connector.connect(user=user,
                                  password=password,
                                  host=host,
                                  database=db)
    return cnx


def get_logger() -> logging.Logger:
    """returns a logging.Logger object with specified configuration"""
    logger = logging.getLogger('user_data')
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


def main():
    """connect to database, get and display all rows in the users table"""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    db_logger = get_logger()
    for user_dict in cursor:
        log_message = ''
        for k, v in user_dict.items():
            log_message += k + '=' + str(v) + '; '
        log_message = log_message[:-1]
        log_record = logging.LogRecord('user_data', logging.INFO, None, None,
                                       log_message, None, None)
        db_logger.handle(log_record)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
