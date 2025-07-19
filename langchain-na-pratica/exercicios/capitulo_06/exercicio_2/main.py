import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool
import requests

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