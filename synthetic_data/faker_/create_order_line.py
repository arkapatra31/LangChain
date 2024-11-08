import pandas as pd
from faker import Faker
import random

fake = Faker()
def generate_order_line(num_records):
    order_line = []
    for _ in range(num_records):
        order_line.append({
            'orderNumber': pd.read_csv('../data_dir/using_faker/orders.csv')['orderNumber'].sample().values[0],
            'productCode': pd.read_csv('../data_dir/using_faker/products.csv')['productCode'].sample().values[0],
            'quantityOrdered': fake.random_int(min=1, max=100),
            'priceEach': round(random.uniform(10, 1000), 2),
            'orderLineNumber': fake.random_int(min=1, max=100)
        })
    return pd.DataFrame(order_line)

if __name__ == '__main__':
    num_records = 100
    order_line = generate_order_line(num_records)
    order_line.to_csv(path_or_buf="../data_dir/using_faker/order_lines.csv", index=False)
    print(order_line.head())