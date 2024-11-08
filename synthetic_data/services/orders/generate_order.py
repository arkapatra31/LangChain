import pandas as pd
from faker import Faker
import random
fake = Faker()

def generate_orders(num_records, df_list):
    orders = []

    # Empty Dataframe initialization
    product_df = pd.DataFrame()
    customer_df = pd.DataFrame()

    # Hold the column name holding the id in product dataframe
    product_column_name = ''

    for df in df_list:
        # Read the first column name of the dataframe
        column_name = df.columns[0].lower()
        if 'id' in column_name and 'customer' not in column_name:
            product_df = df
            product_column_name = column_name
        elif 'customernumber' in column_name:
            customer_df = df



    for _ in range(num_records):
        orders.append({
            'orderNumber': fake.unique.random_int(min=1000, max=9999),
            'orderDate': fake.date(),
            'productID': product_df[product_column_name].sample(random.randint(1,4)).values,
            'customerNumber': customer_df['customerNumber'].sample().values[0],
            'requiredDate': fake.date(),
            'shippedDate': fake.date(),
            'status': fake.random_element(elements=('Shipped', 'Pending', 'Cancelled')),
            'comments': fake.text(max_nb_chars=200)
        })
    return pd.DataFrame(orders)