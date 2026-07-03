def phone(df):

    """
    Transforms the phone number column in the DataFrame to a standard format.

    Parameters:
        df (pd.DataFrame): The input DataFrame containing the phone number column. """
    
    if "phone" in df.columns:
        df["phone"] = df["phone"].astype(str).str.replace(r'\D', '', regex=True)  # Remove non-digit characters
        df["phone"] = df["phone"].str.zfill(10)  # Pad with leading zeros to ensure 10 digits

    return df