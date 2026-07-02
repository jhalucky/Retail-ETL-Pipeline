def validate_missing_values(df):

    missing_values = df.isnull().sum()

    print("\nMissing Vlaues:")
    print(missing_values)

    return missing_values