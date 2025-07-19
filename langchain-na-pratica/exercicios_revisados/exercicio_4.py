
# LangChain na Prática: O primeiro passo com Agentes de IA
# Autor: Igor Medeiros

import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    print("Erro: A variável de ambiente GOOGLE_API_KEY não está definida.")
    print("Por favor, crie um arquivo .env na raiz do projeto com GOOGLE_API_KEY='SUA_CHAVE_AQUI'.")
    exit(1)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)
parser = StrOutputParser()

prompt_pergunta = ChatPromptTemplate.from_template("Gere uma pergunta interessante sobre {topico}.")
prompt_resposta = ChatPromptTemplate.from_template(
    "Responda a pergunta: {pergunta}. Contexto original do tópico: {topico}"
)

chain_pergunta = prompt_pergunta | model | parser

chain_completa = (
    {"pergunta": chain_pergunta, "topico": RunnablePassthrough()}
    | prompt_resposta
    | model
    | parser
)

print(chain_completa.invoke("a filosofia estoica"))
