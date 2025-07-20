# capitulo_08/exercicio_5/main.py
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

prompt = ChatPromptTemplate.from_template("Quem dirigiu {filme}?")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
chain = prompt | llm

# Bug: não trata filmes desconhecidos
resposta = chain.invoke({"filme": "Oppenheimer"})
print(resposta.content)