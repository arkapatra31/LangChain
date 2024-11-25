import os.path
import pandas as pd
from faker import Faker
import random
from synthetic_data import generate_customers_data

fake = Faker()
def generate_customers(num_records):
    customer_df = generate_customers_data(num_records)

    # Ensure the directory exists
    directory = "../../data/customers"
    if not os.path.exists(directory):
        os.makedirs(directory)

    customer_df.to_csv(path_or_buf=f"{directory}/customers.csv", index=False)
    return customer_df