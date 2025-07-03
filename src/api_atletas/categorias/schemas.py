from src.api_atletas.contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import Field


class CategoriaSchema(BaseSchema):
    id: Annotated[int, Field(ge=1, description="ID da categoria")]
    nome: Annotated[str, Field(min_length=3, max_length=50, description="Nome da categoria")]
    