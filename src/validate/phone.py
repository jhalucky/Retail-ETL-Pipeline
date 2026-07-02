import pandas as pd

def validate_phone_numbers(df, phone_column):

    invalid_phone_number = []

    for index, phone in enumerate(df[phone_column]):

        if pd.isna(phone):
            invalid_phone_number.append(index)
            continue

        phone = str(phone)

        if len(phone) != 10:
            invalid_phone_number.append(index)
            continue

        if not phone.isdigit():
            invalid_phone_number.append(index)
            continue

    
    print("\nInvalid Phone numbers:")
    print(invalid_phone_number)


    return invalid_phone_number