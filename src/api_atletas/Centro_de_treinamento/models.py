from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
import sqlalchemy
from src.api_atletas.atletas.models import AtletaModel  # Adjusted to relative import

class CentroTreinamento(BaseModel):
    __tablename__ = "centros_treinamento"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True, nullable=False)
    nome: Mapped[str] = mapped_column(sqlalchemy.String(50), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(sqlalchemy.String(100), nullable=False)
    proprietario: Mapped[str] = mapped_column(sqlalchemy.String(50), nullable=False)
    atletas: Mapped["AtletaModel"] = relationship(
        "AtletaModel", back_populates="centro_treinamento", cascade="all, delete-orphan"
    )