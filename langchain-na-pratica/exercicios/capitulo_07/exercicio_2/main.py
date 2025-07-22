# exercicios/capitulo_07/exercicio_2/main.py
import os
from dotenv import load_dotenv

# LangChain Imports
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# --- 1. FASE DE INDEXAÇÃO (INGESTÃO DE DADOS) ---


# Carregar o conteúdo do arquivo Markdown
print("Carregando Markdown...")
with open("universo.md", "r", encoding="utf-8") as f:
    markdown_text = f.read()

# Definir os delimitadores de chunk para capturar seções inteiras por subtítulo
headers_to_split_on = [
    ("#", "Título"),
    ("##", "Subtítulo"),
    ("###", "Subsubtítulo"),
]

print("Dividindo documento em chunks por subtítulo...")
text_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on,
    strip_headers=True
)

# O método correto é split_text, que retorna uma lista de Document
splits = text_splitter.split_text(markdown_text)

# Inicializar o modelo de embeddings do Google
print("Inicializando modelo de embeddings...")
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Criar o banco de dados vetorial ChromaDB com os chunks
print("Criando e armazenando embeddings no ChromaDB...")
vectorstore = Chroma.from_documents(documents=splits, embedding=embedding_model)

# --- 2. FASE DE RECUPERAÇÃO E GERAÇÃO (RAG) ---

# Criar o retriever a partir do vectorstore
retriever = vectorstore.as_retriever()

# Inicializar o LLM Gemini
print("Inicializando LLM Gemini...")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# Template do Prompt
prompt_template = """
Use o seguinte contexto para responder à pergunta.
Se você não sabe a resposta, apenas diga que não sabe. Não tente inventar uma resposta.

Contexto:
{context}

Pergunta:
{question}

Resposta útil:
"""
prompt = ChatPromptTemplate.from_template(prompt_template)

# Função para formatar os documentos recuperados
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Construir a cadeia RAG usando LangChain Expression Language (LCEL)
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# --- 3. INTERAÇÃO COM O USUÁRIO ---

print("\nSetup completo! O chatbot está pronto.")
print("Digite 'sair' para encerrar.")

while True:
    user_question = input("\nFaça sua pergunta: ")
    if user_question.lower() == 'sair':
        break
    
    print("\nGerando resposta...")
    response = rag_chain.invoke(user_question)
    print("--- Resposta ---")
    print(response)
    print("----------------")

# Limpeza (opcional): remove o banco de dados vetorial ao sair
vectorstore.delete_collection()
print("\nChatbot encerrado.")