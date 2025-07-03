from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"  # Proíbe campos extras nos dados de entrada
        from_attributes = True