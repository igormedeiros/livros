# LangChain na Prática: O primeiro passo com Agentes de IA
# Autor: Igor Medeiros

import os
import requests
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

# 1. Definir a ferramenta para consultar uma API de cotação de moedas
@tool
def get_exchange_rate(base_currency: str, target_currency: str) -> str:
    """
    Obtém a taxa de câmbio atual entre duas moedas usando uma API externa.
    Use esta ferramenta para converter valores entre moedas.
    A API utilizada é a ExchangeRate-API (https://www.exchangerate-api.com/).
    Você precisa de uma chave de API gratuita da ExchangeRate-API, adicionada ao .env como EXCHANGERATE_API_KEY.
    
    Args:
        base_currency (str): O código da moeda base (ex: USD, EUR, BRL).
        target_currency (str): O código da moeda alvo (ex: USD, EUR, BRL).
        
    Returns:
        str: A taxa de câmbio ou uma mensagem de erro.
    """
    api_key = os.getenv("EXCHANGERATE_API_KEY")
    if not api_key:
        return "Erro: Chave de API EXCHANGERATE_API_KEY não configurada no .env"

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para status de resposta ruins (4xx ou 5xx)
        data = response.json()
        if data["result"] == "success":
            return f"1 {base_currency} = {data["conversion_rate"]} {target_currency}"
        else:
            return f"Erro na API: {data["error-type"]}"
    except requests.exceptions.RequestException as e:
        return f"Erro de conexão com a API: {e}"
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"

# 2. Escolher o LLM que será o cérebro do nosso agente
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, google_api_key=google_api_key)

# 3. Definir as ferramentas que o agente pode usar
tools = [get_exchange_rate]

# 4. Criar o Prompt do Agente
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente financeiro prestativo. Use a ferramenta 'get_exchange_rate' para obter taxas de câmbio entre moedas. Se a pergunta não for sobre taxas de câmbio, diga que não pode ajudar."),
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
        "Quanto é 100 EUR em JPY?", # O agente precisará fazer 2 chamadas ou inferir
        "Qual a capital da França?"
    ]

    for pergunta in perguntas:
        print(f"\n> Pergunta: {pergunta}")
        response = agent_executor.invoke({"input": pergunta})
        print(f"\n< Resposta Final: {response['output']}")
