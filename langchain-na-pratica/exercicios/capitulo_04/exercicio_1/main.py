from dotenv import load_dotenv
from langchain.chains import LLMChain, SequentialChain
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# Chain 1: Gera uma pergunta
template_pergunta = "Gere uma pergunta criativa sobre o tópico: {topico}"
prompt_pergunta = PromptTemplate.from_template(template_pergunta)
chain_pergunta = LLMChain(llm=llm, prompt=prompt_pergunta, output_key="pergunta")

# Chain 2: Responde a pergunta gerada
template_resposta = "Responda a seguinte pergunta de forma elaborada: {pergunta}"
prompt_resposta = PromptTemplate.from_template(template_resposta)
chain_resposta = LLMChain(llm=llm, prompt=prompt_resposta, output_key="resposta_final")

# Unindo as duas com SequentialChain
# Note como precisamos definir explicitamente as chaves de entrada e saída
overall_chain = SequentialChain(
    chains=[chain_pergunta, chain_resposta],
    input_variables=["topico"],
    output_variables=["pergunta", "resposta_final"],
    verbose=True # Para vermos o que está acontecendo
)

# Executando a chain
resultado = overall_chain({"topico": "a relatividade de Einstein"})
print("\n--- RESULTADO FINAL ---")
print(resultado)
