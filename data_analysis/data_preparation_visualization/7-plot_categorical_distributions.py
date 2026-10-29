#!/usr/bin/env python3
"""
Module providing a function to plot the distribution of categorical columns.
"""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    Draw one bar plot of value counts per categorical column, in a grid.

    Args:
        df (pandas.DataFrame): the DataFrame to plot.
        columns_to_plot (list): categorical columns to plot. Defaults to
            every column of dtype object except the target Churn.

    Returns:
        None
    """
    if columns_to_plot is None:
        columns_to_plot = [col for col in df.select_dtypes(include='object')
                           if col != 'Churn']

    n_cols = 3
    n_rows = (len(columns_to_plot) + n_cols - 1) // n_cols
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
    axes = axes.flatten()

    for ax, col in zip(axes, columns_to_plot):
        counts = df[col].value_counts()
        ax.bar(counts.index, counts.values)
        ax.set_title(col)
        ax.tick_params(axis='x', rotation=45)

    for ax in axes[len(columns_to_plot):]:
        fig.delaxes(ax)

    plt.tight_layout()
    plt.show()
