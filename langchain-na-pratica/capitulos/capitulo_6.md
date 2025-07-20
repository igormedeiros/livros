## Capítulo 6: Ferramentas e Agentes: Capacitando LLMs com Ações

Neste capítulo, exploraremos um dos conceitos mais poderosos do LangChain: a capacidade de equipar Large Language Models (LLMs) com ferramentas externas, transformando-os em agentes autônomos capazes de interagir com o mundo real. Veremos como os agentes podem raciocinar sobre qual ferramenta usar, executar ações e observar os resultados para alcançar seus objetivos.

### **6.1. O que são Ferramentas (Tools)?**

No contexto do LangChain, uma **Ferramenta (Tool)** é uma função que um agente pode invocar para interagir com o mundo exterior. Isso pode incluir:

*   **APIs externas:** Buscar informações na web, enviar e-mails, acessar bancos de dados, etc.
*   **Funções customizadas:** Realizar cálculos complexos, manipular dados, interagir com sistemas internos.
*   **Outros modelos de IA:** Chamar modelos de visão computacional, processamento de fala, etc.

As ferramentas são essenciais porque os LLMs, por si só, têm limitações. Eles podem gerar texto, mas não podem, por exemplo, buscar informações em tempo real na internet ou executar código. Ao fornecer ferramentas, capacitamos o LLM a superar essas limitações e a realizar tarefas que exigem interação com sistemas externos.

### **6.2. Agentes (Agents): O Cérebro por Trás das Ações**

Um **Agente (Agent)** é um sistema que utiliza um LLM como seu "cérebro" para decidir qual ação tomar, observar o resultado dessa ação e repetir o processo até que a tarefa seja concluída. O processo geralmente segue o padrão **ReAct (Reason + Act)**:

1.  **Reason (Raciocinar):** O LLM analisa a entrada do usuário e o estado atual para determinar qual ferramenta (se houver) deve ser usada e com quais argumentos.
2.  **Act (Agir):** A ferramenta selecionada é executada, e o resultado é observado.
3.  **Observe (Observar):** O LLM recebe o resultado da execução da ferramenta e o utiliza para refinar seu raciocínio ou gerar a resposta final.

O LangChain oferece diversas implementações de agentes, mas a abordagem moderna e recomendada é o `create_tool_calling_agent`, que se beneficia das capacidades de *tool calling* nativas dos LLMs mais recentes, como o Gemini.

### **Exercício 1: Agente de Análise de Vendas com Ferramenta SQL**

Neste exercício, construiremos um agente capaz de interagir com um banco de dados SQLite em memória para responder a perguntas sobre dados de vendas. O agente usará uma ferramenta customizada para executar consultas SQL.

*   **Objetivo:** Criar um agente que utilize uma ferramenta SQL para consultar dados de vendas e responder a perguntas complexas.
*   **Nome do Arquivo:** `exercicios/capitulo_06/exercicio_1/main.py`
*   **Dependências:** `langchain`, `langchain-google-genai`, `python-dotenv`
*   **Comando de Instalação:** `uv add langchain langchain-google-genai python-dotenv`

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

**Comandos de Execução (Linux/macOS):**

```sh
# Navegue até o diretório do exercício
cd exercicios/capitulo_06/exercicio_1

# Dê permissão de execução ao script
chmod +x run.sh

# Execute o exercício
./run.sh
```

**Comandos de Execução (Windows):**

```bat
REM Navegue até o diretório do exercício
cd exercicios\capitulo_06\exercicio_1

REM Execute o exercício
call run.bat
```

**Saída Esperada:**

```text
Agente de Análise de Vendas pronto! Faça sua pergunta.

> Pergunta: Qual a quantidade total de Laptops vendidos?

> Pergunta: Qual o produto mais vendido em termos de quantidade?

> Pergunta: Qual o valor total de vendas?

> Pergunta: Quantos itens foram vendidos em 2024-01-18?

> Pergunta: Qual o nome do meu cachorro?
```

**Troubleshooting Comum:**

*   **`sqlite3.OperationalError: no such table: vendas`**: Verifique se a função `setup_database()` está sendo chamada corretamente e se a tabela `vendas` está sendo criada antes das consultas.
*   **`AuthenticationError`**: Certifique-se de que sua chave de API do Google Gemini (`GOOGLE_API_KEY`) está configurada corretamente no seu arquivo `.env`.
*   **`ModuleNotFoundError`**: Verifique se todas as dependências (`langchain`, `langchain-google-genai`, `python-dotenv`) foram instaladas usando `uv add`.

### **Exercício 2: Agente de Cotação de Moedas com Ferramenta de API Externa**

Neste exercício, construiremos um agente capaz de obter taxas de câmbio de moedas usando uma API externa. Isso demonstra como os agentes podem interagir com serviços web para obter informações em tempo real.

*   **Objetivo:** Criar um agente que utilize uma ferramenta para consultar taxas de câmbio de moedas via API externa.
*   **Nome do Arquivo:** `exercicios/capitulo_06/exercicio_2/main.py`
*   **Dependências:** `langchain`, `langchain-google-genai`, `python-dotenv`, `requests`
*   **Comando de Instalação:** `uv add langchain langchain-google-genai python-dotenv requests`
*   **Configuração Adicional:** Para este exemplo, a API `ExchangeRate-API` é usada. Embora o exemplo não exija uma chave, APIs de cotação de moedas reais geralmente exigem. Se você usar uma API que precise de chave, adicione-a ao seu arquivo `.env` (ex: `EXCHANGE_RATE_API_KEY`).

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

**Comandos de Execução (Linux/macOS):**

```sh
# Navegue até o diretório do exercício
cd exercicios/capitulo_06/exercicio_2

# Dê permissão de execução ao script
chmod +x run.sh

# Execute o exercício
./run.sh
```

**Comandos de Execução (Windows):**

```bat
REM Navegue até o diretório do exercício
cd exercicios\capitulo_06\exercicio_2

REM Execute o exercício
call run.bat
```

**Saída Esperada:**

```text
Agente de Cotação de Moedas pronto! Faça sua pergunta.

> Pergunta: Qual a taxa de câmbio de USD para BRL?

> Pergunta: Quanto é 100 EUR em JPY?

> Pergunta: Qual o valor do dólar hoje?

> Pergunta: Qual o nome do meu gato?
```

**Troubleshooting Comum:**

*   **`requests.exceptions.ConnectionError`**: Verifique sua conexão com a internet. A API de cotação de moedas requer acesso à internet.
*   **`AuthenticationError`**: Certifique-se de que sua chave de API do Google Gemini (`GOOGLE_API_KEY`) está configurada corretamente no seu arquivo `.env`.
*   **`ModuleNotFoundError`**: Verifique se todas as dependências (`langchain`, `langchain-google-genai`, `python-dotenv`, `requests`) foram instaladas usando `uv add`.