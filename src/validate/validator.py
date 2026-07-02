def validate_missing_values(df):
    """Validate for missing values in the DataFrame."""

    missing_values = df.isnull().sum()

    print("\nMissing values:")
    print(missing_values)

    return missing_values



def validate_duplicate_rows(df):
    """Validate for duplicate rows in the DataFrame."""
    
    duplicate_rows = df.duplicated().sum()

    print("\nDuplicate rows:")
    print(duplicate_rows)

    return duplicate_rows