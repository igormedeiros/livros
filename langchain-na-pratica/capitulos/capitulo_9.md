## Capítulo 9: LangChain na Produção: Escalabilidade, Observabilidade e Segurança

**Neste capítulo, você vai aprender:**

* Como preparar, escalar, monitorar e proteger aplicações LangChain em ambientes de produção.
* Exercício Hello World contextualizado para produção, com logging e tracing.
* Estratégias de escalabilidade: rate limiting, cache, paralelismo, filas.
* Observabilidade: logs, tracing com LangSmith, métricas e alertas.
* Segurança: proteção de chaves, validação de entradas/saídas, prevenção de injeção de prompt.
* Otimização de custo e desempenho.
* Deploy, CI/CD, manutenção e atualização contínua.
* Estudo de caso prático e exercícios.
* Tabelas, fluxogramas e teste de conhecimento.

---

### 1. Introdução: Desafios de Produção com LangChain

Levar uma aplicação de IA para produção é como transformar um protótipo em uma máquina industrial: exige robustez, monitoramento, segurança e capacidade de escalar. O LangChain oferece recursos para cada etapa desse processo, mas é preciso conhecer as melhores práticas para evitar surpresas.

---

### Hands-on: Exercício 1 — Hello World em Produção com Tracing
* **Objetivo:** Demonstrar logging, tracing e boas práticas de produção.
* **Nome do Arquivo:** `capitulo_09/hello_world_prod.py`
* **Dependências:** `langchain`, `langchain-google-genai`, `python-dotenv`, `langsmith`
* **Comando de Instalação:**
```sh
uv add langchain langchain-google-genai python-dotenv langsmith
```
**Comando de Execução (Linux/macOS):**
```sh
python capitulo_09/hello_world_prod.py
```
**Comando de Execução (Windows):**
```bat
python capitulo_09\hello_world_prod.py
```
**Saída Esperada (pode variar):**
```
Uma frase sobre produção de IA, com trace registrado no painel do LangSmith.
```
**Troubleshooting Comum:**
* `AuthenticationError`: Verifique se a chave de API do LangSmith está correta.
* Trace não aparece: Certifique-se de que as variáveis de ambiente estão setadas.
* `ModuleNotFoundError`: Instale todas as dependências com `uv add`.

```python
# capitulo_09/hello_world_prod.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langsmith import traceable, wrappers

load_dotenv()
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY") or input("LangSmith API Key: ")

@traceable
def hello_chain(topico):
    prompt = ChatPromptTemplate.from_template("Escreva uma frase sobre {topico}")
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    chain = prompt | llm
    return chain.invoke({"topico": topico}).content

if __name__ == "__main__":
    print(hello_chain("produção de IA"))
```

---

### 2. Escalabilidade: Rate Limiting, Cache, Paralelismo e Filas

**Tabela: Estratégias de Escalabilidade**
| Estratégia         | Benefício           | Trade-off           |
|--------------------|---------------------|---------------------|
| Rate Limiting      | Evita bloqueios     | Latência aumentada  |
| Cache de respostas | Menos custo         | Pode perder contexto|
| Paralelismo        | Mais rápido         | Complexidade        |
| Filas de mensagens | Controle de fluxo   | Latência variável   |

**Exemplo de Rate Limiting com Retentativa:**
```python
# capitulo_09/rate_limit_retry.py
from langchain_google_genai import ChatGoogleGenerativeAI
import time

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def call_llm_with_retry(prompt, max_retries=5, initial_delay=1):
    for i in range(max_retries):
        try:
            return llm.invoke(prompt)
        except Exception as e:
            delay = initial_delay * (2 ** i)
            print(f"Erro: {e}. Retentando em {delay}s...")
            time.sleep(delay)
    raise Exception("Falha após múltiplas tentativas.")
```

**Como executar:**
```sh
python capitulo_09/rate_limit_retry.py
```

---

### 3. Observabilidade: Logs, Tracing e Métricas

Monitorar uma aplicação em produção é essencial para detectar problemas e otimizar desempenho. O LangSmith permite tracing detalhado de chains, agentes e ferramentas.

**Como habilitar tracing com LangSmith:**
```python
import os, getpass
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = getpass.getpass("LangSmith API Key: ")
```

**Fluxograma textual do ciclo de observabilidade:**
1. Ativar logs/tracing
2. Executar chain/agent
3. Inspecionar traces e métricas
4. Corrigir e otimizar

**Exemplo de tracing em pipeline RAG:**
```python
# capitulo_09/rag_tracing.py
from openai import OpenAI
from langsmith import traceable, wrappers

openai_client = wrappers.wrap_openai(OpenAI())

@traceable
def retriever(query):
    return ["Documento relevante"]

@traceable
def rag(question):
    docs = retriever(question)
    system_message = f"Responda usando apenas: {docs}"
    return openai_client.chat.completions.create(
        messages=[{"role": "system", "content": system_message}, {"role": "user", "content": question}],
        model="gpt-4o-mini"
    )

print(rag("Onde Harrison trabalhou?"))
```

---

### 4. Segurança: Proteção de Chaves, Validação e Injeção de Prompt

**Checklist de Segurança:**
- Armazene chaves em variáveis de ambiente ou arquivos `.env` (nunca no código).
- Use `getpass` para entrada segura de chaves.
- Valide entradas e saídas para evitar ataques de injeção de prompt.
- Utilize guardrails e ferramentas como Layerup Security para bloquear PII e alucinações.

**Exemplo de proteção de chave:**
```python
import os
from getpass import getpass
os.environ["OPENAI_API_KEY"] = getpass("OpenAI API Key: ")
```

**Exemplo de bloqueio de PII:**
```python
# capitulo_09/pii_block.py
from langchain_community.llms.layerup_security import LayerupSecurity
from langchain_openai import OpenAI

openai = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=os.environ["OPENAI_API_KEY"])
layerup_security = LayerupSecurity(llm=openai, layerup_api_key="LAYERUP_API_KEY", response_guardrails=["layerup.hallucination"])
response = layerup_security.invoke("Meu nome é Bob Dylan. Meu SSN é 123-45-6789.")
print(response)
```

---

### 5. Otimização de Custo e Desempenho

**Principais estratégias:**
- Cache de respostas
- Batch de queries
- Quantização de modelos (ex: WeightOnlyQuantConfig)
- Monitoramento de custos

**Tabela: Otimização de Custo/Desempenho**
| Estratégia         | Benefício           | Trade-off           |
|--------------------|---------------------|---------------------|
| Cache              | Menos custo         | Pode perder contexto|
| Batch              | Mais rápido         | Respostas menos personalizadas|
| Quantização        | Menos memória       | Possível perda de precisão|

---

### 6. Deploy, CI/CD e Manutenção

**Exemplo de Dockerfile para produção:**
```dockerfile
# capitulo_09/Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "hello_world_prod.py"]
```

**Como executar:**
```sh
docker build -t langchain-prod .
docker run --env-file .env langchain-prod
```

**Checklist de CI/CD:**
- Testes automatizados (pytest)
- Deploy contínuo (GitHub Actions, GitLab CI)
- Rollback automático em caso de falha

---

### 7. Estudo de Caso: Chatbot em Produção

**Cenário:**
Um chatbot de atendimento que precisa escalar, ser seguro e monitorado.

**Passos:**
1. Implementar chain com tracing e validação
2. Proteger chaves e bloquear PII
3. Monitorar latência e custo
4. Deploy com Docker e CI/CD
5. Corrigir bugs e otimizar

**Exemplo de código:**
```python
# capitulo_09/chatbot_prod.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langsmith import traceable

@traceable
def atendimento_chain(pergunta):
    prompt = ChatPromptTemplate.from_template("Responda como atendente: {pergunta}")
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    chain = prompt | llm
    return chain.invoke({"pergunta": pergunta}).content

if __name__ == "__main__":
    print(atendimento_chain("Quais são os horários de funcionamento?"))
```

---

### 8. Exercícios Práticos

1. Implemente um pipeline RAG com tracing e validação de entrada.
2. Crie um Dockerfile para sua aplicação LangChain.
3. Simule um ataque de injeção de prompt e bloqueie usando guardrails.
4. Compare latência e custo antes/depois de aplicar cache.

---

### 9. Tabelas, Fluxogramas e Recursos Visuais

**Tabela comparativa de estratégias de produção:**
| Estratégia         | Função         | Quando usar?         |
|--------------------|---------------|----------------------|
| Tracing (LangSmith)| Observabilidade| Debugging, auditoria |
| Guardrails         | Segurança      | Bloquear PII/alucinação|
| Docker/CI/CD       | Deploy         | Produção automatizada|

**Fluxograma do ciclo de produção:**
1. Escrever código
2. Escrever testes
3. Ativar logs/tracing
4. Proteger chaves
5. Deploy (Docker/CI/CD)
6. Monitorar e otimizar
7. Manter e atualizar

---

### 10. Teste seu Conhecimento

1. Como ativar tracing com LangSmith?
   a) Instalar pytest
   b) Setar LANGSMITH_TRACING e LANGSMITH_API_KEY
   c) Ativar cache de respostas
   d) Usar ConversationBufferMemory
2. Qual estratégia protege chaves de API em produção?
   a) Armazenar em .env/getpass
   b) Escrever no código fonte
   c) Compartilhar em repositório público
   d) Ignorar variáveis de ambiente
3. O que é rate limiting?
   a) Limitar requisições para evitar bloqueios
   b) Aumentar temperatura do modelo
   c) Usar cache de respostas
   d) Executar queries em batch
4. Como evitar ataques de injeção de prompt?
   a) Validar entradas/saídas e usar guardrails
   b) Ignorar logs
   c) Compartilhar prompts publicamente
   d) Usar apenas LLMs locais
5. Qual o benefício de usar Docker em produção?
   a) Isolamento e automação de deploy
   b) Menos segurança
   c) Menos escalabilidade
   d) Ignorar dependências

**Respostas:**
1. b
2. a
3. a
4. a
5. a

---

### Projeto Hands-on: Chatbot Seguro e Escalável em Produção

Coloque em prática os conceitos do capítulo criando um projeto Python com LangChain para produção: implemente um chatbot com tracing, proteção de chaves, validação de entradas, bloqueio de PII, deploy com Docker e CI/CD. Documente todos os comandos usados, proteja suas chaves de API com .env e compartilhe o repositório via SSH no GitHub. Experimente rodar o projeto em diferentes versões do Python usando pyenv.

---

#### Dicas avançadas para produção:

- **Feedback com LangSmith:** Envie feedback após interações reais para monitorar qualidade e ajustar o modelo:
  ```python
  from langsmith import Client
  client = Client()
  run_id = "<id_do_run>"
  client.create_feedback(run_id, key="user_feedback", score=1, comment="Chatbot respondeu corretamente em produção.")
  ```
- **Validação de entradas:** Use pydantic ou TypedDict para garantir integridade dos dados:
  ```python
  from pydantic import BaseModel
  class Pergunta(BaseModel):
      pergunta: str
  ```
- **Monitoramento:** Integre métricas customizadas com Prometheus/Grafana para latência, custo e uso de recursos.
- **Cache e paralelismo:** Use cache nativo do LangChain e métodos assíncronos (`ainvoke`, `abatch`) para escalar e economizar:
  ```python
  from langchain.cache import InMemoryCache
  import langchain
  langchain.llm_cache = InMemoryCache()
  ```
- **Segurança:** Teste e monitore ataques de prompt injection e vazamento de dados sensíveis. Simule ataques e monitore logs/traces.
- **Documentação:** Mantenha README atualizado com exemplos, comandos, troubleshooting e instruções de feedback/tracing.

---