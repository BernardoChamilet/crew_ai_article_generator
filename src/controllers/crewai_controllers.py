from flask import request, jsonify
import src.models.subject_model as models
from src.models.article_model import Article
from pydantic import ValidationError
from src.crew.crew import artigo_crew

# generateArticle recebe um assunto e gera um artigo com no mínimo 300 palavras sobre ele
def generateArticle():
    # Lendo requisição
    req_body = request.get_json()
    # Validando assunto do artigo
    try:
        subject = models.Subject(**req_body)
    except ValidationError as e:
        return jsonify({"erro": e.errors()}), 400
    # Executando a crew 
    try:
        crew_output = artigo_crew.kickoff(inputs={"subject": subject.subject})
    except Exception as e:
        return jsonify({"erro": f"Erro ao gerar o artigo: {str(e)}"}), 500
    # Validando output da crew
    try:
        output_dict = {
            "article": crew_output.tasks_output[-1].raw
        }
        response = Article(**output_dict)
        response_dict = response.model_dump()
    except ValidationError as e:
        return jsonify({"erro": e.errors()}), 400
    # 200: sucesso
    return jsonify(response_dict), 200