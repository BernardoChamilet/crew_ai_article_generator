from pydantic import BaseModel, Field, field_validator
from typing import Optional

# Article é uma classe que representa o artigo gerado pela crew e é usada para validação de dados
class Article(BaseModel):
    title: str = Field(..., min_length=5)
    content: str = Field(..., min_length=600)
    sources: Optional[list[str]] = None
    @field_validator('content')
    @classmethod
    def validate_number_of_words(cls, content):
        if len(content.split()) < 300:
            raise ValueError('O artigo deve ter no mínimo 300 palavras.')
        return content