import pandas as pd

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


def validate_duplicate_primary_keys(df, primary_key_column):
    """Validate for duplicate primary keys in the DataFrame."""
    
    duplicate_primary_keys = df.duplicated(subset=primary_key_column).sum()

    print("\nDuplicate primary keys:")
    print(duplicate_primary_keys)

    return duplicate_primary_keys

def validate_emails(df, email_column):

    """Validate email addresses in the DF."""

    invalid_rows = []

    for index, email in enumerate(df[email_column]):
        if pd.isna(email):
            invalid_rows.append(index)
            continue

        if "@" not in email:
            invalid_rows.append(index)
            continue

        username, domain = email.split("@", 1)

        if username == "" or domain == "":
            invalid_rows.append(index)
            continue

        if "." not in domain:
            invalid_rows.append(index)
            continue

    print("\nInvalid email addresses:")
    print(invalid_rows)

    return invalid_rows