from synthetic_data import llm
from langchain_core.prompts import PromptTemplate
from pandas import DataFrame
import json
from langchain import  hub


def prepare_config_map(config):

    # Create a dict with cols where columns have foreign_key == 0
    config_with_mock_fields = {key.strip(): value for key, value in config.items() if value["foreign_key"] == 0}

    faker_method_map = populate_faker_methods(config_with_mock_fields)

    for key, value in config_with_mock_fields.items():
        if key in faker_method_map.keys():
            config_with_mock_fields[key]["faker_method"] = faker_method_map[key]
        else:
            if value["data_type"] == "int" or value["data_type"] == "float" or value["data_type"] == "int64" or value["data_type"] == "float64":
                config_with_mock_fields[key]["faker_method"] = "faker.random_int"
            elif value["data_type"] == "string":
                config_with_mock_fields[key]["faker_method"] = "faker.random_string"

    # Add columns from config to the config_with_mock_fields where foreign_key == 1
    for key, value in config.items():
        if value["foreign_key"] == 1:
            config_with_mock_fields[key] = value

    return config_with_mock_fields

def populate_faker_methods(config):

    template_bkp = """
        TASK
        You are a Python expert dealing with faker data generation.
        I want you to generate the perfect faker equivalent methods for the following {config}
        
        IMPORTANT
        Always check faker documentation for the correct method before generating the faker method
        
        NEVER USE fake.unique METHOD FOR ANY COLUMN instead use methods like fake.unique.bothify
        
        NOTE
        Always check the data_type and example_data for each column and use them to generate the faker methods
        If example_data is not available, generate the faker method based on the data_type 
        but if example_data is available use the format of the example_data to generate the faker method so that the faker method will generate data in a similar pattern but not the same data
        Always use unique values for the ID columns using supported faker methods and make sure to eliminate the possibility of getting uniquesness errors like Got duplicated values after 9999999 iterations
        
        *** VERIFICATION ***
        Always verify the generated faker methods by referring to latest faker documentation, if any method is deprecated or not supported, generate the method based on the data_type
        
        OUTPUT
        Only return the faker methods. Don't include any other information or comments or explanations.
        Also return the response in a JSON format and do not enclose the response in quotes
        
    """
    template = hub.pull("arkapatra31/faker_mapping")
    # prompt_template = PromptTemplate(
    #     template=template,
    #     input_variables=[format],
    # )

    # Initialise the prompt template
    prompt_template = PromptTemplate(
        input_variables=template.input_variables,  # Variables required by the prompt
        template=template.template  # Template for the prompt
    )

    # prompt_template = PromptTemplate(
    #     input_variables=["config"],
    #     template=template_bkp
    # )

    chain = prompt_template | llm

    response = chain.invoke(
        {
            "config": config
        }
    )

    content = response.content

    # Parse content to json
    json_content = json.loads(content)
    return json_content

__all__ = [prepare_config_map]
