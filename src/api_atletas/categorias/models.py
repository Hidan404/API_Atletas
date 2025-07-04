from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
import sqlalchemy

from src.api_atletas.atletas.models import AtletaModel



class CategoriaModel(BaseModel):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    atletas: Mapped["AtletaModel"] = relationship("AtletaModel", back_populates="categoria")
    