#!/usr/bin/env python3
"""
Module providing a function to plot a correlation heatmap.
"""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """
    Draw an annotated heatmap of the correlations between numeric columns.

    Args:
        df (pandas.DataFrame): the DataFrame to analyze.

    Returns:
        None
    """
    plt.figure(figsize=(6, 5))

    corr = df.select_dtypes(include='number').corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix')

    plt.show()
