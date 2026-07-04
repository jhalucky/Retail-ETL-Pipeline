from src.config.logger import logger
def validate_duplicate_rows(df):

    duplicate_rows = df.duplicated().sum()

    logger.info(f"\nDuplicate rows: {duplicate_rows}")

    return duplicate_rows


def validate_duplicate_primary_keys(df, primary_key_column):

    duplicate_primary_keys = df.duplicated(subset=primary_key_column).sum()

    logger.info(f"\nDuplicate primary keys: {duplicate_primary_keys}")

    return duplicate_primary_keys