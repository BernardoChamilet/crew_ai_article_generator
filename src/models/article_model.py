from pydantic import BaseModel, field_validator

# Article é uma classe que representa o artigo gerado pela crew e é usada para validação de dados
class Article(BaseModel):
    article: str 
    @field_validator('article')
    @classmethod
    def validate_number_of_words(cls, article):
        if len(article.split()) < 300:
            raise ValueError('O artigo deve ter no mínimo 300 palavras.')
        return article