#!/usr/bin/env python3
"""
Module providing chi-square independence tests against the Churn target.
"""
import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """
    Test whether each categorical feature is independent of Churn.

    Args:
        df (pandas.DataFrame): DataFrame with Churn and categorical columns.

    Returns:
        dict: {feature_name: p_value} for every categorical column except
            Churn.
    """
    results = {}
    for col in df.select_dtypes(include='object').columns:
        if col == 'Churn':
            continue
        table = pd.crosstab(df[col], df['Churn'])
        chi2, p_value, dof, expected = stats.chi2_contingency(table)
        results[col] = p_value
    return results
