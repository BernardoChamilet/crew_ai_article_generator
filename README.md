# CrewAI Article Generator

Sistema multiagente feito com CrewAI e Flask para automatizar a criação de artigos

## Estrutura do sistema
* Config: inicialização de variáveis de ambiente
* Controllers: funções das rotas. Recebem a requisição, interagem com outros módulos e enviam a resposta
* Crew: códigos referentes ao uso da biblioteca CrewAI
  * Agents: definição dos agentes
  * Tasks: criação das tarefas
  * Tools: criação das ferramentas
  * LLM: configuração da(s) llm(s)
* Models: modelos criados com pydantic para validação e formatação de dados
* Routes: definição das rotas da api (nome, método http e função)