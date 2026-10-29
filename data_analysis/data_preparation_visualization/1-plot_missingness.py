#!/usr/bin/env python3
"""
Module providing a function to visualize missing values in a DataFrame.
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """
    Plot the position of every missing value in a DataFrame.

    Each missing value is drawn as a vertical bar, with the row index
    on the x-axis and the column name on the y-axis.

    Args:
        df (pandas.DataFrame): the DataFrame to analyze.

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    rows, cols = np.where(df.isnull())
    plt.scatter(rows, cols, marker='|')
    plt.yticks(range(len(df.columns)), df.columns)
    plt.title("Missingness Plot")

    plt.tight_layout()
    plt.show()
