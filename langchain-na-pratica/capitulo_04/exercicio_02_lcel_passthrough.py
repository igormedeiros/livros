
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

prompt_pergunta = ChatPromptTemplate.from_template("Gere uma pergunta interessante sobre {topico}.")
prompt_resposta = ChatPromptTemplate.from_template(
    "Responda a pergunta: {pergunta}. Contexto original do tópico: {topico}"
)

chain_pergunta = prompt_pergunta | model | parser

chain_completa = (
    {"pergunta": chain_pergunta, "topico": RunnablePassthrough()}
    | prompt_resposta
    | model
    | parser
)

print(chain_completa.invoke("a filosofia estoica"))
