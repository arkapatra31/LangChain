from dotenv import load_dotenv
import os
from data_graph.service.generateGraphDocument import transform_output_to_graph
from langchain_neo4j import Neo4jGraph

# Load the environment variables
load_dotenv()

# Create the Neo4jGraph instance
graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USER"),
    password=os.getenv("NEO4J_PASSWORD"),
    refresh_schema=False
)

def neo4j_graph(configuration: str):
    try:
        """ Fetch the graph data from graph transformer"""
        graph_data = transform_output_to_graph(configuration)

        """ Store the graph data in Neo4j """
        graph.add_graph_documents(graph_data)
        return graph_data

    except Exception as e:
        print(f"Error: {e}")


__all__ = [
    neo4j_graph
]
