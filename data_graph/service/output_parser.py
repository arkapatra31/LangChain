from typing import Any, Optional
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Node(BaseModel):
    id: str
    label: str
    properties: Optional[dict]

class Relationship(BaseModel):
    sourceId: str
    targetId: str
    label: str
    properties: Optional[dict]

class Data(BaseModel):
    nodes: list[Node]
    relationships: list[Relationship]

class GraphConfiguration(BaseModel):
    data: Data


output_parser = PydanticOutputParser(pydantic_object=GraphConfiguration)

__all__ = [
    output_parser
]
