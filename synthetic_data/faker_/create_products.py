import random
import pandas as pd
from faker import Faker
fake = Faker()



def generate_products(num_records):
    products = []
    for _ in range(num_records):
        products.append({
            'productCode': fake.unique.random_int(min=100, max=9999),
            'productName':  fake.word(),
            'productLine': pd.read_csv('../data_dir/using_faker/product_lines.csv')['productLine'].sample().values[0],
            'productScale': fake.random_element(elements=('1:10', '1:12', '1:18')),
            'productVendor': fake.company(),
            'productDescription': fake.text(max_nb_chars=200),
            'quantityInStock': fake.random_int(min=1, max=1000),
            'buyPrice': round(random.uniform(10, 1000), 2)
        })
    return pd.DataFrame(products)

if __name__ == '__main__':
    num_records = 100
    products = generate_products(num_records)
    products.to_csv(path_or_buf="../data_dir/using_faker/products.csv", index=False)
    print(products.head())