from crewai import Task
from src.crew.agents.writers import redator

task_redator = Task(
    description=(
        "Com base nas informações fornecidas pelo agente pesquisador, escreva um artigo completo sobre o tema solicitado. "
        "O artigo deve ser informativo, bem estruturado e adequado para leitura pública. "
        "Não invente fatos. Apenas organize e redija com clareza o conteúdo entregue."
    ),
    expected_output=(
        "Um JSON com os seguintes campos:\n"
        "- 'titulo': título do artigo\n"
        "- 'conteudo': corpo do artigo com no mínimo 300 palavras\n"
        "- 'referencias': lista de fontes utilizadas, se possível\n\n"
        "Exemplo de estrutura:\n"
        "{\n"
        "  \"titulo\": \"Título do artigo\",\n"
        "  \"conteudo\": \"Texto com no mínimo 300 palavras...\",\n"
        "  \"referencias\": [\"https://pt.wikipedia.org/wiki/Exemplo\"]\n"
        "}"
    ),
    agent=redator
)