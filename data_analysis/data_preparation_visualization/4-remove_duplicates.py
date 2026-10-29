#!/usr/bin/env python3
"""
Module providing a function to remove duplicate rows from a DataFrame.
"""


def remove_duplicates(df):
    """
    Drop every duplicate row, keeping the first occurrence.

    Args:
        df (pandas.DataFrame): the DataFrame to process.

    Returns:
        pandas.DataFrame: the deduplicated DataFrame.
    """
    return df.drop_duplicates()
