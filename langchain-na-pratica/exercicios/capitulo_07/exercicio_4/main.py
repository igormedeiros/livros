# capitulo_07/exercicio_4/main.py
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain_core.documents import Document

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents([
    Document(page_content="O usuário gosta de pizza."),
    Document(page_content="O usuário mora em Nova York."),
], embeddings)

query = "Qual comida o usuário prefere?"
results = vectorstore.similarity_search(query)
for doc in results:
    print(doc.page_content)