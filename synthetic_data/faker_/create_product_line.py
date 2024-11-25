import pandas as pd
import random
from faker import Faker

fake = Faker()


def generate_product_lines(num_records):
    product_lines = []
    for _ in range(num_records):
        product_lines.append({
            'productLine': fake.random_element(elements=['ProductLine1', 'ProductLine2', 'ProductLine3', 'ProductLine4']),
            'textDescription': fake.text(max_nb_chars=200),
            'htmlDescription': fake.text(max_nb_chars=200),
            'imageURL': fake.image_url()
        })
    return pd.DataFrame(product_lines)


if __name__ == '__main__':
    num_records = 100
    product_line = generate_product_lines(num_records)
    product_line.to_csv(path_or_buf="../data_dir/using_faker/product_lines.csv", index=False)
    print(product_line.head())