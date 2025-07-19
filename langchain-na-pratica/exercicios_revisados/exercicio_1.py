

# LangChain na Prática: O primeiro passo com Agentes de IA
# Autor: Igor Medeiros

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
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    print("Erro: A variável de ambiente GOOGLE_API_KEY não está definida.")
    print("Por favor, crie um arquivo .env na raiz do projeto com GOOGLE_API_KEY='SUA_CHAVE_AQUI'.")
    exit(1)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)

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

