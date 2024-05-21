#!/usr/bin/env python3
""" Task 0 - Regex-ing """

import re
import logging
from typing import List

# To be redacted
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str], redaction: str,
        message: str, separator: str) -> str:
    """
    Returns data obfuscated based on Regex Filtering

    Args
    - fields: what to redact
    - redaction: what to redact the characters with
    - message: the origional string before redaction
    - separator: what to separate the strings with
     """
    for item in fields:
        reg_match = fr'({item}=)([^;{separator}]+)'
        message = re.sub(reg_match, fr'\1{redaction}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter Class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initializes Varaibles """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Redacts specific fields """
        og_mess = super().format(record)
        redacted_message = filter_datum(
            self.fields, self.REDACTION, og_mess, self.SEPARATOR)
        return redacted_message


def get_logger() -> logging.Logger:
    """ Sets up Logging system at INFO level only """
    logger = logging.getLogger("user_data")

    # Setting Logger Level
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = RedactingFormatter(fields=[PII_FIELDS])
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
