from src.api_atletas.contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import Field


class CT(BaseSchema):
    id: Annotated[int, Field(ge=1, description="ID do centro de treinamento")]
    nome: Annotated[str, Field(min_length=3, max_length=50, description="Nome do centro de treinamento")]
    endereco: Annotated[str, Field(min_length=3, max_length=100, description="Endereço do centro de treinamento")]
    telefone: Annotated[str, Field(min_length=10, max_length=15, description="Telefone do centro de treinamento")]
    