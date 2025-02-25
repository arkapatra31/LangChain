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
        # Drop all empty rows, NaN, and None values from the column
        df.dropna(subset=[col], inplace=True)
        # Prepare the schema for the column
        schema[col] = {
            "data_type": associate_dataType(df, col),
            "example_data": format_example_value(df, col, extract_data)
        }

    return schema

def associate_dataType(df, col):
    if str(df[col].dtype) == "int" or str(df[col].dtype) == "float" or str(df[col].dtype) == "int64" or str(df[col].dtype) == "float64":
        return "int"
    else:
        return "string"

def format_example_value(df,col, extract_data):
    column_values = str(df[col].head(5).tolist()) if extract_data == "Yes" else "[]"
    # Handle \ and ' characters in the string
    column_values = column_values.replace("\\", "").replace("'", "")
    return column_values


__all__ = [
    prepare_template_schema
]
