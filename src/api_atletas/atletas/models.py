import sqlalchemy
from sqlalchemy.orm import Mapped, relationship, mapped_column
from src.api_atletas.contrib.mapper import BaseModel
from src.api_atletas.categorias.models import CategoriaModel  # Importa CategoriaModel

#esta classe representa a tabela de atletas no banco de dados
#e herda de BaseModel, que define o id como chave primária e auto-incrementável
#as colunas são definidas com tipos e restrições apropriadas
class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    nome: Mapped[str] = mapped_column(sqlalchemy.String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(sqlalchemy.String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(nullable=False)
    peso: Mapped[float] = mapped_column(nullable=False)
    altura: Mapped[float] = mapped_column(nullable=False)
    sexo: Mapped[str] = mapped_column(sqlalchemy.String(1), nullable=False)
    data_criacao: Mapped[sqlalchemy.DateTime] = mapped_column(
        sqlalchemy.DateTime, default=sqlalchemy.func.now(), nullable=False
    )
    categoria: Mapped["CategoriaModel"] = relationship( back_populates="atletas")
    categoria_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey("categorias.id"), nullable=False)
    centro_treinamento: Mapped["CTModel"] = relationship(
        back_populates="atletas", uselist=False, cascade="all, delete-orphan"
    )
    centro_treinamento_id: Mapped[int] = mapped_column(
        sqlalchemy.ForeignKey("centros_treinamento.id"), nullable=True
    )