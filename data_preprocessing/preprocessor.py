import pandas as pd
import numpy as np
from scipy import stats

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes a pandas DataFrame as input, checks for null values in each column,
    and decides to fill the null values based on the data type of the column and skewness.

    Args:
    df (pd.DataFrame): The input DataFrame to be processed.

    Returns:
    pd.DataFrame: The modified DataFrame with null values handled.

    """
    for col in df.columns:
        if df[col].isnull().any():
            
            # Categorical column
            if df[col].dtype in [np.object_, np.str_]:
                mode_val = df[col].mode().iloc[0]
                df[col] = df[col].fillna(mode_val)
            
            # Numerical column    
            else:
                # calculating skewness
                skewness = stats.skew(df[col].dropna())

                # Determine the fill value based on skewness
                if abs(skewness) > 1:  # If skewness is greater than 1, consider it skewed
                    fill_value = df[col].median()
                else:
                    fill_value = df[col].mean()

                df[col] = df[col].fillna(fill_value)

    return df
