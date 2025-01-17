from langchain_core.prompts import PromptTemplate
from pandas import DataFrame
from synthetic_data import llm
import pandas as pd


def get_prompt():
    # Define the prompt template for generating records based on the example data
    template = """
    I want to generate {number} csv records for the following columns:
    {columns}
    The data type for each column is as follows:
    {data_types}
    The example data for each column is as follows:
    {example_data}
    Always include description for each record which is a unique string and the length of the description should be between 100 and 200.
    Don't include example data in the generated records but understand and learn from the example data.
    Only return the content of the generated records and also don't use comma in values.
    Also make sure that the generated records belongs to or are associated to {flavour}.
    """
    prompt_template = PromptTemplate(
        template=template,
        input_variables=["number", "columns", "data_types", "example_data", "flavour"],
    )
    return prompt_template


def read_dataframe_and_generate_data(domain, config, number_of_records, flavour, reference_dataframe: DataFrame):
    #try:
    # Strip all spaces from config keys
    config = {key.strip(): value for key, value in config.items()}

    # Fetch the prompt template based on the presence of reference data
    prompt_template = get_prompt()

    chain = prompt_template | llm

    # Extract the input details from the configuration
    columns = [col for col in config.keys() if config[col]["foreign_key"] == 0]
    data_types = {col: config[col]["data_type"] for col in columns}
    example_data = {col: config[col]["example_data"] for col in columns}

    # Prepare data for Chain Invocation based on the presence of reference data
    input_data = {
        "number": number_of_records,
        "columns": columns,
        "data_types": data_types,
        "example_data": example_data,
        "flavour": flavour
    }

    # Invoke the chain with the input details
    response = chain.invoke(
        input_data
    )

    content = response.content

    data = [row.split(",") for row in content.split("\n") if row]
    sanitized_data = [idv_data for idv_data in data if len(idv_data) == len(columns)]
    df = pd.DataFrame(sanitized_data, columns=columns)
    df.dropna(inplace=True)
    df.drop(df.index[[0]], inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.to_csv("data.csv", index=False)

    if reference_dataframe.empty:
        return df
    else:
        return manage_foreign_key_data(df, config, reference_dataframe)

    # except Exception as e:
    #     print(f"An error occurred while generating the data: {e}")
    #     return pd.DataFrame()


def manage_foreign_key_data(df, config, reference_dataframe):
    # Fetch the columns along with the datatype from the config where foreign_key == 1
    foreign_key_columns = [col for col in config.keys() if config[col]["foreign_key"] == 1]

    # Pick the columns of the reference dataframe which are present in the foreign key columns
    ref_df: DataFrame = reference_dataframe[foreign_key_columns]

    # Drop duplicate columns from the reference DataFrame
    ref_df = ref_df.loc[:, ~ref_df.columns.duplicated()]

    # Set ref_df size to be equal to the generated DataFrame
    ref_df = ref_df.sample(n=len(df), random_state=42, replace=True)

    # Replace the NaN values in the columns via sampling from the column
    for col in ref_df.columns:
        ref_df[col] = ref_df[col].dropna().sample(n=len(ref_df), replace=True).values

    # Ensure the reference DataFrame index is unique
    ref_df.reset_index(drop=True, inplace=True)

    # Merge the reference DataFrame with the generated DataFrame
    df = pd.concat([df, ref_df], axis=1)

    return df


__all__ = [read_dataframe_and_generate_data]
