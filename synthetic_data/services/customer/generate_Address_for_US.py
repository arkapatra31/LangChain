import csv
import os

# Define a list of US cities, states, and zip codes
data = [
    {"addressLine1": "123 Maple St", "addressLine2": "Apt 2", "city": "New York", "state": "NY", "postalCode": "10001",
     "country": "United States", "country": "United States"},
    {"addressLine1": "456 Oak Ave", "addressLine2": "Suite 300", "city": "Los Angeles", "state": "CA",
     "postalCode": "90001", "country": "United States"},
    {"addressLine1": "789 Pine Dr", "addressLine2": "Unit 5B", "city": "Chicago", "state": "IL", "postalCode": "60601",
     "country": "United States"},
    {"addressLine1": "321 Birch Blvd", "addressLine2": "", "city": "Houston", "state": "TX", "postalCode": "77001",
     "country": "United States"},
    {"addressLine1": "654 Elm St", "addressLine2": "Apt 4C", "city": "Phoenix", "state": "AZ", "postalCode": "85001",
     "country": "United States"},
    {"addressLine1": "987 Cedar Rd", "addressLine2": "", "city": "Philadelphia", "state": "PA", "postalCode": "19101",
     "country": "United States"},
    {"addressLine1": "159 Spruce Ln", "addressLine2": "", "city": "San Antonio", "state": "TX", "postalCode": "78201",
     "country": "United States"},
    {"addressLine1": "753 Willow Cir", "addressLine2": "Suite 10", "city": "San Diego", "state": "CA",
     "postalCode": "92101", "country": "United States"},
    {"addressLine1": "852 Palm Ave", "addressLine2": "", "city": "Dallas", "state": "TX", "postalCode": "75201",
     "country": "United States"},
    {"addressLine1": "951 Hickory St", "addressLine2": "Apt 7", "city": "San Jose", "state": "CA",
     "postalCode": "95101", "country": "United States"},
    {"addressLine1": "248 Magnolia Ct", "addressLine2": "", "city": "Austin", "state": "TX", "postalCode": "73301",
     "country": "United States"},
    {"addressLine1": "134 Redwood Dr", "addressLine2": "", "city": "Jacksonville", "state": "FL", "postalCode": "32201",
     "country": "United States"},
    {"addressLine1": "467 Sycamore St", "addressLine2": "Apt 12", "city": "San Francisco", "state": "CA",
     "postalCode": "94101", "country": "United States"},
    {"addressLine1": "679 Dogwood Ln", "addressLine2": "", "city": "Indianapolis", "state": "IN", "postalCode": "46201",
     "country": "United States"},
    {"addressLine1": "890 Poplar Ave", "addressLine2": "Suite 20", "city": "Columbus", "state": "OH",
     "postalCode": "43085", "country": "United States"},
    {"addressLine1": "907 Walnut St", "addressLine2": "", "city": "Fort Worth", "state": "TX", "postalCode": "76101",
     "country": "United States"},
    {"addressLine1": "543 Beech Dr", "addressLine2": "Unit 6A", "city": "Charlotte", "state": "NC",
     "postalCode": "28201", "country": "United States"},
    {"addressLine1": "123 Chestnut St", "addressLine2": "", "city": "Detroit", "state": "MI", "postalCode": "48201",
     "country": "United States"},
    {"addressLine1": "456 Alder Ave", "addressLine2": "", "city": "Seattle", "state": "WA", "postalCode": "98101",
     "country": "United States"},
    {"addressLine1": "789 Maple Dr", "addressLine2": "Apt 3B", "city": "Denver", "state": "CO", "postalCode": "80201",
     "country": "United States"},
    {"addressLine1": "321 Cypress Cir", "addressLine2": "", "city": "El Paso", "state": "TX", "postalCode": "79901",
     "country": "United States"},
    {"addressLine1": "654 Fir St", "addressLine2": "", "city": "Nashville", "state": "TN", "postalCode": "37201",
     "country": "United States"},
    {"addressLine1": "987 Juniper Rd", "addressLine2": "", "city": "Boston", "state": "MA", "postalCode": "02101",
     "country": "United States"},
    {"addressLine1": "159 Willow Ln", "addressLine2": "", "city": "Memphis", "state": "TN", "postalCode": "38101",
     "country": "United States"},
    {"addressLine1": "753 Birch Cir", "addressLine2": "Suite 4", "city": "Portland", "state": "OR",
     "postalCode": "97201", "country": "United States"},
    {"addressLine1": "852 Cedar Ave", "addressLine2": "", "city": "Las Vegas", "state": "NV", "postalCode": "89101",
     "country": "United States"},
    {"addressLine1": "951 Oak St", "addressLine2": "", "city": "Louisville", "state": "KY", "postalCode": "40201",
     "country": "United States"},
    {"addressLine1": "248 Maple Ct", "addressLine2": "", "city": "Baltimore", "state": "MD", "postalCode": "21201",
     "country": "United States"},
    {"addressLine1": "134 Pine Dr", "addressLine2": "", "city": "Milwaukee", "state": "WI", "postalCode": "53201",
     "country": "United States"},
    {"addressLine1": "467 Spruce St", "addressLine2": "Apt 5", "city": "Albuquerque", "state": "NM",
     "postalCode": "87101", "country": "United States"},
    {"addressLine1": "679 Redwood Ln", "addressLine2": "Unit 2C", "city": "Tucson", "state": "AZ",
     "postalCode": "85701", "country": "United States"},
    {"addressLine1": "890 Chestnut Ave", "addressLine2": "", "city": "Fresno", "state": "CA", "postalCode": "93701",
     "country": "United States"},
    {"addressLine1": "907 Oak St", "addressLine2": "", "city": "Sacramento", "state": "CA", "postalCode": "94203",
     "country": "United States"},
    {"addressLine1": "543 Alder Dr", "addressLine2": "Suite 15", "city": "Kansas City", "state": "MO",
     "postalCode": "64101", "country": "United States"},
    {"addressLine1": "123 Cedar St", "addressLine2": "", "city": "Atlanta", "state": "GA", "postalCode": "30301",
     "country": "United States"},
    {"addressLine1": "456 Maple Ave", "addressLine2": "Apt 9B", "city": "Miami", "state": "FL", "postalCode": "33101",
     "country": "United States"},
    {"addressLine1": "789 Pine Cir", "addressLine2": "", "city": "Raleigh", "state": "NC", "postalCode": "27601",
     "country": "United States"},
    {"addressLine1": "321 Spruce Dr", "addressLine2": "", "city": "Omaha", "state": "NE", "postalCode": "68101",
     "country": "United States"},
    {"addressLine1": "654 Redwood St", "addressLine2": "Unit 8", "city": "Colorado Springs", "state": "CO",
     "postalCode": "80901", "country": "United States"},
    {"addressLine1": "987 Dogwood Rd", "addressLine2": "", "city": "Minneapolis", "state": "MN", "postalCode": "55401",
     "country": "United States"},
    {"addressLine1": "159 Sycamore Ln", "addressLine2": "", "city": "Wichita", "state": "KS", "postalCode": "67201",
     "country": "United States"},
    {"addressLine1": "753 Chestnut Cir", "addressLine2": "", "city": "New Orleans", "state": "LA",
     "postalCode": "70112", "country": "United States"},
    {"addressLine1": "852 Maple Ave", "addressLine2": "", "city": "Cleveland", "state": "OH", "postalCode": "44101",
     "country": "United States"},
    {"addressLine1": "951 Oak St", "addressLine2": "Apt 7A", "city": "Tampa", "state": "FL", "postalCode": "33601",
     "country": "United States"},
    {"addressLine1": "248 Birch Blvd", "addressLine2": "", "city": "Arlington", "state": "TX", "postalCode": "76001",
     "country": "United States"},
    {"addressLine1": "134 Pine Ave", "addressLine2": "Suite 12", "city": "Bakersfield", "state": "CA",
     "postalCode": "93301", "country": "United States"},
    {"addressLine1": "467 Cedar St", "addressLine2": "", "city": "Anaheim", "state": "CA", "postalCode": "92801",
     "country": "United States"},
    {"addressLine1": "679 Spruce Ln", "addressLine2": "", "city": "Santa Ana", "state": "CA", "postalCode": "92701",
     "country": "United States"}
]


def generate_address_for_US():
    # Ensure the directory exists
    directory = "../../data/address"
    if not os.path.exists(directory):
        os.makedirs(directory)

    csv_file_path = os.path.join(directory, "country_data.csv")
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file,
                                fieldnames=["addressLine1", "addressLine2", "city", "state", "postalCode", "country"])
        writer.writeheader()
        for record in data:
            writer.writerow(record)
    file.close()

# # Save to a CSV file
# csv_file_path = "./country_data.csv"
# with open(csv_file_path, mode='a', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=["addressLine1", "addressLine2", "city", "state", "postalCode", "country"])
#     writer.writeheader()
#     for record in data:
#         writer.writerow(record)
#
# csv_file_path
