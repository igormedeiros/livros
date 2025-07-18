
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_template("Crie uma sinopse de filme de uma frase para o gênero: {genero}")
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({"genero": "Comédia de Ficção Científica"}))
