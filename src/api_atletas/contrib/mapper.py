from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy.dialects.sqlite import UUID as SQLiteUUID
from uuid import uuid4

Base = declarative_base()

class BaseModel(Base):
    id: Mapped[UUID] = mapped_column(SQLiteUUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid4)