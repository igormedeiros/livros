## Capítulo 8: Testes, Debugging e Otimização de Aplicações LangChain

**Neste capítulo, você vai aprender:**

* Como testar aplicações LangChain de forma eficiente, cobrindo unitários, integração e funcionais.
* Técnicas de debugging, tracing e monitoramento com LangSmith e ferramentas nativas do LangChain.
* Estratégias de otimização de desempenho, custo e confiabilidade em pipelines de LLM.
* Estudo de caso prático integrando testes, debugging e tracing.
* Exercícios práticos, tabelas comparativas e fluxogramas para fixação dos conceitos.

---

### 1. Por que Testar e Depurar Aplicações LangChain?

Construir aplicações com LLMs é diferente do desenvolvimento tradicional: as respostas são probabilísticas, o contexto é dinâmico e bugs podem ser sutis. Testes e debugging são essenciais para garantir qualidade, segurança e previsibilidade.

Imagine um chatbot que responde de forma inesperada após uma atualização de prompt. Sem testes automatizados e tracing, encontrar a causa pode ser como procurar uma agulha no palheiro. O LangChain oferece recursos para tornar esse processo transparente e eficiente.

---

### 2. Testes em LangChain: Unitários, Integração e Funcionais

**Ferramentas recomendadas:**
- `pytest` (Python)
- `unittest` (Python)
- LangSmith (para avaliação e tracing)

**Tabela: Tipos de Teste em Aplicações LangChain**

| Tipo         | O que cobre?                | Ferramenta principal | Exemplo prático |
|--------------|----------------------------|---------------------|-----------------|
| Unitário     | Funções isoladas, prompts  | pytest/unittest     | Testar parser   |
| Integração   | Chains, pipelines          | pytest + LangSmith  | Testar chain    |
| Funcional    | Comportamento do app       | LangSmith           | Teste end-to-end|

**Exemplo de Teste Unitário:**

```python
# capitulo_08/exercicio_1/main.py
import pytest
from langchain_core.output_parsers import StrOutputParser

def test_str_output_parser():
    parser = StrOutputParser()
    output = parser.invoke({"content": "Olá, mundo!"})
    assert output == "Olá, mundo!"
```

**Como executar:**
```sh
uv add pytest
pytest capitulo_08/exercicio_1/main.py
```

**Resultado esperado:**
```
.
1 passed in 0.01s
```

---

### 3. Debugging: Logs, Verbose e Inspeção de Chains

O LangChain permite ativar logs detalhados para inspecionar o fluxo de execução:

```python
# capitulo_08/exercicio_2/main.py
from langchain.globals import set_debug, set_verbose

set_debug(True)      # Ativa logs detalhados
set_verbose(True)    # Mostra entradas e saídas legíveis
# ... código da chain ...
```

**Fluxograma textual do ciclo de debugging:**

1. Ativar logs (`set_debug`, `set_verbose`)
2. Executar chain/agent
3. Inspecionar entradas, saídas e erros
4. Corrigir e repetir

**Exemplo de saída de log:**
```
[chain/start] [chain:AgentExecutor] Entering Chain run with input:
{"input": "Quem dirigiu Oppenheimer?"}
[llm/start] [chain:AgentExecutor > llm:ChatOpenAI] Entering LLM run...
[llm/end] ...
```

---

### 4. Tracing e Monitoramento com LangSmith

O LangSmith é a plataforma oficial para tracing, avaliação e observabilidade de aplicações LangChain. Ele permite inspecionar cada passo de uma chain, visualizar erros, latência e até associar feedback do usuário.

**Como habilitar tracing com LangSmith:**

```python
# capitulo_08/exercicio_3/main.py
import os, getpass
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Digite sua LangSmith API key: ")
```

**No terminal:**
```sh
export LANGSMITH_TRACING="true"
export LANGSMITH_API_KEY="<sua_api_key>"
```

**Exemplo prático:**
```python
# capitulo_08/exercicio_4/main.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("Resuma: {texto}")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
chain = prompt | llm

response = chain.invoke({"texto": "LangChain facilita o desenvolvimento de apps com LLMs."})
print(response.content)
```

**Após executar, acesse o painel do LangSmith para visualizar o trace completo.**

---

### 5. Otimização: Desempenho, Custo e Confiabilidade

**Principais estratégias:**
- Reduzir número de chamadas ao LLM (cache, batch)
- Ajustar temperatura e parâmetros do modelo
- Usar memory e retrievers para evitar repetições
- Monitorar latência e custo via tracing

**Tabela: Estratégias de Otimização**

| Estratégia         | Benefício           | Trade-off           |
|--------------------|---------------------|---------------------|
| Cache de respostas | Menos custo         | Pode perder contexto|
| Batch de queries   | Mais rápido         | Respostas menos personalizadas|
| Ajuste de temp.    | Mais previsível     | Menos criatividade  |

---

### 6. Estudo de Caso: Chatbot com Bugs, Testes e Tracing

**Cenário:**
Um chatbot que responde perguntas sobre filmes, mas apresenta bugs de contexto e respostas erradas.

**Passos:**
1. Escrever chain com bug proposital
2. Criar teste unitário para identificar erro
3. Ativar logs e tracing para localizar bug
4. Corrigir e otimizar

**Exemplo de código:**
```python
# capitulo_08/exercicio_5/main.py
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

prompt = ChatPromptTemplate.from_template("Quem dirigiu {filme}?")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
chain = prompt | llm

# Bug: não trata filmes desconhecidos
resposta = chain.invoke({"filme": "Oppenheimer"})
print(resposta.content)
```

**Teste unitário para o bug:**
```python
# capitulo_08/exercicio_6/main.py
import pytest
from capitulo_08.exercicio_5.main import chain

def test_filme_desconhecido():
    resposta = chain.invoke({"filme": "FilmeInexistente"})
    assert "Desculpe" in resposta.content or resposta.content == ""
```

**Como executar:**
```sh
pytest capitulo_08/exercicio_6/main.py
```

**Resultado esperado:**
Teste falha, indicando o bug. Após correção, o teste deve passar.

---

### Hands-on: Exercício 1 — Teste Unitário de Parser
* **Objetivo:** Testar o parser de saída de LLM.
* **Nome do Arquivo:** `capitulo_08/exercicio_1/main.py`
* **Dependências:** `pytest`, `langchain-core`
* **Comando de Instalação:**
```sh
uv add pytest langchain-core
```
**Comando de Execução (Linux/macOS):**
```sh
pytest capitulo_08/exercicio_1/main.py
```
**Comando de Execução (Windows):**
```bat
pytest capitulo_08\exercicio_1\main.py
```
**Saída Esperada (pode variar):**
```
.
1 passed in 0.01s
```
**Troubleshooting Comum:**
* `ModuleNotFoundError`: Verifique se todas as dependências foram instaladas corretamente.
* Erros de sintaxe: Confira se o código está igual ao exemplo.

---

### Hands-on: Exercício 2 — Debugging de Chains
* **Objetivo:** Ativar logs detalhados e inspecionar execução de chains.
* **Nome do Arquivo:** `capitulo_08/exercicio_2/main.py`
* **Dependências:** `langchain`
* **Comando de Instalação:**
```sh
uv add langchain
```
**Comando de Execução (Linux/macOS):**
```sh
python capitulo_08/exercicio_2/main.py
```
**Comando de Execução (Windows):**
```bat
python capitulo_08\exercicio_2\main.py
```
**Saída Esperada (pode variar):**
```
[chain/start] ...
[llm/start] ...
[llm/end] ...
```
**Troubleshooting Comum:**
* `ModuleNotFoundError`: Verifique se todas as dependências foram instaladas corretamente.
* Logs não aparecem: Certifique-se de que `set_debug(True)` e `set_verbose(True)` estão ativados.

---

### Hands-on: Exercício 3 — Tracing com LangSmith
* **Objetivo:** Habilitar tracing e monitorar execução de chains.
* **Nome do Arquivo:** `capitulo_08/exercicio_3/main.py`
* **Dependências:** `langchain`, `langchain-google-genai`
* **Comando de Instalação:**
```sh
uv add langchain langchain-google-genai
```
**Comando de Execução (Linux/macOS):**
```sh
export LANGSMITH_TRACING="true"
export LANGSMITH_API_KEY="<sua_api_key>"
python capitulo_08/exercicio_3/main.py
```
**Comando de Execução (Windows):**
```bat
set LANGSMITH_TRACING=true
set LANGSMITH_API_KEY=<sua_api_key>
python capitulo_08\exercicio_3\main.py
```
**Saída Esperada (pode variar):**
```
Resuma: ...
[Trace disponível no painel LangSmith]
```
**Troubleshooting Comum:**
* `AuthenticationError`: Verifique se a chave de API está correta.
* Trace não aparece: Certifique-se de que as variáveis de ambiente estão setadas.

---

### Hands-on: Exercício 4 — Teste de Bug em Chatbot
* **Objetivo:** Identificar e corrigir bug em chatbot.
* **Nome do Arquivo:** `capitulo_08/exercicio_5/main.py` e `capitulo_08/exercicio_6/main.py`
* **Dependências:** `pytest`, `langchain-core`, `langchain-google-genai`
* **Comando de Instalação:**
```sh
uv add pytest langchain-core langchain-google-genai
```
**Comando de Execução (Linux/macOS):**
```sh
pytest capitulo_08/exercicio_6/main.py
```
**Comando de Execução (Windows):**
```bat
pytest capitulo_08\exercicio_6\main.py
```
**Saída Esperada (pode variar):**
```
F
1 failed in 0.01s
```
**Troubleshooting Comum:**
* Teste falha: Corrija o bug no chatbot e rode novamente.
* `ModuleNotFoundError`: Verifique se todas as dependências foram instaladas corretamente.

---

### Pontos Chave
* Testes unitários, integração e funcionais garantem qualidade em aplicações LangChain.
* Debugging e tracing são essenciais para identificar e corrigir bugs em pipelines de LLM.
* Otimização de desempenho e custo pode ser feita com cache, batch e ajuste de parâmetros.
* Ferramentas como pytest, LangSmith e logs detalhados são fundamentais para o ciclo de desenvolvimento.

---

### Resumo do Capítulo
Neste capítulo, você aprendeu a testar, debugar, traçar e otimizar aplicações LangChain, usando ferramentas modernas e práticas recomendadas. O domínio desses recursos é essencial para construir aplicações robustas, seguras e eficientes com LLMs.

---

### Teste seu Conhecimento

1. Qual comando ativa logs detalhados no LangChain?
   a) set_verbose(False)
   b) set_debug(True)
   c) set_trace(True)
   d) enable_logs()
2. Como habilitar tracing com LangSmith?
   a) Instalar pytest
   b) Setar LANGSMITH_TRACING e LANGSMITH_API_KEY
   c) Ativar cache de respostas
   d) Usar ConversationBufferMemory
3. Qual estratégia reduz custo em aplicações LLM?
   a) Aumentar temperatura
   b) Cache de respostas
   c) Ignorar logs
   d) Usar apenas testes unitários
4. O que diferencia um teste unitário de um teste funcional?
   a) Teste unitário cobre funções isoladas, funcional cobre comportamento do app
   b) Teste funcional cobre apenas chains
   c) Ambos são iguais
   d) Teste unitário cobre apenas LLMs
5. Como inspecionar a execução de uma chain passo a passo?
   a) Ativar logs/tracing
   b) Ignorar erros
   c) Usar cache
   d) Executar sem testes

**Respostas:**
1. b
2. b
3. b
4. a
5. a

---

### Projeto Hands-on: Testes, Debugging e Tracing em Chatbot

Coloque em prática os conceitos do capítulo criando um projeto Python com LangChain que implementa um chatbot testável, com testes unitários e funcionais, debugging com logs detalhados e tracing via LangSmith. Documente todos os comandos usados, proteja suas chaves de API com .env e compartilhe o repositório via SSH no GitHub. Experimente rodar o projeto em diferentes versões do Python usando pyenv.
