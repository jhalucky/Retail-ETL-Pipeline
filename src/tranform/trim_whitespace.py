# from src.extract.read_csv import read_csv

def trim_whitespace(df):
    """
    Trim leading and trailing whitespace from string columns in a DF.
    """

    string_columns = df.select_dtypes(include="object").columns

    print(string_columns)

    for column in string_columns:
        df[column] = df[column].str.strip()

    print("\nTrimmed whitespace from string columns.")

    return df