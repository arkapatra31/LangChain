from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


class OutputParserForQuestion(BaseModel):
    question: str = Field(..., description="This is the input question")
    answer: str = Field(..., description="Here goes the answer to the question")


def getParser():
    return PydanticOutputParser(pydantic_object=OutputParserForQuestion)


__all__ = [getParser]
