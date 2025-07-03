import sqlalchemy
from src.api_atletas.contrib.mapper import BaseModel

#esta classe representa a tabela de atletas no banco de dados
#e herda de BaseModel, que define o id como chave primária e auto-incrementável
#as colunas são definidas com tipos e restrições apropriadas
class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    nome = sqlalchemy.Column(sqlalchemy.String(length=50), nullable=False)
    cpf = sqlalchemy.Column(sqlalchemy.String(length=11), nullable=False, unique=True)
    idade = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    peso = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    altura = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    sexo = sqlalchemy.Column(sqlalchemy.String(length=1), nullable=False)