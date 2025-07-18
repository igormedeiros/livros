
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

chain_capital = ChatPromptTemplate.from_template("Qual é a capital de {pais}?") | model | parser
chain_populacao = ChatPromptTemplate.from_template("Qual é a população aproximada de {pais}?") | model | parser
chain_curiosidade = ChatPromptTemplate.from_template("Conte uma curiosidade sobre {pais}.") | model | parser

mapa_paralelo = RunnableParallel(
    capital=chain_capital,
    populacao=chain_populacao,
    curiosidade=chain_curiosidade
)

resultado = mapa_paralelo.invoke({"pais": "Egito"})
print(resultado)
