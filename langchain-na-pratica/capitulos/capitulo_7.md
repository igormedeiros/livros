## Capítulo 7: RAG - Geração Aumentada por Recuperação com LangChain

**Neste capítulo, você vai aprender:**

*   O que é RAG (Retrieval-Augmented Generation) e por que essa técnica é fundamental para criar IAs com conhecimento atualizado e específico.
*   Os conceitos essenciais por trás do RAG: Embeddings, Bancos de Dados Vetoriais (ChromaDB) e Chunking.
*   Como usar a LangChain Expression Language (LCEL) para construir pipelines de RAG de forma declarativa e intuitiva.
*   A implementação de um projeto prático: um chatbot que responde a perguntas sobre um documento PDF usando RAG, LangChain e o modelo Gemini do Google.


### O Problema: A Memória Curta da IA

Modelos de linguagem (LLMs) como o Gemini do Google são extremamente inteligentes, mas seu conhecimento é limitado ao que viram durante o treinamento. Eles não sabem sobre seus documentos privados ou eventos recentes. Para resolver isso, usamos uma técnica chamada RAG (Retrieval-Augmented Generation), que dá ao LLM uma "memória externa" para consultar.

Esse problema é conhecido como "memória curta" dos LLMs. Mesmo os modelos mais avançados, como o Gemini, GPT-4 ou Claude, só conseguem responder com base nas informações presentes em seus dados de treinamento, que geralmente têm um corte temporal (por exemplo, até 2023) e não incluem documentos privados, dados corporativos ou informações específicas do seu contexto. Isso significa que, se você perguntar sobre um relatório interno da sua empresa, um artigo científico recém-publicado ou até mesmo sobre um documento PDF que só você possui, o LLM não conseguirá responder de forma precisa — simplesmente porque ele nunca viu esse conteúdo.

Além disso, LLMs não têm acesso direto à internet ou a bancos de dados externos durante a inferência. Eles não podem buscar informações em tempo real ou consultar arquivos locais por conta própria. Isso limita bastante sua utilidade em aplicações que exigem respostas atualizadas, personalizadas ou baseadas em dados privados.

Outro desafio é o tamanho da janela de contexto: mesmo que você tente "colar" um documento inteiro no prompt, há um limite de tokens que o modelo pode processar de uma vez. Documentos longos, bases de conhecimento extensas ou múltiplos arquivos rapidamente ultrapassam esse limite, tornando inviável enviar tudo para o LLM analisar de uma só vez.

Por isso, surge a necessidade de uma abordagem que permita ao LLM acessar informações externas de forma eficiente, segura e contextualizada. É aí que entra o RAG: ele atua como um "ponteiro inteligente" para a memória externa, permitindo que o modelo recupere apenas os trechos mais relevantes de grandes volumes de dados e use esse contexto para gerar respostas fundamentadas, atualizadas e personalizadas.

Em resumo, a limitação dos LLMs em acessar conhecimento fora do seu treinamento é um obstáculo para aplicações práticas em ambientes corporativos, acadêmicos ou pessoais. O RAG resolve esse problema ao conectar o modelo a fontes de dados externas, ampliando sua utilidade e tornando-o realmente capaz de responder perguntas sobre qualquer conteúdo que você desejar.


### A Solução: RAG (Geração Aumentada por Recuperação)

RAG (Retrieval-Augmented Generation) é uma abordagem que conecta modelos de linguagem (LLMs) a fontes externas de conhecimento, permitindo que eles respondam perguntas com base em informações que não estavam presentes em seus dados de treinamento. O processo de RAG pode ser dividido em três etapas principais:

1. **Recuperar (Retrieve):** Quando uma pergunta é feita, o sistema busca os trechos mais relevantes de uma base de conhecimento externa (como documentos, wikis, PDFs, bancos de dados, etc.). Essa busca é feita por similaridade semântica, usando embeddings para encontrar os textos mais próximos do significado da pergunta.

2. **Aumentar (Augment):** Os trechos recuperados são inseridos em um prompt junto com a pergunta original. Esse contexto adicional fornece ao LLM informações específicas e atualizadas, ampliando sua capacidade de resposta.

3. **Gerar (Generate):** O prompt enriquecido é enviado ao LLM, que utiliza tanto o contexto recuperado quanto seu conhecimento prévio para gerar uma resposta precisa, fundamentada e contextualizada.

Essa arquitetura reduz significativamente o risco de "alucinações" (respostas inventadas) e permite que a IA utilize dados privados, corporativos ou atualizados, tornando-a muito mais útil em cenários do mundo real.

---

### As Ferramentas Essenciais

Para implementar um pipeline RAG eficiente, alguns componentes são fundamentais:

- **Embeddings:** São representações numéricas de textos, criadas por modelos especializados. Embeddings permitem que o significado de frases, sentenças ou documentos seja comparado matematicamente. Textos com significados semelhantes terão embeddings próximos no espaço vetorial. Isso é essencial para buscar informações relevantes por similaridade de significado, e não apenas por palavras-chave.

- **Banco de Dados Vetorial (ChromaDB):** Um banco de dados vetorial armazena embeddings e permite buscas rápidas por similaridade. O ChromaDB, por exemplo, é uma solução open source leve e fácil de usar, ideal para prototipagem e produção. Ele permite indexar grandes volumes de dados e recuperar rapidamente os chunks mais relevantes para cada pergunta.

- **Chunking:** Como LLMs têm um limite de tokens (quantidade de texto que conseguem processar de uma vez), é necessário dividir documentos longos em pedaços menores chamados chunks. O chunking garante que cada parte do texto seja gerenciável e que informações importantes não sejam perdidas. Parâmetros como `chunk_size` e `chunk_overlap` ajudam a equilibrar contexto e granularidade.

- **LangChain Expression Language (LCEL):** LCEL é uma linguagem declarativa baseada em operadores de pipeline (`|`) que facilita a composição de fluxos de processamento em IA. Com LCEL, você pode conectar loaders, splitters, retrievers, prompts, LLMs e parsers de forma enxuta e intuitiva, criando pipelines robustos e fáceis de manter.

---

Essas ferramentas, quando combinadas, permitem criar aplicações de IA capazes de responder perguntas sobre qualquer conteúdo, seja ele um documento PDF, um arquivo Markdown, uma planilha CSV ou uma base de dados inteira. O RAG transforma o LLM em um verdadeiro "especialista" sobre os dados que você fornecer, tornando-o útil para aplicações corporativas, acadêmicas e pessoais.


### Projeto Prático: Chatbot de Documentos com LCEL e Gemini

Vamos construir uma aplicação de linha de comando em Python que lê um documento PDF e responde a perguntas sobre seu conteúdo.

Use o comando abaixo para iniciar o projeto:

```sh
uv init
```

Assim, você terá a seguinte estrutura de pastas: 

```
exercicios/
└── capitulo_07/
    └── exercicio_1/
        ├── app.py
        ├── seu_documento.pdf
        ├── pyproject.toml
        └── .env
```

#### Instalação de Dependências

Crie um ambiente virtual e instale as bibliotecas com `uv`:

```sh
# Navegue até o diretório do exercício
cd exercicios/capitulo_07/exercicio_1

# Crie o ambiente virtual com uv
uv venv

# Ative o ambiente virtual
# No Linux/macOS:
source .venv/bin/activate
# No Windows:
.venv\Scripts\activate

# Instale as dependências
uv add langchain langchain-google-genai langchain-chroma pypdf python-dotenv
```

#### Configuração da Chave de API

Você precisará de uma chave de API do Google AI Studio. Crie um arquivo chamado `.env` na pasta do projeto e adicione sua chave:

```
GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"
```

#### O Código Completo (`main.py`)

Este script único contém toda a lógica. Ele carrega o PDF, o divide em chunks, armazena no ChromaDB e cria a cadeia RAG com LCEL para interagir com o modelo Gemini.

```python
# exercicios/capitulo_07/exercicio_1/main.py
import os
from dotenv import load_dotenv

# LangChain Imports
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# --- 1. FASE DE INDEXAÇÃO (INGESTÃO DE DADOS) ---

# Carregar o documento PDF
print("Carregando PDF...")
loader = PyPDFLoader("seu_documento.pdf")
docs = loader.load()

# Dividir o documento em chunks
print("Dividindo documento em chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

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
```

---

### Executando e Testando

Para executar sua aplicação, simplesmente rode o script no seu terminal:

```sh
uv run main.py
```

A aplicação irá processar seu PDF e, em seguida, solicitará que você faça perguntas.

**Exemplo de Interação:**

1.  Carregue um PDF sobre a história do Brasil.
2.  Execute `uv run main.py`.
3.  Quando solicitado, pergunte: "Quem descobriu o Brasil?"
4.  O chatbot usará o conteúdo do seu PDF para responder de forma precisa.

### Exemplos Adicionais

Para fixar ainda mais os conceitos, preparei outros exemplos de como usar RAG com diferentes tipos de documentos e formatos.

#### Lendo Arquivos Markdown (.md)

Por que vetorizar arquivos em formato markdown? O processo para ler arquivos Markdown é muito semelhante ao de PDFs. A principal diferença é o uso do `UnstructuredMarkdownLoader`.

A vantagem prática é que markdowns são compreensíveis por humanos e LLMs ao mesmo tempo. Frequentemente, usamos markdowns em uma wiki, por exemplo, para documentar projetos, o que facilita a consulta e a atualização de informações.

Outra vantagem é o caracter delimitador, o que permite que o LLM entenda melhor a estrutura do documento, como títulos, subtítulos e listas.

**Sobre o caracter delimitador, chunk size e overlap:**

O caracter delimitador é um elemento do texto (como títulos `#`, `##`, listas ou tabelas) usado para dividir o documento em partes menores (chunks) de forma lógica. No caso de arquivos Markdown, delimitadores como títulos ajudam o splitter a identificar onde começa e termina cada seção, permitindo que cada chunk corresponda a uma parte coesa do conteúdo. Isso mantém o contexto e a estrutura do documento, facilitando a recuperação de informações relevantes durante o processo de RAG.

Ao configurar o splitter, você pode definir:

- **chunk_size**: o número máximo de caracteres em cada chunk. Por exemplo, `chunk_size=1000` cria pedaços de até 1000 caracteres. Ajuste esse valor conforme o tamanho médio das seções do seu documento e a janela de contexto do LLM.
- **chunk_overlap**: quantos caracteres do final de um chunk serão repetidos no início do próximo. Por exemplo, `chunk_overlap=200` garante que informações importantes na fronteira entre dois chunks não sejam perdidas.

Exemplo de uso com splitter de texto:

```python
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
```

No caso de Markdown, você pode usar delimitadores de cabeçalho para dividir por seções:

```python
headers_to_split_on = [
    ("#", "Título"),
    ("##", "Subtítulo"),
    ("###", "Subsubtítulo"),
]
text_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on,
    strip_headers=True
)
splits = text_splitter.split_documents(docs)
```

O ajuste desses parâmetros depende do equilíbrio entre contexto suficiente para o LLM e o limite de tokens do modelo. Teste diferentes valores para encontrar o melhor resultado para seu caso de uso.

O processo para ler e estruturar dados a partir de arquivos Markdown é bastante flexível, pois o formato markdown permite organizar informações em listas, tabelas e seções bem definidas. Ao usar o `UnstructuredMarkdownLoader`, cada seção, lista ou bloco de texto pode ser tratado como um documento separado, facilitando a recuperação de informações específicas durante o processo de RAG.

Por exemplo, se você possui um arquivo markdown com uma tabela de dados ou listas de tópicos, o loader irá dividir automaticamente esses elementos em chunks lógicos. Isso permite que perguntas direcionadas sobre itens, tópicos ou valores específicos sejam respondidas com precisão, aproveitando a estrutura do markdown para melhorar a segmentação e a relevância das respostas.

Além disso, você pode personalizar o pré-processamento do markdown para extrair apenas certas seções ou tipos de conteúdo, tornando o pipeline ainda mais adaptado ao seu caso de uso. Dessa forma, o markdown não serve apenas como um formato de documentação, mas também como uma fonte estruturada de dados para aplicações de IA.

**Estrutura de Pastas:**

```
exercicios/
└── capitulo_07/
    └── exercicio_2/
        ├── main.py
        ├── seu_documento.md
        ├── pyproject.toml
        └── .env
```

**Código Completo (`main.py`):**

```python
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
```

**Como funciona a divisão por subtítulo:**  
O `MarkdownHeaderTextSplitter` permite que cada chunk corresponda exatamente a uma seção do markdown, delimitada por títulos como `##` ou `###`. Assim, quando você faz uma pergunta, o sistema pode recuperar o chunk inteiro de um subtítulo relevante, garantindo que a resposta esteja contextualizada dentro daquela seção do documento.


**Dependências Adicionais:**

Adicione `unstructured` e `markdown` ao seu `pyproject.toml`:

```toml
[project]
# ...
dependencies = [
    # ...
    "unstructured",
    "markdown",
]
```

#### Lendo Arquivos CSV (.csv)

Para arquivos CSV, usamos o `CSVLoader`. Ele trata cada linha do CSV como um documento separado.

**Como funciona a leitura de CSV:**

O formato CSV (Comma-Separated Values) é amplamente utilizado para armazenar dados tabulares, como planilhas ou exportações de bancos de dados. Cada linha do arquivo representa um registro (ou entrada), e cada coluna representa um campo desse registro.

Ao usar o `CSVLoader` da LangChain, cada linha do CSV é carregada como um documento independente. Isso significa que, para cada registro, você terá um chunk separado no seu banco vetorial. Esse comportamento é útil para buscas precisas em dados estruturados, como perguntas sobre clientes, produtos, transações, etc.

**Exemplo de uso:**

```python
from langchain_community.document_loaders.csv_loader import CSVLoader

# Carregar o documento CSV
loader = CSVLoader(file_path="seus_dados.csv")
docs = loader.load()

# docs será uma lista de Document, cada um representando uma linha do CSV
```

Se o seu CSV for muito grande, você pode aplicar chunking adicional em campos de texto longos, mas normalmente cada linha já é um chunk lógico.

**Dica:**
Os objetos `Document` criados pelo loader incluem os dados de cada linha e também podem conter metadados, como o número da linha ou o nome das colunas. Isso facilita a recuperação de informações específicas e a exibição de resultados contextualizados.

**Quando usar CSVLoader:**
- Quando você tem dados tabulares e quer permitir buscas por registros específicos.
- Quando precisa de granularidade por linha (ex: perguntas sobre um cliente ou transação específica).

Se quiser personalizar o pré-processamento, pode manipular os dados antes de criar os embeddings, por exemplo, filtrando colunas ou combinando campos em um texto único para cada registro.



**Estrutura de Pastas:**

```
exercicios/
└── capitulo_07/
    └── exercicio_3/
        ├── app_csv.py
        ├── seus_dados.csv
        ├── pyproject.toml
        └── .env
```

**Código Completo (`main.py`):**

```python
# exercicios/capitulo_07/exercicio_3/main.py
import os
from dotenv import load_dotenv

# LangChain Imports
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# --- 1. FASE DE INDEXAÇÃO (INGESTÃO DE DADOS) ---

# Carregar o documento CSV
print("Carregando CSV...")
loader = CSVLoader(file_path="seus_dados.csv")
docs = loader.load()

# Se necessário, aplicar chunking em campos de texto longos
# Para a maioria dos casos, cada linha já é um chunk lógico
# Exemplo de uso do splitter (opcional):
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# splits = text_splitter.split_documents(docs)
splits = docs  # normalmente, cada linha do CSV já é um chunk

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
```

**Sobre o delimitador e chunking em CSV:**  
No caso de arquivos CSV, cada linha já funciona como um chunk lógico, pois representa um registro completo da tabela. Se algum campo do CSV contiver textos longos (por exemplo, descrições ou observações), você pode aplicar um splitter adicional nesses campos usando o `RecursiveCharacterTextSplitter` para garantir que o conteúdo não ultrapasse o limite de contexto do LLM. No entanto, para a maioria dos usos, cada linha do CSV é suficiente como unidade de recuperação, facilitando buscas precisas e contextualizadas.


### Pontos Chave

*   RAG é uma técnica poderosa para estender o conhecimento de LLMs com dados privados ou atualizados.
*   O processo de RAG consiste em Recuperar, Aumentar e Gerar.
*   Ferramentas como ChromaDB para armazenamento vetorial e LCEL para construção de pipelines são essenciais para implementar RAG com LangChain.
*   A combinação de LangChain com modelos como o Gemini permite criar aplicações de IA sofisticadas com relativa simplicidade.

---

### Resumo do Capítulo

Neste capítulo, você mergulhou no mundo da Geração Aumentada por Recuperação (RAG). Aprendeu os conceitos fundamentais que tornam essa técnica possível e construiu um chatbot funcional do zero, capaz de conversar sobre o conteúdo de um documento PDF. Este projeto prático demonstrou como LangChain, ChromaDB e os modelos Gemini do Google se unem para criar soluções de IA inteligentes e com conhecimento específico.

Além do exemplo com PDF, você também aprendeu como aplicar RAG em outros formatos de documentos, como Markdown e CSV. Viu como o uso de delimitadores (como títulos em Markdown ou linhas em CSV) permite dividir o conteúdo em chunks lógicos, facilitando a recuperação de informações relevantes e mantendo o contexto necessário para respostas precisas.

O capítulo detalhou a importância de ajustar o tamanho do chunk e o overlap para equilibrar contexto e eficiência, além de mostrar como cada tipo de documento pode exigir estratégias diferentes de chunking. Você viu exemplos práticos de como configurar o splitter para cada caso, garantindo que tanto textos longos quanto dados tabulares possam ser usados em pipelines de RAG.

Também foram apresentadas dicas para produção, como persistir o banco vetorial em disco, trabalhar com múltiplos documentos e enriquecer as respostas do chatbot com metadados (por exemplo, indicando a página ou linha de origem da informação). Essas práticas tornam o sistema mais robusto, eficiente e pronto para aplicações reais.

Com esse conhecimento, você está preparado para criar aplicações de IA que vão além do trivial, integrando dados próprios, estruturados ou não, e oferecendo respostas fundamentadas, seguras e contextualizadas para os usuários.

---

### Teste seu Conhecimento

1. O que significa a sigla RAG?
    a) Random Access Generation
    b) Retrieval-Augmented Generation
    c) Real-time Augmented Grammar
    d) Recursive Agent Generation

2. Qual é a principal função de um banco de dados vetorial como o ChromaDB em um pipeline RAG?
    a) Armazenar o histórico da conversa.
    b) Executar o modelo de linguagem.
    c) Armazenar e buscar embeddings de texto por similaridade.
    d) Dividir documentos em chunks.

3. O que é "chunking" e por que é importante?
    a) O processo de converter texto em embeddings.
    b) O processo de quebrar textos longos em pedaços menores para facilitar a recuperação e respeitar o limite de contexto do LLM.
    c) O processo de enviar um prompt para o LLM.
    d) O processo de avaliar a qualidade da resposta do LLM.

4. Qual o papel dos delimitadores em arquivos Markdown e CSV no contexto de RAG?
    a) Servem apenas para estilizar o texto.
    b) Permitem dividir o documento em chunks lógicos, facilitando a segmentação e a recuperação de informações.
    c) São ignorados pelo pipeline.
    d) Servem para criptografar o conteúdo.

5. Para que serve a LangChain Expression Language (LCEL)?
    a) Para treinar modelos de linguagem.
    b) Para criar interfaces de usuário para chatbots.
    c) Para compor cadeias (chains) de processamento de forma declarativa e enxuta.
    d) Para definir o estilo de escrita do LLM.

6. Qual das opções abaixo é uma boa prática para produção de pipelines RAG?
    a) Manter o banco vetorial apenas em memória.
    b) Persistir o banco vetorial em disco, trabalhar com múltiplos documentos e enriquecer as respostas com metadados.
    c) Não usar chunking.
    d) Ignorar o contexto do usuário.

**Respostas:**
1. b
2. c
3. b
4. b
5. c
6. b

---

### Projeto Hands-on: Expandindo o Chatbot RAG

Agora é sua vez de aprimorar o projeto que construímos. Tente implementar as seguintes melhorias:

*   **Múltiplos Documentos:** Modifique o código para carregar e processar múltiplos arquivos de uma pasta. (Dica: use um loop e a função `os.listdir()`).
*   **Persistência:** O ChromaDB criado neste exemplo é "efêmero" (em memória). Pesquise na documentação do LangChain e do ChromaDB como torná-lo persistente, salvando os dados em disco para não precisar reprocessar o PDF toda vez. (Dica: use `persist_directory` ao criar o Chroma).
*   **Adicionar Fontes:** Modifique a cadeia RAG para também retornar de qual página do documento a informação foi extraída. (Dica: o retriever retorna objetos `Document` que contêm metadados, incluindo a página).
