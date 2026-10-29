#!/usr/bin/env python3
"""
Module providing a function to handle missing values in TotalCharges.
"""


def clean_total_charges(df, method='drop'):
    """
    Handle missing values in the TotalCharges column.

    The original DataFrame is left unchanged, so several strategies can
    be compared on the same data.

    Args:
        df (pandas.DataFrame): DataFrame with missing values in
            TotalCharges.
        method (str): 'drop' removes the rows with a missing value,
            'median' fills them with the column median, and 'impute'
            fills them with MonthlyCharges * tenure.

    Returns:
        pandas.DataFrame: the modified copy of the DataFrame.
    """
    df = df.copy()
    missing = df['TotalCharges'].isna()
    if method == 'drop':
        df = df[~missing]
    elif method == 'median':
        df.loc[missing, 'TotalCharges'] = df['TotalCharges'].median()
    elif method == 'impute':
        df.loc[missing, 'TotalCharges'] = (df.loc[missing, 'MonthlyCharges']
                                           * df.loc[missing, 'tenure'])
    return df
