from crewai import Task
from src.crew.agents.researcher import pesquisador

task_pesquisador = Task(
    description=(
        "Pesquise o tema fornecido utilizando sua ferramenta de consulta à Wikipedia. "
        "Seu objetivo é coletar informações confiáveis e relevantes que sirvam de base para a redação de um artigo. "
        "Apresente os dados de forma clara, estruturada e objetiva."
    ),
    expected_output=(
        "Um resumo informativo com os principais pontos sobre o tema fornecido. "
        "Evite copiar diretamente trechos longos da fonte. Prefira uma síntese bem escrita, com coesão e clareza."
    ),
    agent=pesquisador
)