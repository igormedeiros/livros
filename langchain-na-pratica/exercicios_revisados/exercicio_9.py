# LangChain na Prática: O primeiro passo com Agentes de IA
# Autor: Igor Medeiros

import os
import sqlite3
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool

# Carregar variáveis de ambiente
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    print("Erro: A variável de ambiente GOOGLE_API_KEY não está definida.")
    print("Por favor, crie um arquivo .env na raiz do projeto com GOOGLE_API_KEY='SUA_CHAVE_AQUI'.")
    exit(1)

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
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, google_api_key=google_api_key)

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
