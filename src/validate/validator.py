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


def validate_duplicate_primary_keys(df, primary_key_columns):
    """Validate for duplicate primary keys in the DataFrame."""
    
    duplicate_primary_keys = df.duplicated(subset=primary_key_columns).sum()

    print("\nDuplicate primary keys:")
    print(duplicate_primary_keys)

    return duplicate_primary_keys