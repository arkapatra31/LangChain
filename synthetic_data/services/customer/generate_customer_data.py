import os.path
import pandas as pd
from faker import Faker
import random

fake = Faker()


def generate_customers_data(num_records):
    customers = []
    for _ in range(num_records):
        country_details = fetch_country_data()
        gender = fake.random_element(elements=("Male", "Female"))
        lastName = (
            fake.last_name_male() if gender == "Male" else fake.last_name_female()
        )
        firstName = (
            fake.first_name_male() if gender == "Male" else fake.first_name_female()
        )
        customers.append(
            {
                "customerNumber": fake.unique.random_int(min=1000, max=9999),
                "customerName": firstName.capitalize() + " " + lastName.capitalize(),
                "contactLastName": lastName,
                "contactFirstName": firstName,
                "gender": gender,
                "phone": fake.phone_number(),
                "addressLine1": country_details.get(
                    "addressLine1"
                ),  # fake.street_address(),
                "addressLine2": country_details.get(
                    "addressLine2"
                ),  # fake.secondary_address(),
                "city": country_details.get("city"),  # fake.city(),
                "state": country_details.get("state"),  # fake.state(),
                "postalCode": country_details.get("postalCode"),  # fake.zipcode(),
                "country": country_details.get("country"),  # fake.country(),
                "salesRepEmployeeNumber": fake.random_int(min=1000, max=9999),
                "creditLimit": round(random.uniform(1000, 10000), 2),
                "LTV": round(random.uniform(1000, 10000), 2),
            }
        )
    fetch_country_data()
    customer_df = pd.DataFrame(customers)
    customer_df.drop_duplicates(
        subset=["customerNumber", "phone", "addressLine1"], keep="first", inplace=True
    )
    return customer_df


def fetch_country_data():
    country_details = pd.read_csv(
        "../../data/address/country_data.csv", encoding="ISO-8859-1"
    ).sample(n=1)
    return country_details.to_dict(orient="records")[0]
