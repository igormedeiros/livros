# capitulo_07/exercicio_3/main.py
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain_core.documents import Document

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents([
    Document(page_content="O usuário gosta de pizza."),
    Document(page_content="O usuário mora em Nova York."),
], embeddings)

query = "Qual comida o usuário prefere?"
results = vectorstore.similarity_search(query)
for doc in results:
    print(doc.page_content)