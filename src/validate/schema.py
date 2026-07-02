def validate_schema(df, expected_columns): #same schema validation function can be used for all other files schema validation checking 

    """
    Validate whether dataframe has the exact expected schema or not.
    
    """

    actual_columns = list(df.columns)

    if actual_columns == expected_columns:
        print("\nSchema Validation Passed")
        return True
    
    print("\nSchema Validation Failed")
    
    print("\nExpected Columns:")
    print(expected_columns)

    print("\nActual Columns:")
    print(actual_columns)


    return False