from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_template("Conte uma história curta sobre um robô que aprendeu a sonhar.")
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

chain = prompt | model | parser

print("--- Resposta em Streaming ---")
for chunk in chain.stream({}):
    print(chunk, end="", flush=True)
print("\n--- Fim do Streaming ---")

