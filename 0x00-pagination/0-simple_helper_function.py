#!/usr/bin/env python3
""" Simple helper function """


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    begin_page = (page - 1) * page_size
    range_page = begin_page + page_size
    return (begin_page, range_page)