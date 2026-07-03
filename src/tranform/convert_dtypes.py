import pandas as pd

def convert_dtypes(df):
    """
    Converts the data types of columns in a DataFrame to appropriate types.

    Parameters:
        df (pd.DataFrame): The input DataFrame."""
    
    if "signup_date" in df.columns:
        print("\nConverting 'signup_date' to datetime...")
        df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")

    if "order_date" in df.columns:
        print("\nConverting 'order_date' to datetime...")
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    if "payment_date" in df.columns:
        print("\nConverting 'payment_date' to datetime...")
        df["payment_date"] = pd.to_datetime(df["payment_date"], errors="coerce")
    
    return df