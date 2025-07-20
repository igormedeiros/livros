# exercicios/capitulo_01/exercicio_2/main.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

# Carrega as variáveis de ambiente
load_dotenv()

# Inicializa o LLM
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# Cria um template de prompt com um placeholder para o histórico de chat
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente prestativo. Responda às perguntas de forma concisa e útil."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# Cria o parser de saída
output_parser = StrOutputParser()

# Cria a chain
chain = prompt | model | output_parser

# Histórico de chat (simulado por enquanto)
chat_history = []

print("Chatbot Simples. Digite 'sair' para encerrar.")

while True:
    user_input = input("Você: ")
    if user_input.lower() == 'sair':
        break

    # Invoca a chain com a entrada do usuário e o histórico de chat
    response = chain.invoke({
        "input": user_input,
        "chat_history": chat_history
    })

    print(f"Bot: {response}")

    # Atualiza o histórico de chat
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response))

print("Chatbot encerrado.")