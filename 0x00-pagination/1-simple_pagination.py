#!/usr/bin/env python3

'''0x00. Pagination'''

from typing import Tuple
import csv
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int]:
    '''return a tuple of size two containing a start index and an end index'''
    return ((page - 1) * page_size, page * page_size)


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
        '''gets the pages of the intended data'''
        assert type(page) is int and page > 0 and type(page_size) \
            is int and page_size > 0
        data_set = self.dataset()
        range = index_range(page, page_size)
        if (len(data_set) <= (page - 1) * page_size):
            return []
        return list(data_set[range[0]: range[1]])
