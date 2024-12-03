import pandas as pd
from faker import Faker
import random

fake = Faker()


def generate_order_line_items_details(num_of_records, df_list):
    order_line_items = []

    # Empty Dataframe initialization
    product_df = pd.DataFrame()
    order_df = pd.DataFrame()

    # Hold the column name holding the id in product dataframe
    product_column_name = ""

    for df in df_list:
        # Read all the columns in the dataframe
        columns = df.columns

        # Iterate through the columns to find the column name holding the id in product dataframe
        for column in columns:
            column_name = column.lower()
            if "id" in column_name and "order" not in column_name:
                product_df = df
                product_column_name = column_name
            elif "ordernumber" in column_name:
                order_df = df

    for x in range(num_of_records):

        # Randomly select 1 to 4 product codes
        product_codes = (
            product_df[product_column_name].sample(random.randint(1, 4)).values
        )

        # Randomly select 1 to 4 quantities for each product code
        quantities = [
            fake.random_int(min=1, max=100) for _ in range(len(product_codes))
        ]

        order_line_items.append(
            {
                "orderNumber": order_df.iloc[x]["orderNumber"],
                "productCode": product_codes,
                "quantityOrdered": quantities,
                "priceEach": [
                    round(random.uniform(10, 1000), 2)
                    for _ in range(len(product_codes))
                ],
                "orderLineNumber": fake.random_int(min=1, max=100),
            }
        )
    return pd.DataFrame(order_line_items)
