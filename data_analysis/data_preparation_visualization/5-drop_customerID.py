#!/usr/bin/env python3
"""
Module providing a function to drop the customerID column.
"""


def drop_customerID(df):
    """
    Remove the customerID column, a unique identifier with no
    predictive value.

    Args:
        df (pandas.DataFrame): DataFrame containing a customerID column.

    Returns:
        pandas.DataFrame: the DataFrame without customerID.
    """
    return df.drop(columns=['customerID'])
