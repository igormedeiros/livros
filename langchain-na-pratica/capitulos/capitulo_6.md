## Capítulo 6: Ferramentas e Agentes: Capacitando LLMs com Ações

**Neste capítulo, você vai aprender:**

* Como equipar LLMs com ferramentas externas para criar agentes autônomos e interativos.
* Diferenças entre ferramentas (Tools) e agentes (Agents) no LangChain.
* Implementação prática de agentes com ferramentas customizadas, APIs externas e integração via LangGraph.
* Exercícios práticos de análise de vendas e cotação de moedas, com instruções de execução, troubleshooting e dicas de modularização.
* Pontos chave, checklist e projeto hands-on para consolidar o aprendizado sobre agentes e ferramentas.

---

Neste capítulo, exploraremos um dos conceitos mais poderosos do LangChain: a capacidade de equipar Large Language Models (LLMs) com ferramentas externas, transformando-os em agentes autônomos capazes de interagir com o mundo real. Veremos como os agentes podem raciocinar sobre qual ferramenta usar, executar ações e observar os resultados para alcançar seus objetivos. O padrão ReAct é recomendado para raciocínio iterativo e uso eficiente de ferramentas.

### **6.1. O que são Ferramentas (Tools)?**

No contexto do LangChain, uma **Ferramenta (Tool)** é uma função que um agente pode invocar para interagir com o mundo exterior. Isso pode incluir:

*   **APIs externas:** Buscar informações na web, enviar e-mails, acessar bancos de dados, etc.
*   **Funções customizadas:** Realizar cálculos complexos, manipular dados, interagir com sistemas internos.
*   **Outros modelos de IA:** Chamar modelos de visão computacional, processamento de fala, etc.

Ferramentas podem ser funções decoradas com `@tool`, instâncias de classes Tool, ou carregadas via `load_tools` para integrações externas. Descrições detalhadas são essenciais para o LLM decidir o uso correto da ferramenta. Recomenda-se testar ferramentas isoladamente antes de integrá-las ao agente.

### **6.2. Agentes (Agents): O Cérebro por Trás das Ações**

Um **Agente (Agent)** é um sistema que utiliza um LLM como seu "cérebro" para decidir qual ação tomar, observar o resultado dessa ação e repetir o processo até que a tarefa seja concluída. O processo geralmente segue o padrão **ReAct (Reason + Act)**:

1.  **Reason (Raciocinar):** O LLM analisa a entrada do usuário e o estado atual para determinar qual ferramenta (se houver) deve ser usada e com quais argumentos.
2.  **Act (Agir):** A ferramenta selecionada é executada, e o resultado é observado.
3.  **Observe (Observar):** O LLM recebe o resultado da execução da ferramenta e o utiliza para refinar seu raciocínio ou gerar a resposta final.

O LangChain oferece diversas implementações de agentes, mas a abordagem moderna e recomendada é o `create_tool_calling_agent` (LangChain) ou `create_react_agent` (LangGraph), que se beneficiam das capacidades de *tool calling* nativas dos LLMs mais recentes. Prompts podem ser customizados para orientar o agente. Recomenda-se uso de streaming (`agent_executor.stream`) para inspecionar o raciocínio do agente passo a passo.

---

### Hands-on: Exercício 1 — Agente de Análise de Vendas com Ferramenta SQL

* **Objetivo:** Criar um agente que utilize uma ferramenta SQL para consultar dados de vendas e responder a perguntas complexas.
* **Nome do Arquivo:** `exercicios/capitulo_06/exercicio_1/main.py`
* **Dependências:** `langchain`, `langchain-google-genai`, `python-dotenv`
* **Comando de Instalação:**
```sh
uv add langchain langchain-google-genai python-dotenv
```
* **Configuração Adicional:** Certifique-se de que sua chave de API do Google Gemini (`GOOGLE_API_KEY`) está configurada corretamente no seu arquivo `.env`.

```python
# exercicios/capitulo_06/exercicio_1/main.py
import sqlite3
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool

# Carregar variáveis de ambiente
load_dotenv()

# 1. Configurar o banco de dados SQLite em memória
def setup_database():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY,
            produto TEXT,
            quantidade INTEGER,
            preco REAL,
            data TEXT
        )
    ''')
    vendas_data = [
        ('Laptop', 2, 1200.00, '2024-01-15'),
        ('Mouse', 5, 25.00, '2024-01-15'),
        ('Teclado', 3, 75.00, '2024-01-16'),
        ('Monitor', 1, 300.00, '2024-01-17'),
        ('Laptop', 1, 1200.00, '2024-01-18'),
        ('Webcam', 4, 50.00, '2024-01-18'),
    ]
    cursor.executemany('INSERT INTO vendas (produto, quantidade, preco, data) VALUES (?, ?, ?, ?)', vendas_data)
    conn.commit()
    return conn

# 2. Definir a ferramenta SQL para o agente
@tool
def execute_sql_query(query: str) -> str:
    """
    Executa uma consulta SQL no banco de dados de vendas e retorna o resultado.
    Use esta ferramenta para responder a perguntas sobre dados de vendas.
    O banco de dados contém uma tabela 'vendas' com as colunas:
    'id', 'produto', 'quantidade', 'preco', 'data'.
    Exemplo de uso: SELECT SUM(quantidade) FROM vendas WHERE produto = 'Laptop';
    """
    conn = setup_database()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return str(results)
    except sqlite3.Error as e:
        conn.close()
        return f"Erro ao executar a consulta SQL: {e}"

# 3. Escolher o LLM que será o cérebro do nosso agente
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# 4. Definir as ferramentas que o agente pode usar
tools = [execute_sql_query]

# 5. Criar o Prompt do Agente
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente especializado em analisar dados de vendas. Use a ferramenta 'execute_sql_query' para responder a perguntas sobre vendas. Se a pergunta não puder ser respondida com os dados de vendas, diga que não tem informações."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# 6. Criar o Agente
agent = create_tool_calling_agent(llm, tools, prompt)

# 7. Criar o Executor do Agente
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- Execução ---
if __name__ == "__main__":
    print("Agente de Análise de Vendas pronto! Faça sua pergunta.")

    perguntas = [
        "Qual a quantidade total de Laptops vendidos?",
        "Qual o produto mais vendido em termos de quantidade?",
        "Qual o valor total de vendas?",
        "Quantos itens foram vendidos em 2024-01-18?",
        "Qual o nome do meu cachorro?"
    ]

    for pergunta in perguntas:
        print(f"\n> Pergunta: {pergunta}")
        response = agent_executor.invoke({"input": pergunta})
        print(f"\n< Resposta Final: {response['output']}")
```

**Comando de Execução (Linux/macOS):**
```sh
cd exercicios/capitulo_06/exercicio_1
chmod +x run.sh
./run.sh
```
**Comando de Execução (Windows):**
```bat
cd exercicios\capitulo_06\exercicio_1
call run.bat
```
**Saída Esperada (pode variar):**
```
Agente de Análise de Vendas pronto! Faça sua pergunta.
> Pergunta: Qual a quantidade total de Laptops vendidos?
< Resposta Final: ...
> Pergunta: Qual o produto mais vendido em termos de quantidade?
< Resposta Final: ...
> Pergunta: Qual o valor total de vendas?
< Resposta Final: ...
> Pergunta: Quantos itens foram vendidos em 2024-01-18?
< Resposta Final: ...
> Pergunta: Qual o nome do meu cachorro?
< Resposta Final: Não tenho informações sobre isso.
```
**Troubleshooting Comum:**
* `sqlite3.OperationalError: no such table: vendas`: Verifique se a função `setup_database()` está sendo chamada corretamente.
* `AuthenticationError`: Verifique a chave de API do Gemini no `.env`.
* `ModuleNotFoundError`: Instale todas as dependências com `uv add`.

---

### Hands-on: Exercício 2 — Agente de Cotação de Moedas com Ferramenta de API Externa

* **Objetivo:** Criar um agente que utilize uma ferramenta para consultar taxas de câmbio de moedas via API externa.
* **Nome do Arquivo:** `exercicios/capitulo_06/exercicio_2/main.py`
* **Dependências:** `langchain`, `langchain-google-genai`, `python-dotenv`, `requests`
* **Comando de Instalação:**
```sh
uv add langchain langchain-google-genai python-dotenv requests
```
* **Configuração Adicional:** Se usar uma API que exija chave, adicione ao `.env` (ex: `EXCHANGE_RATE_API_KEY`).

```python
# exercicios/capitulo_06/exercicio_2/main.py
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool
import requests
import os

# Carregar variáveis de ambiente
load_dotenv()

# 1. Definir a ferramenta de cotação de moedas
@tool
def get_exchange_rate(base_currency: str, target_currency: str) -> str:
    """
    Obtém a taxa de câmbio atual entre duas moedas.
    Use esta ferramenta para converter valores entre moedas.
    Exemplo: get_exchange_rate("USD", "BRL")
    """
    try:
        # Usando uma API de cotação de moedas gratuita (ex: ExchangeRate-API)
        # Você pode precisar se registrar para obter uma chave de API real
        # Para fins de demonstração, usaremos um endpoint público ou simulado
        api_key = os.getenv("EXCHANGE_RATE_API_KEY") # Se necessário
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()
        
        if data and data["rates"] and target_currency in data["rates"]:
            rate = data["rates"][target_currency]
            return f"A taxa de câmbio de {base_currency} para {target_currency} é {rate}"
        else:
            return f"Não foi possível obter a taxa de câmbio para {base_currency}/{target_currency}"
    except Exception as e:
        return f"Erro ao obter a taxa de câmbio: {e}"

# 2. Escolher o LLM que será o cérebro do nosso agente
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# 3. Definir as ferramentas que o agente pode usar
tools = [get_exchange_rate]

# 4. Criar o Prompt do Agente
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente especializado em cotação de moedas. Use a ferramenta 'get_exchange_rate' para responder a perguntas sobre taxas de câmbio."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# 5. Criar o Agente
agent = create_tool_calling_agent(llm, tools, prompt)

# 6. Criar o Executor do Agente
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- Execução ---
if __name__ == "__main__":
    print("Agente de Cotação de Moedas pronto! Faça sua pergunta.")

    perguntas = [
        "Qual a taxa de câmbio de USD para BRL?",
        "Quanto é 100 EUR em JPY?",
        "Qual o valor do dólar hoje?",
        "Qual o nome do meu gato?"
    ]

    for pergunta in perguntas:
        print(f"\n> Pergunta: {pergunta}")
        response = agent_executor.invoke({"input": pergunta})
        print(f"\n< Resposta Final: {response['output']}")
```

**Comando de Execução (Linux/macOS):**
```sh
cd exercicios/capitulo_06/exercicio_2
chmod +x run.sh
./run.sh
```
**Comando de Execução (Windows):**
```bat
cd exercicios\capitulo_06\exercicio_2
call run.bat
```
**Saída Esperada (pode variar):**
```
Agente de Cotação de Moedas pronto! Faça sua pergunta.
> Pergunta: Qual a taxa de câmbio de USD para BRL?
< Resposta Final: ...
> Pergunta: Quanto é 100 EUR em JPY?
< Resposta Final: ...
> Pergunta: Qual o valor do dólar hoje?
< Resposta Final: ...
> Pergunta: Qual o nome do meu gato?
< Resposta Final: Não tenho informações sobre isso.
```
**Troubleshooting Comum:**
* `requests.exceptions.ConnectionError`: Verifique sua conexão com a internet.
* `AuthenticationError`: Verifique a chave de API do Gemini no `.env`.
* `ModuleNotFoundError`: Instale todas as dependências com `uv add`.

---

### Troubleshooting Comum
* Debug de ferramentas: teste funções isoladamente e verifique logs detalhados com `verbose=True`.
* Use tracing para inspeção de execuções e identificar gargalos.
* Instale todas as dependências e configure corretamente o `.env`.
* Proteja chaves de API e modularize ferramentas para facilitar manutenção.

---

### Pontos Chave
* Ferramentas permitem que LLMs interajam com sistemas externos e superem limitações.
* Agentes usam LLMs para raciocinar, decidir e executar ações com ferramentas.
* O padrão ReAct (Reason + Act) e prompts customizados são diferenciais para agentes autônomos eficientes.
* Exercícios práticos mostram integração com banco de dados, APIs externas e modularização.

---

### Resumo do Capítulo
Neste capítulo, você aprendeu como equipar LLMs com ferramentas externas, criando agentes autônomos e interativos no LangChain. Viu a diferença entre ferramentas e agentes, implementou agentes com ferramentas customizadas e APIs externas, e consolidou o aprendizado com exercícios práticos, troubleshooting e dicas de boas práticas.

---

### Teste seu Conhecimento
1. No LangChain, o que é uma Ferramenta (Tool)?
   a) Um modelo de linguagem.
   b) Uma função que o agente pode invocar para interagir com sistemas externos.
   c) Um arquivo de configuração.
   d) Um tipo de prompt especial.
2. Qual é o papel do agente em um sistema LangChain?
   a) Executar comandos de sistema.
   b) Raciocinar, decidir qual ferramenta usar e observar resultados.
   c) Gerar apenas texto sem interação externa.
   d) Armazenar dados em banco de dados.
3. O padrão ReAct (Reason + Act) envolve:
   a) Apenas raciocinar sobre a entrada do usuário.
   b) Raciocinar, agir usando ferramentas e observar resultados.
   c) Executar comandos sem raciocínio.
   d) Gerar prompts estáticos.
4. Qual erro pode ocorrer se a tabela 'vendas' não for criada corretamente?
   a) requests.exceptions.ConnectionError
   b) sqlite3.OperationalError: no such table: vendas
   c) ModuleNotFoundError
   d) AuthenticationError
5. Para consultar taxas de câmbio em tempo real, o agente precisa:
   a) Apenas um LLM.
   b) Uma ferramenta que acesse uma API externa.
   c) Um arquivo .env vazio.
   d) Um banco de dados local.
6. Como inspecionar o raciocínio do agente passo a passo?
   a) Usando agent_executor.stream para visualizar cada etapa.
   b) Executando apenas o LLM sem ferramentas.
   c) Ignorando logs.
   d) Usando prompts estáticos.

**Respostas:**
1. b
2. b
3. b
4. b
5. b
6. a

---

### Projeto Hands-on: Orquestrando Ferramentas e Agentes

Coloque em prática os conceitos do capítulo criando um projeto Python que utiliza LangChain para construir um agente capaz de integrar múltiplas ferramentas: uma para análise de dados locais (ex: vendas) e outra para consulta de APIs externas (ex: cotação de moedas). Siga a estrutura sugerida:

- Estrutura de diretórios para agentes e ferramentas.
- Checklist de boas práticas: modularização, logging, versionamento, testes automatizados.
- Fluxograma do fluxo de decisão do agente.
- Dicas para integração de múltiplas ferramentas e fontes de dados.
- Passos para ativar tracing e compartilhar logs via GitHub.
- Experimente rodar o projeto em diferentes versões do Python usando pyenv.

---