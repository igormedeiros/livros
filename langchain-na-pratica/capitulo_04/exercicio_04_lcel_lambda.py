
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

def calcular_quadrados(numeros: list[int]) -> list[int]:
    print("Executando a função Python para calcular quadrados...")
    return [n*n for n in numeros]

prompt = ChatPromptTemplate.from_template("Descreva esta lista de números de forma poética: {lista_quadrados}")
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

chain = (
    RunnableLambda(calcular_quadrados)
    | (lambda quadrados: {"lista_quadrados": quadrados})
    | prompt
    | model
    | parser
)

print(chain.invoke([1, 2, 3, 4, 5]))
