from pydantic import BaseModel


class ProductDataModel(BaseModel):
    productCode: str # = Field(..., description="The product code")
    productName: str #= Field(..., description="The product name")
    productLine: str #= Field(..., description="The product line")
    productScale: str #= Field(..., description="The product scale")
    productVendor: str #= Field(..., description="The product vendor")
    productDescription: str #= Field(..., description="The product description")
    quantityInStock: int #= Field(..., description="The quantity in stock")
    buyPrice: float #= Field(..., description="The buy price")

#Export the model to be used in the main.py file
__all__ = ["ProductDataModel"]
