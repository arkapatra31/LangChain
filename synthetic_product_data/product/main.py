import json

from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_experimental.tabular_synthetic_data.openai import (
    OPENAI_TEMPLATE,
    create_openai_data_generator,
)
from langchain_experimental.tabular_synthetic_data.prompts import (
    SYNTHETIC_FEW_SHOT_PREFIX,
    SYNTHETIC_FEW_SHOT_SUFFIX,
)
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from synthetic_data.data_model.products import ProductDataModel
from dotenv import load_dotenv

load_dotenv()


class ProductDataModel(BaseModel):
    productCode: str  # = Field(..., description="The product code")
    productName: str  # = Field(..., description="The product name")
    productLine: str  # = Field(..., description="The product line")
    productScale: str  # = Field(..., description="The product scale")
    productVendor: str  # = Field(..., description="The product vendor")
    productDescription: str  # = Field(..., description="The product description")
    quantityInStock: int  # = Field(..., description="The quantity in stock")
    buyPrice: float  # = Field(..., description="The buy price")


examples = [
    {
        "example": """
        'productCode': [9691], 'productName': ["Mamaearth-Onion-Growth-Control-Redensyl"],
        'productLine': ["Hair Oil"], 'productScale': ["01:18"],
        'productVendor': ["Mamaearth" ], 'productDescription': ["Mamaearth Redensyl Hairoil"],
        'quantityInStock': [232], 'buyPrice': [554.12]
        """
    },
    {
        "example": """
        'productCode': [3078], 'productName': ["Godrej-Protekt-Master-Blaster-Handwash"],
        'productLine': ["Health & Hygeine"], 'productScale': ["01:07"],
        'productVendor': ["Godrej", ], 'productDescription': ["Godrej handwash"],
        'quantityInStock': [171], 'buyPrice': [105.98]
        """
    },
    {
        "example": """
        'productCode': [9091], 'productName': ["Mamaearth-Natural-Turmeric-Saffron-brightning"],
        'productLine': ["Body Wash"], 'productScale': ["01:10"],
        'productVendor': ["Mamaearth", ], 'productDescription': ["Mamaearth Bodywash"],
        'quantityInStock': [100], 'buyPrice': [299.56]
        """
    },
]

OPENAI_TEMPLATE = PromptTemplate(input_variables=["example"], template="{example}")

prompt_template = FewShotPromptTemplate(
    prefix=SYNTHETIC_FEW_SHOT_PREFIX,
    examples=examples,
    suffix=SYNTHETIC_FEW_SHOT_SUFFIX,
    input_variables=["subject", "extra"],
    example_prompt=OPENAI_TEMPLATE,
)

synthetic_data_generator = create_openai_data_generator(
    output_schema=ProductDataModel,
    llm=ChatOpenAI(
        temperature=1, model="gpt-4o-mini", verbose=True
    ),  # You'll need to replace with your actual Language Model instance
    prompt=prompt_template,
)

synthetic_results = synthetic_data_generator.generate(
    subject="ProductData",
    extra="the name must be chosen at random. Make it something you wouldn't normally choose.",
    runs=50,
)

if __name__ == "__main__":
    with open("synthetic-product.json", "w+") as f:
        for result in synthetic_results:
            f.write(result.json())
            f.write("\n")
    # for result in synthetic_results:
    #     print(result)
