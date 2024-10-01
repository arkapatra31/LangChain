from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


class OutputParserForQuestion(BaseModel):
    question: str = Field(..., description="This is the input question")
    answer: str = Field(..., description="Here goes the answer to the question")
    facts: List[str] = Field(..., description="Occupation Details")

    # def get_parser(self):
    #     return {
    #         "question": self.question,
    #         "answer": self.answer,
    #         "facts": self.facts
    #     }


output_parser = PydanticOutputParser(pydantic_object=OutputParserForQuestion)

__all__ = [output_parser]
