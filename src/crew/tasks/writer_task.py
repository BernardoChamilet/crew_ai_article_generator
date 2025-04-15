from crewai import Task
from src.crew.agents.writers import redator

task_redator = Task(
    description=(
        "Com base nas informações fornecidas pelo agente pesquisador, escreva um artigo completo sobre o tema fornecido. "
        "O artigo deve ser informativo, bem estruturado e adequado para leitura pública. "
        "Não invente fatos. Apenas organize e redija com clareza o conteúdo entregue. "
    ),
    expected_output=(
        "Um artigo com no mínimo 300 palavras bem estruturado e com referências sobre o tema proposto"
        "Esse deve ser seu Final Answer. "
        "Retorne somente esse artigo como `Final Answer`. Nenhum outro texto deve ser incluído antes ou depois."
    ),
    agent=redator
)