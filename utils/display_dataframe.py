import pandas as pd

def safe_display_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepares a DataFrame for display in Streamlit to avoid ArrowTypeError by:
    - Filling NaNs
    - Converting all columns to string
    - Ensuring index and column names are clean
    """
    df = df.copy()
    df.fillna("", inplace=True)
    df = df.astype(str)
    df.columns = df.columns.map(str)
    df.reset_index(drop=True, inplace=True)
    return df
