from flask import Blueprint
import src.controllers.crewai_controllers as controllers

crewai_bp = Blueprint('crewai', __name__)

# Rota gerar artigo
@crewai_bp.route("/generate_article", methods=('POST',))
def gerarArtigo():
    return controllers.gerarArtigo()