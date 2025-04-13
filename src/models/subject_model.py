from pydantic import BaseModel, Field, field_validator

# Subject é uma classe que representa o assunto do artigo e é usada para validação de dados
class Subject(BaseModel):
    subject: str = Field(..., min_length=3, max_length=100)
    @field_validator('subject')
    @classmethod
    def clean(cls, subject):
        clean_subject = subject.strip()
        if not clean_subject:
            raise ValueError("Assunto não pode ser vazio.")
        return clean_subject