#!/usr/bin/env python3
"""
Module providing a function to standardize the charge columns.
"""
from sklearn import preprocessing


def scale_numeric(df):
    """
    Standardize MonthlyCharges and TotalCharges to mean 0 and std 1.

    Args:
        df (pandas.DataFrame): DataFrame with MonthlyCharges and
            TotalCharges columns.

    Returns:
        pandas.DataFrame: the DataFrame with the two columns scaled.
    """
    df = df.copy()
    cols = ['MonthlyCharges', 'TotalCharges']
    scaler = preprocessing.StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])
    return df
