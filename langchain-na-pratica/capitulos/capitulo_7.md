# Capítulo 7: Técnicas Avançadas: Memória, Feedback e Aprendizado Contínuo

**Neste capítulo, você vai aprender:**

* O papel da memória em agentes de IA e sua analogia com o cérebro humano.
* Tipos de memória em LangChain: ConversationBufferMemory, GenerativeAgentMemory, VectorStore, Knowledge Triples, e ChromaDB.
* Como implementar e testar memória em agentes, com exemplos práticos e instruções de execução.
* Estratégias de feedback e aprendizado contínuo para agentes que evoluem com a experiência.
* Estudo de caso: Assistente de suporte que aprende com interações reais.
* Exercício hands-on para consolidar o aprendizado.

---

### 1. Introdução: Por que Memória é Fundamental para Agentes de IA?

Imagine um agente de IA sem memória: ele responde a cada pergunta como se fosse a primeira vez, sem contexto ou aprendizado. Assim como o cérebro humano, a memória permite que agentes retenham informações, aprendam com experiências passadas e adaptem seu comportamento. Em LangChain, a memória é o que transforma um chatbot simples em um assistente inteligente e evolutivo.

---

### 2. Tipos de Memória em LangChain

| Tipo de Memória              | Descrição                                                                 | Uso Típico                      |
|------------------------------|--------------------------------------------------------------------------|----------------------------------|
| ConversationBufferMemory     | Armazena o histórico da conversa em buffer.                              | Chatbots, FAQ, suporte           |
| GenerativeAgentMemory        | Permite reflexão, auto-resumo e aprendizado contínuo.                    | Agentes autônomos, simulacros    |
| VectorStore (Semantic)       | Busca semântica de memórias usando embeddings.                           | Recuperação de contexto, RAG     |
| ChromaDB                     | Banco de dados vetorial AI-native para busca semântica eficiente.        | RAG, armazenamento escalável     |
| Knowledge Triples            | Estrutura fatos em triplas (sujeito, predicado, objeto).                 | Base de conhecimento estruturada |

**Fluxograma textual:**

Usuário → [Agente] → [Memória (Buffer/Semântica/ChromaDB/Estruturada)] → [Ferramentas/Respostas]

---

### 2.1 Introdução ao ChromaDB

O ChromaDB é um banco de dados vetorial open-source, projetado para armazenar e buscar embeddings de forma eficiente. Ele é amplamente utilizado em aplicações de IA para recuperação de contexto, RAG (Retrieval-Augmented Generation) e armazenamento escalável de memórias semânticas.

**Vantagens:**
- Busca rápida e eficiente de vetores.
- Suporte nativo a LangChain.
- Fácil integração com modelos de embeddings.

---

### 3. Implementação Prática: Memória em Ação

#### 3.1 ConversationBufferMemory

**Instalação dos pacotes:**
```sh
uv add langchain langchain-openai python-dotenv
```

**Exemplo de código:**
```python
# capitulo_07/exercicio_1/main.py
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage

model = ChatOpenAI(temperature=0)

@tool
def get_user_age(name: str) -> str:
    """Retorna a idade do usuário (exemplo didático)."""
    if "bob" in name.lower():
        return "42 anos"
    return "41 anos"

tools = [get_user_age]
prompt = ChatPromptTemplate.from_messages([
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent = create_tool_calling_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory)

# Primeira interação
print(agent_executor.invoke({"input": "Oi! Meu nome é Bob, qual minha idade?"}))
# Segunda interação (memória)
print(agent_executor.invoke({"input": "Você lembra meu nome?"}))
```

**Execução:**
```sh
python capitulo_07/exercicio_1/main.py
```
**Resultado esperado:**
```
{'output': '42 anos'}
{'output': 'Seu nome é Bob.'}
```
**Troubleshooting Comum:**
* `ModuleNotFoundError`: Verifique se todas as dependências foram instaladas corretamente.
* Problemas de permissão: Verifique se o arquivo está no diretório correto.

---

#### 3.2 GenerativeAgentMemory

**Instalação dos pacotes:**
```sh
uv add langchain
```

**Exemplo de código:**
```python
# capitulo_07/exercicio_2/main.py
from langchain.experimental.generative_agents import GenerativeAgent, GenerativeAgentMemory
from datetime import datetime, timedelta

memory = GenerativeAgentMemory(reflection_threshold=8)
agent = GenerativeAgent(
    name="Tommie",
    age=25,
    traits="ansioso, gosta de design, comunicativo",
    status="procurando emprego",
    memory=memory,
)

observations = [
    "Tommie lembra do cachorro Bruno de infância",
    "Tommie está cansado após dirigir",
    "Viu a nova casa",
    "Os vizinhos têm um gato",
    "A rua é barulhenta à noite",
    "Tommie está com fome",
    "Tommie tenta descansar."
]
for obs in observations:
    agent.memory.add_memory(obs)

print(agent.get_summary(force_refresh=True))
```

**Execução:**
```sh
python capitulo_07/exercicio_2/main.py
```
**Resultado esperado:**
```
Resumo do agente: Tommie é ansioso, gosta de design, comunicativo, está cansado e sente falta do cachorro Bruno.
```
**Troubleshooting Comum:**
* `ModuleNotFoundError`: Verifique se todas as dependências foram instaladas corretamente.
* Erros de sintaxe: Confira se o código está igual ao exemplo.

---

#### 3.3 VectorStore: Memória Semântica

**Instalação dos pacotes:**
```sh
uv add langchain langchain-openai faiss-cpu
```

**Exemplo de código:**
```python
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
```

**Execução:**
```sh
python capitulo_07/exercicio_3/main.py
```
**Resultado esperado:**
```
O usuário gosta de pizza.
```
**Troubleshooting Comum:**
* `ModuleNotFoundError`: Verifique se todas as dependências foram instaladas corretamente.
* Erros de importação: Confira se os pacotes estão instalados.

---

#### 3.4 ChromaDB: Memória Vetorial AI-native

**Instalação dos pacotes:**
```sh
uv add chromadb langchain langchain-openai
```

**Exemplo de código:**
```python
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
```

**Execução:**
```sh
python capitulo_07/exercicio_4/main.py
```
**Resultado esperado:**
```
O usuário gosta de pizza.
```
**Troubleshooting Comum:**
* `ModuleNotFoundError`: Verifique se todas as dependências foram instaladas corretamente.
* Erros de importação: Confira se os pacotes estão instalados.

---

#### 3.5 Knowledge Triples: Memória Estruturada

**Exemplo de código:**
```python
# capitulo_07/exercicio_5/main.py
from typing_extensions import TypedDict

class KnowledgeTriple(TypedDict):
    subject: str
    predicate: str
    object: str

triples = [
    KnowledgeTriple(subject="João", predicate="gosta de", object="pizza"),
    KnowledgeTriple(subject="Maria", predicate="mora em", object="São Paulo"),
]
for triple in triples:
    print(f"{triple['subject']} {triple['predicate']} {triple['object']}")
```

**Execução:**
```sh
python capitulo_07/exercicio_5/main.py
```
**Resultado esperado:**
```
João gosta de pizza
Maria mora em São Paulo
```
**Troubleshooting Comum:**
* `ModuleNotFoundError`: Verifique se todas as dependências foram instaladas corretamente.

---

#### 3.6 Assistente de Suporte Evolutivo

**Exemplo de código:**
```python
# capitulo_07/exercicio_6/main.py
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

model = ChatOpenAI(temperature=0)

@tool
def registrar_feedback(feedback: str) -> str:
    """Registra feedback do usuário na memória."""
    return f"Feedback registrado: {feedback}"

tools = [registrar_feedback]
prompt = ChatPromptTemplate.from_messages([
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent = create_tool_calling_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory)

print(agent_executor.invoke({"input": "Preciso de ajuda com minha conta."}))
print(agent_executor.invoke({"input": "O atendimento foi ótimo!"}))
print(agent_executor.invoke({"input": "Qual foi meu feedback anterior?"}))
```

**Execução:**
```sh
python capitulo_07/exercicio_6/main.py
```
**Resultado esperado:**
```
Feedback registrado: O atendimento foi ótimo!
Qual foi meu feedback anterior? O atendimento foi ótimo!
```
**Troubleshooting Comum:**
* `ModuleNotFoundError`: Verifique se todas as dependências foram instaladas corretamente.
* Problemas de permissão: Verifique se o arquivo está no diretório correto.

---

### 4. Feedback e Aprendizado Contínuo

A memória sozinha não basta: agentes avançados precisam refletir sobre suas ações, receber feedback e adaptar seu comportamento. Em LangChain, isso pode ser feito com mecanismos de reflexão (reflection_threshold), auto-resumo e atualização de memórias.

**Fluxograma textual:**

Usuário → [Agente] → [Memória] → [Reflexão/Feedback] → [Aprimoramento do agente]

---

### 5. Estudo de Caso: Assistente de Suporte Evolutivo

Imagine um assistente de suporte que aprende com cada interação, ajustando suas respostas e memórias conforme o feedback do usuário.

**Exemplo de código:**
```python
# capitulo_07/exercicio_6/main.py
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

model = ChatOpenAI(temperature=0)

@tool
def registrar_feedback(feedback: str) -> str:
    """Registra feedback do usuário na memória."""
    return f"Feedback registrado: {feedback}"

tools = [registrar_feedback]
prompt = ChatPromptTemplate.from_messages([
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent = create_tool_calling_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory)

print(agent_executor.invoke({"input": "Preciso de ajuda com minha conta."}))
print(agent_executor.invoke({"input": "O atendimento foi ótimo!"}))
print(agent_executor.invoke({"input": "Qual foi meu feedback anterior?"}))
```

---

### Hands-on: Exercício — Memória em Agentes LangChain

#### Exercício 1: ConversationBufferMemory
* **Objetivo:** Demonstrar memória de conversação em agentes.
* **Nome do Arquivo:** `capitulo_07/exercicio_1/main.py`
* **Dependências:** `langchain`, `langchain-openai`, `python-dotenv`
* **Comando de Instalação:**
```sh
uv add langchain langchain-openai python-dotenv
```

---

#### Exercício 2: GenerativeAgentMemory
* **Objetivo:** Demonstrar memória reflexiva e auto-resumo.
* **Nome do Arquivo:** `capitulo_07/exercicio_2/main.py`
* **Dependências:** `langchain`
* **Comando de Instalação:**
```sh
uv add langchain
```

---

#### Exercício 3: VectorStore (Memória Semântica)
* **Objetivo:** Demonstrar busca semântica de memórias.
* **Nome do Arquivo:** `capitulo_07/exercicio_3/main.py`
* **Dependências:** `langchain`, `langchain-openai`, `faiss-cpu`
* **Comando de Instalação:**
```sh
uv add langchain langchain-openai faiss-cpu
```

---

#### Exercício 4: ChromaDB (Memória Vetorial AI-native)
* **Objetivo:** Demonstrar busca semântica usando ChromaDB.
* **Nome do Arquivo:** `capitulo_07/exercicio_4/main.py`
* **Dependências:** `chromadb`, `langchain`, `langchain-openai`
* **Comando de Instalação:**
```sh
uv add chromadb langchain langchain-openai
```
**Comando de Execução (Linux/macOS):**
```sh
python capitulo_07/chromadb_memory.py
```
**Comando de Execução (Windows):**
```bat
python capitulo_07\chromadb_memory.py
```
**Saída Esperada (pode variar):**
```
O usuário gosta de pizza.
```
**Troubleshooting Comum:**
* `ModuleNotFoundError`: Verifique se todas as dependências foram instaladas corretamente.
* Erros de importação: Confira se os pacotes estão instalados.

---

#### Exercício 5: Knowledge Triples
* **Objetivo:** Demonstrar memória estruturada com triplas.
* **Nome do Arquivo:** `capitulo_07/exercicio_5/main.py`
* **Dependências:** `typing_extensions`
* **Comando de Instalação:**
```sh
uv add typing_extensions
```

---

#### Exercício 6: Assistente de Suporte Evolutivo
* **Objetivo:** Demonstrar agente que aprende com feedback do usuário.
* **Nome do Arquivo:** `capitulo_07/exercicio_6/main.py`
* **Dependências:** `langchain`, `langchain-openai`, `python-dotenv`
* **Comando de Instalação:**
```sh
uv add langchain langchain-openai python-dotenv
```

---

### Pontos Chave
* Memória transforma agentes simples em assistentes inteligentes e adaptativos.
* LangChain oferece múltiplos tipos de memória: buffer, semântica, reflexiva, estruturada e ChromaDB.
* Feedback e reflexão permitem aprendizado contínuo dos agentes.
* Exercícios práticos mostram como implementar e testar cada tipo de memória.

---

### Resumo do Capítulo
Neste capítulo, você explorou técnicas avançadas de memória, feedback e aprendizado contínuo em agentes de IA com LangChain. Aprendeu a implementar diferentes tipos de memória, testar agentes evolutivos e consolidar o conhecimento com exercícios práticos.

---

### Teste seu Conhecimento

1. Qual tipo de memória permite busca semântica de informações?
   a) ConversationBufferMemory
   b) VectorStore
   c) ChromaDB
   d) Knowledge Triples
2. O que o parâmetro reflection_threshold controla em GenerativeAgentMemory?
   a) Quantidade de memória armazenada
   b) Quando o agente reflete e aprende
   c) O tipo de embedding usado
   d) O número de ferramentas disponíveis
3. Knowledge Triples são usadas para:
   a) Armazenar histórico linear de conversa
   b) Estruturar fatos em sujeito, predicado e objeto
   c) Buscar contexto semântico
   d) Gerar auto-resumo do agente
4. Para registrar feedback do usuário em um agente, você deve:
   a) Usar ConversationBufferMemory
   b) Implementar uma ferramenta customizada
   c) Utilizar VectorStore ou ChromaDB
   d) Adicionar triplas manualmente
5. Um trade-off entre memória buffer e semântica é:
   a) Buffer é mais poderoso, semântica é mais simples
   b) Buffer é simples e rápido, semântica é mais complexa e poderosa
   c) Semântica não permite busca, buffer permite
   d) Ambos são iguais em escalabilidade

**Respostas:**
1. b, c
2. b
3. b
4. b
5. b

---

### Projeto Hands-on: Agente Evolutivo com Memória e Feedback

Coloque em prática os conceitos do capítulo criando um agente Python com LangChain que utiliza memória semântica (ChromaDB) e registra feedback do usuário. O agente deve adaptar suas respostas conforme o histórico e feedback recebido. Documente todos os comandos usados, proteja suas chaves de API com .env e compartilhe o repositório via SSH no GitHub. Experimente rodar o projeto em diferentes versões do Python usando pyenv.