def validate_missing_values(df):
    """Validate for missing values in the DataFrame."""

    missing_values = df.isnull().sum()

    print("\nMissing values:")
    print(missing_values)

    return missing_values