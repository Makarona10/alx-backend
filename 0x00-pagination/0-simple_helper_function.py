#!/usr/bin/env python3

'''0x00. Pagination'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    return ((page - 1) * page_size, page * page_size)
