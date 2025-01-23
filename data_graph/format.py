import pandas as pd

# Read all files in the data folder and append to a single dataframe
filePath = "./data"

df1 = pd.read_csv(f"{filePath}/Car Owners.csv")


prompt = """
You are a data scientist who is excellent in identifying data and linking them.

INPUT
I have a 5 different CSV data attached
{csv1}
{csv2}
{csv3}
{csv4}
{csv5}

TASK
I want you to analyze the data, find the possible link within each CSV and identify the probable nodes with the ID and relationship by analyzing the presence of foreign keys.
Finally I want to create a Neo4J Graph using the CSV so you will return only the complete cypher query which when executed in Neo4j Browser will  create the complete graph. Don't include any explanations or metadata.
Always create the nodes first and then define the relationships
"""