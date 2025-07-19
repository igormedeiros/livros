
# LangChain na Prática: O primeiro passo com Agentes de IA
# Autor: Igor Medeiros

import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    print("Erro: A variável de ambiente GOOGLE_API_KEY não está definida.")
    print("Por favor, crie um arquivo .env na raiz do projeto com GOOGLE_API_KEY='SUA_CHAVE_AQUI'.")
    exit(1)

def calcular_quadrados(numeros: list[int]) -> list[int]:
    print("Executando a função Python para calcular quadrados...")
    return [n*n for n in numeros]

prompt = ChatPromptTemplate.from_template("Descreva esta lista de números de forma poética: {lista_quadrados}")
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)
parser = StrOutputParser()

chain = (
    RunnableLambda(calcular_quadrados)
    | (lambda quadrados: {"lista_quadrados": quadrados})
    | prompt
    | model
    | parser
)

print(chain.invoke([1, 2, 3, 4, 5]))
