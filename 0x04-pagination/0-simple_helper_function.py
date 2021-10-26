#!/usr/bin/env python3
"""contains index_range function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns tuple with index range for given page and page size"""
    return (page * page_size - page_size, page * page_size)
