#!/usr/bin/env python3
"""
Module providing Welch's t-tests of numeric features against Churn.
"""
from scipy import stats


def ttest_numeric(df):
    """
    Compare the mean of each numeric feature between churned and
    retained customers with Welch's t-test.

    H0: the means are equal in the Churn=Yes and Churn=No groups.
    H1: the means differ.

    Args:
        df (pandas.DataFrame): DataFrame with a Churn column.

    Returns:
        dict: {feature_name: p_value} for every numeric column.
    """
    results = {}
    yes = df[df['Churn'] == 'Yes']
    no = df[df['Churn'] == 'No']
    for col in df.select_dtypes(include='number').columns:
        t_stat, p_value = stats.ttest_ind(yes[col], no[col], equal_var=False)
        results[col] = p_value
    return results
