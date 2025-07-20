# capitulo_08/exercicio_4/main.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("Resuma: {texto}")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
chain = prompt | llm

response = chain.invoke({"texto": "LangChain facilita o desenvolvimento de apps com LLMs."})
print(response.content)