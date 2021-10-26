#!/usr/bin/env python3
"""conatins Server class and index_range function"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns tuple with index range for given page and page size"""
    return (page * page_size - page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """fetches indexes from a given page"""
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        idx = index_range(page, page_size)
        self.dataset()
        return self.__dataset[idx[0]:idx[1]]
