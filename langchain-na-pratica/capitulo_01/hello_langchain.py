

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Carrega as variáveis de ambiente (necessário para a chave do Google)
# Certifique-se de ter um arquivo .env como explicado no Capítulo 2
load_dotenv()

# 1. Crie um template de prompt.
#    Pense nisso como o "molde" para a sua pergunta.
#    A variável {topico} será preenchida dinamicamente.
prompt_template = ChatPromptTemplate.from_template(
    "Escreva uma única frase engraçada sobre o tópico: {topico}"
)

# 2. Inicialize o modelo de linguagem.
#    Este é o "cérebro" que vai gerar a resposta. Usaremos o Gemini Flash.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 3. Crie um parser de saída.
#    Ele vai extrair apenas o texto da resposta do modelo.
output_parser = StrOutputParser()

# 4. Crie a "Chain" usando o operador pipe (|).
#    Esta é a mágica da LangChain Expression Language (LCEL)!
#    O fluxo é: prompt -> modelo -> parser
chain = prompt_template | model | output_parser

# 5. Invoque a chain com um tópico.
#    O LangChain cuida de passar o resultado de um passo para o outro.
print("Executando a chain...")
resposta = chain.invoke({"topico": "desenvolvedores Python"})

# Imprime o resultado final
print("\nResposta da Chain:")
print(resposta)

