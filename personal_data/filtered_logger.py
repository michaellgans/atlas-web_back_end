#!/usr/bin/env python3
""" Task 0 - Regex-ing """

import re
from typing import List


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
