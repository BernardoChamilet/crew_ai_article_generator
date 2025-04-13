from flask import request, jsonify
import src.models.subject_model as models
from pydantic import ValidationError

# generateArticle recebe um assunto e gera um artigo com no mínimo 300 palavras sobre ele
def generateArticle():
    # Lendo requisição
    req_body = request.get_json()
    # Validando assunto do artigo
    try:
         subject = models.Subject(**req_body)
    except ValidationError as e:
        return jsonify({"erro": e.errors()}), 400
    subject = subject.model_dump()
    return jsonify(subject), 200