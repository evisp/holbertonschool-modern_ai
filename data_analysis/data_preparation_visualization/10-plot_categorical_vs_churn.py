#!/usr/bin/env python3
"""
Module providing a function to plot the churn rate of each category.
"""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """
    Draw a bar plot of the churn rate (share of 'Yes') per category.

    Args:
        df (pandas.DataFrame): DataFrame with a Churn column.
        col (str): the categorical column to group by.

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    churn_rate = (df['Churn'] == 'Yes').groupby(df[col]).mean()
    plt.bar(churn_rate.index, churn_rate.values)
    plt.title(f"Churn Rate by {col}")
    plt.ylabel("Churn Rate")
    plt.xticks(rotation=45)

    plt.show()
