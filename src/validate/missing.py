from src.config.logger import logger

def validate_missing_values(df):

    missing_values = df.isnull().sum()
    logger.info(f"\nMissing values:\n{missing_values}")

    return missing_values