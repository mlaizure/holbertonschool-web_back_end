#!/usr/bin/env python3
"""contains zoom_array function"""
from typing import List, Tuple, Iterator


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """returns zoomed tuple as list"""
    zoomed_in: Iterator = (
        item for item in lst
        for i in range(factor)
    )
    return list(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
