from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from uuid import uuid4

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id: Mapped[UUID] = mapped_column(PostgresUUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid4)