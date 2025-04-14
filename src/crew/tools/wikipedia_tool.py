from crewai.tools.base_tool import BaseTool
import requests

# WikipediaTool é uma CrewAI tool para para consultar a API da wikipedia e obter informações relevantes para os artigos
class WikipediaTool(BaseTool):
    def __init__(self):
        self.name = "Wikipedia Tool"
        self.description= "Consulta a API da Wikipedia e obtém informações relevantes sobre um tema para o artigo retornando um resumo confiável."
    def _run(self, subject: str) -> str:
        try:
            # Fazendo requisição á api do wikipedia
            url = f"https://pt.wikipedia.org/api/rest_v1/page/summary/{subject.replace(' ', '_')}" # assunto do artigo -> assunto_do_artigo
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                # 'extract' é onde o resumo se encontra. Caso não exista, retorna 'Resumo não encontrado'
                return data.get("extract", "Resumo não encontrado.")
            elif response.status_code == 404:
                # 404(not found): nenhum artgo encontrado
                return "Nenhum artigo foi encontrado na Wikipedia para esse tema."
            else:
                return f"Erro ao consultar a Wikipedia: {response.status_code}"
        except Exception as e:
            return f"Ocorreu um erro inesperado ao consultar a Wikipedia: {str(e)}"
        
# Instanciando a Wikipedia Tool
wikipedia_tool = WikipediaTool()