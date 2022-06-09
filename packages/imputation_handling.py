#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

"""
Useful functions to handle missing values
"""

def prepare_imputation(data, cols):
    """
    Prepare data for imputation
    
    Parameters
    ----------
    data : pandas.DataFrame
        Dataframe to be prepared for imputation
    cols : list
        List of columns to be imputed

    Returns
    -------
    pandas.DataFrame
        Dataframe prepared for imputation
    """
    
    if data is None or cols is None:
        raise ValueError('data and cols must be specified')

    # replace 'unknown' with nan for features in impute_cols
    for col in cols:
        data[col] = data[col].replace('unknown', np.nan)
    
    return data