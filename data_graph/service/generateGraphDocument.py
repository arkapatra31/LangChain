from langchain_core.documents import Document
from langchain_experimental.graph_transformers import LLMGraphTransformer
from llms import gemini_llm, llm
from cloudLLM import groq_llm

''' Function to transform the output to graph '''
def transform_output_to_graph(input_data: str):
    try:
        # Fetch the LLM instance
        llm #= gemini_llm

        # Create the LLMGraphTransformer instance
        graph_transformer = LLMGraphTransformer(llm)

        # Convert the input data into Document
        documents = [Document(page_content=input_data)]

        # Transform the input data to graph
        graph = graph_transformer.convert_to_graph_documents(documents)
        # Ensure nodes and relationships are included
        nodes = graph[0].nodes
        relationships = graph[0].relationships
        return graph

    except Exception as e:
        print(f"Error: {e}")


__all__ = [
    transform_output_to_graph
]