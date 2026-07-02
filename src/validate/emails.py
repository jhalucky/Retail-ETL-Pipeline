import pandas as pd

def validate_emails(df, email_column):

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

    print("\nInvalid Rows:")
    print(invalid_rows)


    return invalid_rows

    