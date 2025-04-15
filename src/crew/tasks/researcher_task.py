from crewai import Task
from src.crew.agents.researcher import pesquisador

task_pesquisador = Task(
    description=(
        "Pesquise sobre o tema {subject} utilizando sua ferramenta Wikipedia Tool. "
        "Use diretamente a string {subject} como input da ferramenta. "
        "Atenção: a ferramenta espera um texto simples como input, sem estruturas JSON."
        "Seu objetivo é coletar informações confiáveis e relevantes que sirvam de base para a redação de um artigo. "
        "Apresente os dados de forma clara, estruturada e objetiva, com no máximo 800 palavras. "
        "Após receber o resumo da ferramenta Wikipedia Tool, finalize a tarefa retornando esse conteúdo com 'Final Answer: ...'. "
        "Evite repetir o uso da ferramenta se a resposta já foi obtida. "
        "Atenção: O conteúdo deve ser resumido e conter no máximo 800 palavras, focando nos pontos mais importantes do tema."
    ),
    expected_output=(
        "Um resumo informativo com cerca de 800 palavras com os principais pontos sobre {subject}. "
        "Evite copiar diretamente trechos longos da fonte. Prefira uma síntese bem escrita, com coesão e clareza. "
        "Esse resumo será usado na próxima etapa"
    ),
    agent=pesquisador
)