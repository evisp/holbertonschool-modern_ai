#!/usr/bin/env python3
"""
Module providing a function to split the data into train and test sets.
"""
from sklearn import model_selection


def split_data(df, target='Churn', test_size=0.2, random_state=42):
    """
    Split features and target into stratified train and test sets.

    Args:
        df (pandas.DataFrame): the DataFrame to split.
        target (str): name of the target column.
        test_size (float): proportion of rows in the test set.
        random_state (int): seed for a reproducible split.

    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    X = df.drop(columns=[target])
    y = df[target]
    return model_selection.train_test_split(X, y, test_size=test_size,
                                            random_state=random_state,
                                            stratify=y)
