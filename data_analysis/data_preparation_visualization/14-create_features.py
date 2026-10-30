#!/usr/bin/env python3
"""
Module providing a function to engineer NumServices and TenureGroup.
"""
import pandas as pd


def create_features(df):
    """
    Create NumServices and TenureGroup, then drop the columns used.

    NumServices counts the services a customer subscribes to. For
    InternetService, 'DSL' and 'Fiber optic' count as subscribed.
    TenureGroup bins tenure into 0-12, 13-24, 25-48, 49-60 and 60+,
    with 0 excluded and upper bounds inclusive.

    Args:
        df (pandas.DataFrame): the pre-cleaned Telco DataFrame.

    Returns:
        pandas.DataFrame: the DataFrame with the new features.
    """
    df = df.copy()
    services = ['MultipleLines', 'OnlineSecurity', 'OnlineBackup',
                'DeviceProtection', 'TechSupport', 'StreamingTV',
                'StreamingMovies']

    has_internet = df['InternetService'].isin(['DSL', 'Fiber optic'])
    df['NumServices'] = (df[services] == 'Yes').sum(axis=1) + has_internet

    df['TenureGroup'] = pd.cut(df['tenure'],
                               bins=[0, 12, 24, 48, 60, float('inf')],
                               labels=['0-12', '13-24', '25-48', '49-60',
                                       '60+'])

    return df.drop(columns=services + ['InternetService', 'tenure'])
