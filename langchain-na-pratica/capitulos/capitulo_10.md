## Capítulo 10: Projeto Final Integrador — Assistente de Viagem Inteligente

**Neste capítulo, você vai aprender:**

* Como integrar múltiplos conceitos do LangChain em um projeto robusto.
* Construir um agente de viagem inteligente que pesquisa destinos, clima, atrações e gerencia orçamento.
* Utilizar ferramentas externas (Tavily) e customizadas no LangChain.
* Orquestrar interações com LLM, ferramentas e gerenciamento de segredos.
* Documentar comandos, troubleshooting, pontos chave e testar conhecimento.

---

### Hands-on: Exercício — Assistente de Viagem Inteligente

* **Objetivo:** Desenvolver um agente completo que auxilia no planejamento de viagens, combinando pesquisa e gerenciamento de orçamento.
* **Nome do Arquivo:** `exercicios/capitulo_09/exercicio_1/main.py`
* **Dependências:** `langchain`, `langchain-google-genai`, `langchain-tavily`, `python-dotenv`
* **Comando de Instalação:**
```sh
uv add langchain langchain-google-genai langchain-tavily python-dotenv
```
* **Configuração Adicional:** Adicione sua chave de API da Tavily ao arquivo `.env` como `TAVILY_API_KEY`.

```python
# capitulo_09/assistente_viagem.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearchResults
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool

# Carregar variáveis de ambiente
load_dotenv()

# --- Ferramentas ---

# Ferramenta de busca na internet
search_tool = TavilySearchResults(
    max_results=3,
    description="Uma ferramenta de busca para encontrar informações na internet sobre destinos de viagem, clima, atrações, etc."
)

# Ferramenta customizada para gerenciar orçamento de viagem (simulado em memória)
class OrcamentoViagem:
    def __init__(self):
        self.orcamento = {}

    @tool
    def adicionar_item_orcamento(self, item: str, custo: float) -> str:
        """
        Adiciona um item e seu custo ao orçamento de viagem.
        Útil para planejar gastos.
        Exemplo: adicionar_item_orcamento("Passagem Aérea", 1500.00)
        """
        self.orcamento[item] = self.orcamento.get(item, 0.0) + custo
        return f"Item '{item}' com custo de R${custo:.2f} adicionado ao orçamento. Orçamento atual: {self.orcamento}"

    @tool
    def ver_orcamento_total(self) -> str:
        """
        Retorna o total do orçamento de viagem e a lista de itens.
        """
        total = sum(self.orcamento.values())
        if not self.orcamento:
            return "O orçamento de viagem está vazio."
        return f"Orçamento total: R${total:.2f}. Itens: {self.orcamento}"

orcamento_viagem = OrcamentoViagem()

tools = [search_tool, orcamento_viagem.adicionar_item_orcamento, orcamento_viagem.ver_orcamento_total]

# --- LLM ---
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# --- Prompt do Agente ---
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente de planejamento de viagens. Use as ferramentas disponíveis para ajudar o usuário a planejar sua viagem, pesquisar informações e gerenciar o orçamento. Seja prestativo e informativo."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# --- Agente e Executor ---
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- Execução ---
if __name__ == "__main__":
    print("Assistente de Viagem pronto! Como posso ajudar a planejar sua próxima aventura?")

    perguntas = [
        "Qual o clima em Paris em agosto?",
        "Quais são as principais atrações turísticas em Roma?",
        "Adicione 'Passagem Aérea' com custo de 2500.00 ao orçamento.",
        "Adicione 'Hospedagem' com custo de 1200.00 ao orçamento.",
        "Qual o meu orçamento total até agora?",
        "Preciso de ideias para uma viagem de aventura na América do Sul.",
        "Qual o custo de um jantar em um restaurante médio em Tóquio?",
        "Qual o meu orçamento total?",
    ]

    for pergunta in perguntas:
        print(f"\n> Pergunta: {pergunta}")
        response = agent_executor.invoke({"input": pergunta})
        print(f"\n< Resposta Final: {response['output']}")
```

**Comando de Execução (Linux/macOS):**
```sh
chmod +x capitulo_09/execucao_exercicio_9_1.sh
./capitulo_09/execucao_exercicio_9_1.sh
```
**Comando de Execução (Windows):**
```bat
REM Execute o exercício no Windows
capitulo_09\execucao_exercicio_9_1.bat
```
**Saída Esperada (pode variar):**
```
Assistente de Viagem pronto! Como posso ajudar a planejar sua próxima aventura?
> Pergunta: Qual o clima em Paris em agosto?
< Resposta Final: ...
> Pergunta: Quais são as principais atrações turísticas em Roma?
< Resposta Final: ...
> Pergunta: Adicione 'Passagem Aérea' com custo de 2500.00 ao orçamento.
< Resposta Final: ...
> Pergunta: Adicione 'Hospedagem' com custo de 1200.00 ao orçamento.
< Resposta Final: ...
> Pergunta: Qual o meu orçamento total até agora?
< Resposta Final: ...
> Pergunta: Preciso de ideias para uma viagem de aventura na América do Sul.
< Resposta Final: ...
> Pergunta: Qual o custo de um jantar em um restaurante médio em Tóquio?
< Resposta Final: ...
> Pergunta: Qual o meu orçamento total?
< Resposta Final: ...
```
**Troubleshooting Comum:**
* `AuthenticationError` ou `TAVILY_API_KEY` não configurada: Verifique se a chave está correta no `.env`.
* `GOOGLE_API_KEY` não configurada: Verifique se está no `.env`.
* `ModuleNotFoundError`: Instale todas as dependências com `uv add`.
* Erros de conexão: Verifique sua internet e limites de API.
* Agente não usando a ferramenta: Revise as descrições das ferramentas.
* Saída inesperada: Ative `verbose=True` para inspecionar o raciocínio do agente.

---

### Pontos Chave
* Projetos integradores consolidam múltiplos conceitos do LangChain.
* Agentes com múltiplas ferramentas resolvem tarefas complexas e reais.
* LCEL facilita a composição de pipelines robustos.
* Segurança no gerenciamento de chaves de API é fundamental.

---

### Resumo do Capítulo
Neste capítulo, você aplicou todos os conceitos aprendidos para construir um Assistente de Viagem Inteligente. O projeto final demonstrou como orquestrar agentes, integrar ferramentas externas e customizadas, aplicar LCEL e gerenciar segredos de forma segura.

---

### Teste seu Conhecimento

1. Qual o principal benefício de usar múltiplas ferramentas em um agente?
   a) Reduz o custo das chamadas de API.
   b) Permite que o agente execute tarefas mais complexas e diversificadas.
   c) Aumenta a velocidade de resposta do LLM.
   d) Elimina a necessidade de um LLM.
2. No Assistente de Viagem, qual ferramenta seria usada para descobrir "Qual o clima em Paris em agosto?"
   a) adicionar_item_orcamento
   b) ver_orcamento_total
   c) search_tool
   d) Nenhuma das anteriores.
3. Por que é importante usar `load_dotenv()` e um arquivo `.env` para as chaves de API?
   a) Para tornar o código mais curto.
   b) Para melhorar a performance do agente.
   c) Para evitar que as chaves de API sejam expostas no código-fonte e versionadas.
   d) Para que o agente possa se conectar à internet.
4. Se o Assistente de Viagem não estivesse usando a ferramenta `adicionar_item_orcamento` quando solicitado, qual seria a primeira coisa a verificar?
   a) A versão do Python.
   b) A descrição da ferramenta `adicionar_item_orcamento`.
   c) A conexão com a internet.
   d) O modelo do LLM.
5. Qual o conceito central do LangChain que permite ao agente decidir dinamicamente qual ferramenta usar?
   a) Prompt Templates.
   b) Output Parsers.
   c) O loop de raciocínio (ReAct) do agente.
   d) Streaming de respostas.

**Respostas:**
1. b
2. c
3. c
4. b
5. c

---

### Projeto Hands-on: Assistente de Viagem Inteligente

Coloque em prática os conceitos do capítulo criando um projeto Python com LangChain para ser um assistente de viagem inteligente. Implemente pesquisa de destinos, clima, atrações, gerenciamento de orçamento e integração de múltiplas ferramentas. Documente todos os comandos usados, proteja suas chaves de API com .env e compartilhe o repositório via SSH no GitHub. Experimente rodar o projeto em diferentes versões do Python usando pyenv.
