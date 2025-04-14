from crewai.crew import Crew
from src.crew.tasks.researcher_task import task_pesquisador
from src.crew.tasks.writer_task import task_redator

# Criando a Crew
artigo_crew = Crew(
    agents=[task_pesquisador.agent, task_redator.agent],
    tasks=[task_pesquisador, task_redator],
    verbose=True
)