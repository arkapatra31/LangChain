import pandas as pd
from llms import llm as openai_llm
from pandas import DataFrame


def prepare_template_schema(df: DataFrame, extract_data: str):
    df.reset_index(drop=True, inplace=True)
    # Extract columns from the DataFrame
    columns = df.columns.tolist()
    # We need to pass all the records as example values to the column in the schema
    schema = {}
    for col in columns:
        # Prepare the schema for the column
        schema[col] = {
            "data_type": str(df[col].dtype),
            "example_data": df[col].head(1).tolist() if extract_data == "Yes" else []
        }

    return schema


__all__ = [
    prepare_template_schema
]
