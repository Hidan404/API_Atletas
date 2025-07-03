from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat
from src.api_atletas.contrib.schemas import BaseSchema


class AtletaSchema(BaseSchema):
    nome: Annotated[str, Field(min_length=3, max_length=50, description="Nome do atleta")]
    cpf: Annotated[str, Field(min_length=11, max_length=11, description="CPF do atleta")]
    idade: Annotated[int, Field(ge=0, description="Idade do atleta")]
    peso: Annotated[PositiveFloat, Field(ge=0.0, description="Peso do atleta")]
    altura: Annotated[PositiveFloat, Field(ge=0.0, description="Altura do atleta")]
    sexo: Annotated[str, Field(min_length=1, max_length=1, description="Sexo do atleta (M/F)")]