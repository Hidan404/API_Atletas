import sqlalchemy


class AtletaModel(sqlalchemy.Model):
    __tablename__ = "atletas"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    nome = sqlalchemy.Column(sqlalchemy.String(length=50), nullable=False)
    cpf = sqlalchemy.Column(sqlalchemy.String(length=11), nullable=False, unique=True)
    idade = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    peso = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    altura = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    sexo = sqlalchemy.Column(sqlalchemy.String(length=1), nullable=False)