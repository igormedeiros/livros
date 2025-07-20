## **Capítulo 10: Projeto Final Integrador: Assistente de Viagem Inteligente**

### **Visão Geral do Projeto**

O Assistente de Viagem será um agente que utiliza:
*   Um LLM (Gemini 2.5 Flash) como seu cérebro de raciocínio.
*   Uma ferramenta de busca na internet (Tavily) para obter informações atualizadas sobre destinos, clima, atrações, etc.
*   Ferramentas customizadas para adicionar itens a um orçamento de viagem e consultar o total.
*   A arquitetura de agentes do LangChain (`create_tool_calling_agent` e `AgentExecutor`) para orquestrar as interações.

### **Exercício Prático: Assistente de Viagem Inteligente**

*   **Objetivo:** Desenvolver um agente completo que auxilia no planejamento de viagens, combinando pesquisa e gerenciamento de orçamento.
*   **Nome do Arquivo:** `exercicios/capitulo_09/exercicio_1/main.py`
*   **Dependências:** `langchain`, `langchain-google-genai`, `langchain-tavily`, `python-dotenv`
*   **Comando de Instalação:** `uv add langchain langchain-google-genai langchain-tavily python-dotenv`
*   **Configuração Adicional:** Você precisará de uma chave de API da Tavily. Você pode obter uma gratuitamente em [tavily.com](https://tavily.com/). Adicione-a ao seu arquivo `.env` como `TAVILY_API_KEY`.

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
        return f"Item '{item}' com custo de R${costo:.2f} adicionado ao orçamento. Orçamento atual: {self.orcamento}"

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

**Comando de Execução:**

```sh
```sh
chmod +x capitulo_09/execucao_exercicio_9_1.sh
./capitulo_09/execucao_exercicio_9_1.sh
```
```

**Saída Esperada (pode variar ligeiramente):**

```text
Assistente de Viagem pronto! Como posso ajudar a planejar sua próxima aventura?

> Pergunta: Qual o clima em Paris em agosto?
... (saída verbose do agente) ...
< Resposta Final: Em agosto, o clima em Paris é geralmente quente e ensolarado, com temperaturas médias variando de 16°C a 25°C. É um dos meses mais quentes do ano, ideal para atividades ao ar livre.

> Pergunta: Quais são as principais atrações turísticas em Roma?
... (saída verbose do agente) ...
< Resposta Final: As principais atrações turísticas em Roma incluem o Coliseu, o Fórum Romano, o Panteão, a Fontana di Trevi, a Praça de São Pedro e os Museus do Vaticano, que abrigam a Capela Sistina.

> Pergunta: Adicione 'Passagem Aérea' com custo de 2500.00 ao orçamento.
... (saída verbose do agente) ...
< Resposta Final: Item 'Passagem Aérea' com custo de R$2500.00 adicionado ao orçamento. Orçamento atual: {'Passagem Aérea': 2500.0}

> Pergunta: Adicione 'Hospedagem' com custo de 1200.00 ao orçamento.
... (saída verbose do agente) ...
< Resposta Final: Item 'Hospedagem' com custo de R$1200.00 adicionado ao orçamento. Orçamento atual: {'Passagem Aérea': 2500.0, 'Hospedagem': 1200.0}

> Pergunta: Qual o meu orçamento total até agora?
... (saída verbose do agente) ...
< Resposta Final: Orçamento total: R$3700.00. Itens: {'Passagem Aérea': 2500.0, 'Hospedagem': 1200.0}

> Pergunta: Preciso de ideias para uma viagem de aventura na América do Sul.
... (saída verbose do agente) ...
< Resposta Final: Para uma viagem de aventura na América do Sul, você pode considerar destinos como a Patagônia (Argentina/Chile) para trekking e paisagens deslumbrantes, a Amazônia (Brasil/Peru/Equador) para ecoturismo e vida selvagem, ou a Bolívia para explorar o Salar de Uyuni e a cultura andina.

> Pergunta: Qual o custo de um jantar em um restaurante médio em Tóquio?
... (saída verbose do agente) ...
< Resposta Final: O custo de um jantar em um restaurante médio em Tóquio pode variar bastante, mas geralmente fica entre 2.000 a 5.000 ienes por pessoa, o que equivale a aproximadamente R$70 a R$175, dependendo da cotação atual.

> Pergunta: Qual o meu orçamento total?
... (saída verbose do agente) ...
< Resposta Final: Orçamento total: R$3700.00. Itens: {'Passagem Aérea': 2500.0, 'Hospedagem': 1200.0}
```

**Troubleshooting Comum:**

*   **`AuthenticationError` ou `TAVILY_API_KEY` não configurada:** Certifique-se de que você obteve sua `TAVILY_API_KEY` do Tavily e a adicionou corretamente ao seu arquivo `.env` na raiz do projeto.
*   **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Verifique se sua `GOOGLE_API_KEY` está corretamente configurada no arquivo `.env`.
*   **`ModuleNotFoundError`:** Verifique se todas as dependências (`langchain`, `langchain-google-genai`, `langchain-tavily`, `python-dotenv`) foram instaladas corretamente usando `uv add` ou `pip install`.
*   **Erros de Conexão:** Problemas de rede ou limites de taxa da API (Tavily ou Google Gemini) podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.
*   **Agente não usando a ferramenta:** Se o agente não estiver chamando as ferramentas quando esperado, revise as `description` das ferramentas. Elas devem ser claras e concisas, indicando exatamente o que a ferramenta faz e quando deve ser usada. O LLM usa essa descrição para decidir se a ferramenta é relevante para a tarefa.
*   **Saída Inesperada do Agente:** Se a resposta final do agente não for a esperada, ative `verbose=True` no `AgentExecutor` para inspecionar o processo de raciocínio do LLM e as chamadas de ferramentas. Isso ajudará a identificar onde o fluxo está se desviando.

### Resumo do Capítulo

Neste capítulo, você aplicou todos os conceitos aprendidos ao longo do livro para construir um Assistente de Viagem Inteligente. Este projeto final demonstrou como:

*   **Orquestrar Agentes:** Utilizar o LLM como um motor de raciocínio para tomar decisões dinâmicas.
*   **Integrar Múltiplas Ferramentas:** Capacitar o agente a interagir com o mundo externo através de ferramentas de busca e ferramentas customizadas para gerenciamento de dados.
*   **Aplicar LCEL:** Compor um pipeline complexo de forma elegante e eficiente.
*   **Gerenciar Segredos:** Manter as chaves de API seguras usando variáveis de ambiente.

Este projeto é um exemplo claro do poder do LangChain para construir aplicações de IA que resolvem problemas reais, combinando diferentes capacidades para criar soluções inteligentes e autônomas.

### **Pontos Chave**
*   Projetos integradores são a melhor forma de consolidar o aprendizado de múltiplos conceitos.
*   Agentes com ferramentas são poderosos para interagir com o mundo real e dados externos.
*   A LCEL facilita a construção de pipelines complexos e legíveis.
*   A segurança no gerenciamento de chaves de API é fundamental em qualquer aplicação.

### **Teste seu Conhecimento**

1. Qual o principal benefício de usar múltiplas ferramentas em um agente, como demonstrado no Assistente de Viagem?
   a) Reduz o custo das chamadas de API.
   b) Permite que o agente execute tarefas mais complexas e diversificadas.
   c) Aumenta a velocidade de resposta do LLM.
   d) Elimina a necessidade de um LLM.
2. No projeto do Assistente de Viagem, qual ferramenta seria usada para descobrir "Qual o clima em Paris em agosto?"
   a) `adicionar_item_orcamento`
   b) `ver_orcamento_total`
   c) `search_tool`
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

*(Respostas: 1-b, 2-c, 3-c, 4-b, 5-c)*
