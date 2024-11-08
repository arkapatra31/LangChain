import pandas as pd
from faker import Faker
import random

fake = Faker()

# Generate synthetic data for Customers
def generate_customers(num_records):
    customers = []
    for _ in range(num_records):
        customers.append({
            'customerNumber': fake.unique.random_int(min=1000, max=9999),
            'customerName': fake.company(),
            'contactLastName': fake.last_name(),
            'contactFirstName': fake.first_name(),
            'phone': fake.phone_number(),
            'addressLine1': fake.street_address(),
            'addressLine2': fake.secondary_address(),
            'city': fake.city(),
            'state': fake.state(),
            'postalCode': fake.zipcode(),
            'country': fake.country(),
            'salesRepEmployeeNumber': fake.random_int(min=1000, max=9999),
            'creditLimit': round(random.uniform(1000, 10000), 2),
            'LTV': round(random.uniform(1000, 10000), 2)
        })
    return pd.DataFrame(customers)

# Generate synthetic data for OrderDetails
def generate_order_details(num_records):
    order_details = []
    for _ in range(num_records):
        order_details.append({
            'orderNumber': fake.random_int(min=1000, max=9999),
            'productCode': fake.unique.random_int(min=1000, max=9999),
            'quantityOrdered': fake.random_int(min=1, max=100),
            'priceEach': round(random.uniform(10, 1000), 2),
            'orderLineNumber': fake.random_int(min=1, max=10)
        })
    return pd.DataFrame(order_details)

# Generate synthetic data for Orders
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
            'customerNumber': fake.random_int(min=1000, max=9999)
        })
    return pd.DataFrame(orders)

# Generate synthetic data for Products
def generate_products(num_records):
    products = []
    for _ in range(num_records):
        products.append({
            'productCode': fake.unique.random_int(min=1000, max=9999),
            'productName': fake.word(),
            'productLine': fake.word(),
            'productScale': fake.random_element(elements=('1:10', '1:12', '1:18')),
            'productVendor': fake.company(),
            'productDescription': fake.text(max_nb_chars=200),
            'quantityInStock': fake.random_int(min=1, max=1000),
            'buyPrice': round(random.uniform(10, 1000), 2)
        })
    return pd.DataFrame(products)

# Generate synthetic data for ProductLines
def generate_product_lines(num_records):
    product_lines = []
    for _ in range(num_records):
        product_lines.append({
            'productLine': fake.unique.word(),
            'textDescription': fake.text(max_nb_chars=200),
            'htmlDescription': fake.text(max_nb_chars=200),
            'imageURL': fake.image_url()
        })
    return pd.DataFrame(product_lines)

# Example usage
customers_df = generate_customers(100)
#customers_df.to_csv('../data_dir/using_faker/customers.csv', index=False)
order_details_df = generate_order_details(100)
orders_df = generate_orders(100)
products_df = generate_products(100)
product_lines_df = generate_product_lines(100)

# Combine the dataframes into a single dataframe
combined_df = pd.concat([customers_df, order_details_df, orders_df, products_df, product_lines_df], axis=1)

#Save the combined dataframe to a CSV file
combined_df.to_csv('../data_dir/using_faker/combined_data.csv', index=False)

print(combined_df.head())