def save_cleaned(df, output_path):
    """
    Save the cleaned DataFrame to a CSV file.

    Parameters:
    df (pandas.DataFrame): The cleaned DataFrame to be saved.
    output_path (str): The path where the CSV file will be saved.

    Returns:
    None
    """
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")