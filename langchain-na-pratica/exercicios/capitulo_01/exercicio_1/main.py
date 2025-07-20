# main.py

# 1. Declara as as bibliotecas necessárias
import os  
from dotenv import load_dotenv  
from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain_core.prompts import ChatPromptTemplate  
from langchain_core.output_parsers import StrOutputParser

# 2 - Carrega as variáveis de ambiente (necessário para a chave do Google)  
# Certifique-se de ter um arquivo .env  
load_dotenv()

# 3. Crie um template de prompt.  
# A variável {topico} será preenchida dinamicamente.  
prompt_template = ChatPromptTemplate.from_template(  
    "Escreva uma única frase engraçada sobre o tópico: {topico}"  
)

# 4. Inicialize o LLM.  gemini-2.5-flash
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 3. Crie um parser de saída.  
#    Ele vai extrair apenas o texto da resposta do modelo.  
output_parser = StrOutputParser()

# 4. Crie a "Chain" usando o operador pipe (|).  
#    O fluxo é: prompt -> modelo -> parser  
chain = prompt_template | model | output_parser

# 5. Invoque a chain com um tópico.  
#    O LangChain cuida de passar o resultado de um passo para o outro.  
print("Executando a chain...")  
resposta = chain.invoke({"topico": "desenvolvedores Python"})

# Imprime o resultado final  
print("\nResposta da Chain:")  
print(resposta)