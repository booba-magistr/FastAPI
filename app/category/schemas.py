from pydantic import BaseModel, Field


class SchemaCategoryAdd(BaseModel):
    #  id автоматически генерируется
    name: str = Field(..., max_length=150, description='Имя категории')