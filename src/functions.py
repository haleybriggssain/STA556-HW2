import pandas as pd
import numpy as np
from pathlib import Path


def clean_columns(data: pd.DataFrame) -> pd.DataFrame:
    """Get rid of spaces in the column names
    
    Parameters
    ---
    data: DataFrame
        dataset
    
    Returns
    ---
    dataframe
        dataframe of dataset with no spaces in the columns
            
    """
    data_copy = data.copy()
    data_copy.columns = data_copy.columns.str.replace(' ', '')
    return data


def filter_languages(data: pd.DataFrame, column:str, category:str) -> int:
    """ Sum the number of languages with certain categorical characteristics

    Parameters
    ---
    data: DataFrame
        dataset
    column: str
        column to be filtered
    category: str
        group (from the column) included in the filter
    
    Returns
    ---
    int
        number of languages in the category/group

    """
    return len(data.loc[data[column] == category])


def avg_speakers(data: str) -> int:
    """Calculate the average number of speakers in an entire dataset

    Parameters
    ---
    data
        dataset

    Returns
    ---
    dataframe
        average number of speakers
        
    """
    return data["Speakers"].sum() / len(data)