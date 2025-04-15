# CrewAI Article Generator

Sistema multiagente feito com CrewAI e Flask para automatizar a criação de artigos

## Estrutura do sistema
* Config: inicialização de variáveis de ambiente
* Controllers: funções das rotas. Recebem a requisição, interagem com outros módulos e enviam a resposta
* Crew: códigos referentes ao uso da biblioteca CrewAI
  * Agents: definição dos agentes
  * LLM: configuração da(s) llm(s)
  * Tasks: criação das tarefas
  * Tools: criação das ferramentas
* Models: modelos criados com pydantic para validação e formatação de dados
* Routes: definição das rotas da api (nome, método http e função)

## Siga os passos abaixo para clonar e executar o projeto localmente:
* 1. Clone o repositório
```
git clone https://github.com/BernardoChamilet/crew_ai_article_generator
cd crew_ai_article_generator
```
* 2. Crie um ambiente virtual (opcional)
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
* 3. Instale as dependências
```
pip install -r requirements.txt
```
* 4. Crie um .env na raiz do projeto contendo
```
SECRET_KEY=sua_chave_secreta
PORT=5000
GROQ_API_KEY=sua_chave_da_groq
DEBUG=True/False
```
* 5. Na raiz do projeto rode
```
python main.py
```