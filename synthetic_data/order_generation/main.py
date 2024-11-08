import pandas as pd
import os
from faker import Faker
import random
from synthetic_data import generate_orders
fake = Faker()

def generate_order_data(num_records, dataframes):
    orders = generate_orders(num_records, dataframes)
    # Ensure the directory exists
    directory = "../../data/orders"
    if not os.path.exists(directory):
        os.makedirs(directory)
    orders.to_csv(path_or_buf=f"{directory}/orders.csv", index=False)
    return orders
