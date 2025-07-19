# LangChain na Prática: O primeiro passo com Agentes de IA
# Autor: Igor Medeiros

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily_search import TavilySearchResults
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

# Carregar variáveis de ambiente
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    print("Erro: A variável de ambiente GOOGLE_API_KEY não está definida.")
    print("Por favor, crie um arquivo .env na raiz do projeto com GOOGLE_API_KEY='SUA_CHAVE_AQUI'.")
    exit(1)

# 1. Escolher o LLM que será o cérebro do nosso agente
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)

# 2. Definir as ferramentas que o agente pode usar
search_tool = TavilySearchResults(
    max_results=2,
    description="Uma ferramenta de busca para encontrar informações na internet sobre eventos atuais, pessoas, lugares ou empresas."
)
tools = [search_tool]

# 3. Criar o Prompt do Agente
# Este prompt é um template especial que guia o agente
# Os placeholders {chat_history} e {agent_scratchpad} são gerenciados pelo AgentExecutor
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente prestativo."),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# 4. Criar o Agente
# Esta função conecta o LLM, as ferramentas e o prompt
agent = create_tool_calling_agent(llm, tools, prompt)

# 5. Criar o Executor do Agente
# O executor é o loop que roda o agente até a resposta final
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- Execução ---
if __name__ == "__main__":
    print("Agente de Pesquisa pronto! Faça sua pergunta.")
    
    pergunta1 = "Qual foi o filme vencedor do Oscar de Melhor Filme em 2024?"
    print(f"\n> Pergunta: {pergunta1}")
    response1 = agent_executor.invoke({"input": pergunta1})
    print(f"\n< Resposta Final: {response1['output']}")

    pergunta2 = "Qual é a cor do céu?"
    print(f"\n> Pergunta: {pergunta2}")
    response2 = agent_executor.invoke({"input": pergunta2})
    print(f"\n< Resposta Final: {response2['output']}")
