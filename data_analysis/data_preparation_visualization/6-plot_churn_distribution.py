#!/usr/bin/env python3
"""
Module providing a function to plot the distribution of the Churn target.
"""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """
    Draw a bar plot of how many customers did and did not churn.

    Bars are skyblue for 'No' and salmon for 'Yes'.

    Args:
        df (pandas.DataFrame): DataFrame with a Churn column.

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    counts = df['Churn'].value_counts()
    colors = ['skyblue' if k == 'No' else 'salmon' for k in counts.index]
    plt.bar(counts.index, counts.values, color=colors)
    plt.title('Churn Distribution')
    plt.ylabel('Count')

    plt.show()
