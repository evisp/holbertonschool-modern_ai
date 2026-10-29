#!/usr/bin/env python3
"""
Module providing a function to fix the types of two Telco columns.
"""
import pandas as pd


def convert_columns(df):
    """
    Convert TotalCharges to numbers and SeniorCitizen to Yes/No labels.

    Entries in TotalCharges that cannot be read as numbers, such as the
    blank strings in the Telco data, become NaN.

    Args:
        df (pandas.DataFrame): DataFrame with the columns TotalCharges
            and SeniorCitizen.

    Returns:
        pandas.DataFrame: the modified DataFrame.
    """
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
    return df
