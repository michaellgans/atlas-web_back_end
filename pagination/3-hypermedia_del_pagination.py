#!/usr/bin/env python3
""" Task 3 - Deletion-resilient hypermedia pagination """

import csv
import math
from typing import List, Dict


class Server:
    """ Server class to paginate a database of popular baby names. """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """ Dataset indexed by sorting position, starting at 0 """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Returns data even when indexes are deleted """
        assert type(index) is int and type(page_size) is int
        assert index > 0 and page_size > 0
        assert index < len(self.indexed_dataset())

        # Results can be different than just start and end
        # Because in this version, entries may be deleted
        data = self.indexed_dataset()
        new_data = []
        next_index = index

        # Run through the entries and add them to the data set
        # Only if they're in the data set
        for item in range(page_size):
            while next_index not in data:
                next_index += 1
            new_data.append(data[next_index])
            next_index += 1

        data_dict = {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": new_data
        }

        return data_dict
