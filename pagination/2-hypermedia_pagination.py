#!/usr/bin/env python3
""" Task 2 - Hypermedia Pagination """

import csv
import math
from typing import List, Tuple, Union, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """ Creates a helper function to know what index series to show """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size

    return (start_index, end_index)


class Server:
    """ Server class to paginate a database of popular baby names. """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Gets the data for a specific page """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        data_start, data_end = index_range(page, page_size)
        data_length = len(self.dataset())

        if data_start >= data_length:
            return []

        return self.dataset()[data_start:data_end]
        print("Dataset:", self.dataset())

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, List[List]]]:
        """ Returns a Dictionary with Mulitple Entries """
        data_dict = {}
        data_dict["page_size"] = 1
        data_dict["page"] = 2
        data_dict["data"] = self.get_page(page, page_size)
        data_dict["next_page"] = 3
        data_dict["prev_page"] = 4
        data_dict["total_page"] = 5
        return data_dict
