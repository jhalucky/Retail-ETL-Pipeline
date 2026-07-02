import pandas as pd

def read_csv(file_path):
    """
    Reads a CSV file and returns pandas DataFrame.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:    
        pd.DataFrame: DataFrame containing the data from the CSV file.

    """

    df = pd.read_csv(file_path)
    return df
    