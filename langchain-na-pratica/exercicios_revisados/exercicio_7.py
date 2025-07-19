# LangChain na Prática: O primeiro passo com Agentes de IA
# Autor: Igor Medeiros

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    print("Erro: A variável de ambiente GOOGLE_API_KEY não está definida.")
    print("Por favor, crie um arquivo .env na raiz do projeto com GOOGLE_API_KEY='SUA_CHAVE_AQUI'.")
    exit(1)

prompt = ChatPromptTemplate.from_template("Conte uma história curta sobre um robô que aprendeu a sonhar.")
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)
parser = StrOutputParser()

chain = prompt | model | parser

print("--- Resposta em Streaming ---")
for chunk in chain.stream({}):
    print(chunk, end="", flush=True)
print("\n--- Fim do Streaming ---")

