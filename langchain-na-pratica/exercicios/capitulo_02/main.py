# exercicios/capitulo_02/exercicio_1/main.py
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
prompt = ChatPromptTemplate.from_template("Diga olá para o mundo do LangChain!")
print(prompt.format())