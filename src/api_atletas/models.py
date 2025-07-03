import sqlalchemy
from sqlalchemy.orm import Mapped
from src.api_atletas.contrib.mapper import BaseModel

#esta classe representa a tabela de atletas no banco de dados
#e herda de BaseModel, que define o id como chave primária e auto-incrementável
#as colunas são definidas com tipos e restrições apropriadas
class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    id = Mapped[sqlalchemy.Integer] = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    nome = Mapped[sqlalchemy.String(length=50)] = sqlalchemy.Column(sqlalchemy.String(length=50), nullable=False)
    cpf = Mapped[sqlalchemy.String(length=11)] = sqlalchemy.Column(sqlalchemy.String(length=11), nullable=False, unique=True)
    idade = Mapped[sqlalchemy.Integer] = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    peso = Mapped[sqlalchemy.Float] = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    altura = Mapped[sqlalchemy.Float] = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    sexo = Mapped[sqlalchemy.String(length=1)] = sqlalchemy.Column(sqlalchemy.String(length=1), nullable=False)
    data_criacao = Mapped[sqlalchemy.DateTime] = sqlalchemy.Column(
        sqlalchemy.DateTime, default=sqlalchemy.func.now(), nullable=False
    )