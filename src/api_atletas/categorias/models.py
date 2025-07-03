from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
import sqlalchemy

from api_atletas.atletas.models import AtletaModel



class CategoriaModel(BaseModel):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    atletas: Mapped["AtletaModel"] = relationship("AtletaModel", back_populates="categoria")
    data_criacao: Mapped[sqlalchemy.DateTime] = mapped_column(
        sqlalchemy.DateTime, default=sqlalchemy.func.now(), nullable=False
    )