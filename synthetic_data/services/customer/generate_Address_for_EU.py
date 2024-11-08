import os
from faker import Faker
import pandas as pd
import csv
import random

# Sample data for European countries with correct state/city/postalCode
countries_data = {
    "Germany": {
        "states": ["Bavaria", "Berlin", "Hamburg", "Hesse", "Saxony"],
        "cities": ["Munich", "Berlin", "Hamburg", "Frankfurt", "Leipzig"],
        "postal_codes": ["80331", "10115", "20095", "60311", "04103"]
    },
    "France": {
        "states": ["Île-de-France", "Provence-Alpes-Côte d'Azur", "Auvergne-Rhône-Alpes", "Occitanie",
                   "Nouvelle-Aquitaine"],
        "cities": ["Paris", "Marseille", "Lyon", "Toulouse", "Bordeaux"],
        "postal_codes": ["75000", "13000", "69000", "31000", "33000"]
    },
    "Italy": {
        "states": ["Lazio", "Lombardy", "Campania", "Veneto", "Piedmont"],
        "cities": ["Rome", "Milan", "Naples", "Venice", "Turin"],
        "postal_codes": ["00100", "20100", "80100", "30100", "10100"]
    },
    "Spain": {
        "states": ["Madrid", "Catalonia", "Andalusia", "Valencia", "Galicia"],
        "cities": ["Madrid", "Barcelona", "Seville", "Valencia", "A Coruña"],
        "postal_codes": ["28001", "08001", "41001", "46001", "15001"]
    },
    "Netherlands": {
        "states": ["North Holland", "South Holland", "Utrecht", "Gelderland", "Limburg"],
        "cities": ["Amsterdam", "Rotterdam", "Utrecht", "Arnhem", "Maastricht"],
        "postal_codes": ["1012", "3011", "3511", "6811", "6211"]
    }
}


# Random address generator function
def generate_address():
    country = random.choice(list(countries_data.keys()))
    state = random.choice(countries_data[country]["states"])
    city = random.choice(countries_data[country]["cities"])
    postal_code = random.choice(countries_data[country]["postal_codes"])
    address_line1 = f"{random.randint(1, 999)} {random.choice(['Main St', 'High St', 'Oak St', 'Park Ave', 'Maple Ave'])}"
    address_line2 = f"Apt {random.randint(1, 50)}"

    return [address_line1, address_line2, city, state, postal_code, country]


def generate_address_for_EU():
    # Generate 50 records
    records = [generate_address() for _ in range(50)]

    # Ensure the directory exists
    directory = "../../data/address"
    if not os.path.exists(directory):
        os.makedirs(directory)

    csv_file_path = os.path.join(directory, "country_data.csv")
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["addressLine1", "addressLine2", "city", "state", "postalCode", "country"])
        writer.writerows(records)
    file.close()

# # Generate 50 records
# records = [generate_address() for _ in range(50)]
#
# # Writing to CSV
# csv_file_path = './country_data.csv'
# with open(csv_file_path, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["addressLine1", "addressLine2", "city", "state", "postalCode", "country"])
#     writer.writerows(records)
