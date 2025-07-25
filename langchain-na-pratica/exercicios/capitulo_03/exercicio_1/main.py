import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Carrega variáveis de ambiente (.env)
load_dotenv()

# Inicializa o modelo Gemini
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# Template dinâmico para tradução
template = """Você é um tradutor multilíngue especialista.
Traduza o texto abaixo para o idioma: {idioma_destino}.
Responda apenas com a tradução.

Texto:
{texto_origem}
"""

prompt = ChatPromptTemplate.from_template(template)
parser = StrOutputParser()

# Pipeline LCEL: prompt -> modelo -> parser
chain = prompt | llm | parser

# Exemplos de uso
exemplos = [
    {"texto_origem": "A inteligência artificial está mudando o mundo.", "idioma_destino": "Francês"},
    {"texto_origem": "Python is a powerful programming language.", "idioma_destino": "Japonês"},
    {"texto_origem": "Heddllo, world!", "idioma_destino": "Klingon"},
]

# main
__name__ = "__main__"

for exemplo in exemplos:
    print(f"Traduzindo '{exemplo['texto_origem']}' para {exemplo['idioma_destino']}...")
    resultado = chain.invoke(exemplo)
    print(f"Resultado: {resultado}\n")