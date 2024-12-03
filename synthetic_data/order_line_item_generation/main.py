import pandas as pd
from faker import Faker
import random
import os

from synthetic_data import generate_order_line_items_details

fake = Faker()


def generate_order_line_items_data(num_records, dataframes):
    order_line_items = generate_order_line_items_details(num_records, dataframes)
    # Ensure the directory exists
    directory = "../../data/order_line_items"
    if not os.path.exists(directory):
        os.makedirs(directory)
    order_line_items.to_csv(
        path_or_buf=f"{directory}/order_line_items.csv", index=False
    )
    return order_line_items
