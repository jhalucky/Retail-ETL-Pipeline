def validate_duplicate_rows(df):

    duplicate_rows = df.duplicated().sum()

    print("\nDuplicate rows:")
    print(duplicate_rows)

    return duplicate_rows


def validate_duplicate_primary_keys(df, primary_key_column):

    duplicate_primary_keys = df.duplicated(subset=primary_key_column).sum()

    print("\nDuplicate primary keys:")
    print(duplicate_primary_keys)

    return duplicate_primary_keys