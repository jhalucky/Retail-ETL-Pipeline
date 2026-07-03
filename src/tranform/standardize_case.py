def standardize_case(df):

    """
    Standardizes the case of all string columns, convert their first letter to Uppercase in a DataFrame.

    Parameters:
        df (pd.DataFrame): The input DataFrame."""
    
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.title()

        print("\nStandardized case for column:")

    return df