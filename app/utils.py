import pandas as pd

def preprocess_data(df):
    # Handle negative values in key columns
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_columns] = df[numeric_columns].applymap(lambda x: max(x, 0))
    return df
