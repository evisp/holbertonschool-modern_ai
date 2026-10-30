#!/usr/bin/env python3
"""
Module providing a function to encode the Telco features for modeling.
"""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """
    Encode the target and the categorical features as numbers.

    Churn uses a LabelEncoder, the binary Yes/No columns an
    OrdinalEncoder, Contract and PaymentMethod one-hot encoding with the
    first category dropped, and TenureGroup an OrdinalEncoder in
    alphabetical order.

    Args:
        df (pandas.DataFrame): the DataFrame to encode.

    Returns:
        tuple: the encoded DataFrame, the fitted LabelEncoder for Churn,
            the fitted OrdinalEncoder for the binary columns and the
            fitted OrdinalEncoder for TenureGroup.
    """
    df = df.copy()

    label_encoder = preprocessing.LabelEncoder()
    df['Churn'] = label_encoder.fit_transform(df['Churn'])

    binary_cols = ['Partner', 'Dependents', 'PaperlessBilling',
                   'SeniorCitizen']
    binary_encoder = preprocessing.OrdinalEncoder()
    df[binary_cols] = binary_encoder.fit_transform(df[binary_cols])

    df = pd.get_dummies(df, columns=['Contract', 'PaymentMethod'],
                        drop_first=True)

    tenure_encoder = preprocessing.OrdinalEncoder()
    df['TenureGroup'] = tenure_encoder.fit_transform(df[['TenureGroup']])

    return df, label_encoder, binary_encoder, tenure_encoder
