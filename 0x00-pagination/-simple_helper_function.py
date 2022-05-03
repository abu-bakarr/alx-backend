#!/usr/bin/env python3
"""
Simple Helper Function
"""


def index_range(page: int, page_size: int) -> tuple:
    """index"""
    return (page - 1) * page_size, page * page_size
