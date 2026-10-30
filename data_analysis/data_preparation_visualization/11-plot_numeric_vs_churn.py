#!/usr/bin/env python3
"""
Module providing a function to compare a numeric column across churn groups.
"""
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """
    Draw the histograms of a numeric column for churned and retained
    customers on the same axes.

    Args:
        df (pandas.DataFrame): DataFrame with a Churn column.
        col (str): the numeric column to plot.

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    groups = [df.loc[df['Churn'] == 'No', col],
              df.loc[df['Churn'] == 'Yes', col]]
    plt.hist(groups, bins=30, label=['No', 'Yes'])
    plt.title(f"{col} Distribution by Churn")
    plt.xlabel(col)
    plt.legend(title='Churn')

    plt.show()
