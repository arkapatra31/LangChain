import pandas as pd
from faker import Faker
import random

fake = Faker()
def generate_orders(num_records):
    orders = []
    for _ in range(num_records):
        orders.append({
            'orderNumber': fake.unique.random_int(min=1000, max=9999),
            'orderDate': fake.date(),
            'requiredDate': fake.date(),
            'shippedDate': fake.date(),
            'status': fake.random_element(elements=('Shipped', 'Pending', 'Cancelled')),
            'comments': fake.text(max_nb_chars=200),
            'customerNumber': pd.read_csv('../data_dir/using_faker/customers.csv')['customerNumber'].sample().values[0]
        })
    return pd.DataFrame(orders)

if __name__ == '__main__':
    num_records = 100
    orders = generate_orders(num_records)
    orders.to_csv(path_or_buf="../data_dir/using_faker/orders.csv", index=False)
    print(orders.head())