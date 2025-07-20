## Capítulo 4: Construção de Pipelines: Da SequentialChain à LCEL

**Neste capítulo, você vai aprender:**

* O papel dos pipelines em aplicações reais (chatbots, RAG, automação).
* A evolução das chains no LangChain: do imperativo ao declarativo.
* Como construir pipelines com LCEL, RunnablePassthrough, RunnableParallel e RunnableLambda.
* Diferenças entre abordagens clássicas (LLMChain/SequentialChain) e modernas (LCEL).
* Exercícios práticos para criar pipelines eficientes, paralelos, com streaming e tracing.
* Troubleshooting, checklist de construção, teste de conhecimento e projeto hands-on.

---

### A Evolução das Chains: Do Imperativo ao Declarativo

Nos primeiros dias do LangChain, a forma de construir fluxos de trabalho era através de classes como LLMChain e SequentialChain. Essa abordagem, embora funcional, era o que chamamos de **imperativa**: você instanciava objetos e os conectava de forma mais verbosa, o que tornava o código mais difícil de ler e manter. Era como dar instruções passo a passo para montar um móvel, detalhando cada parafuso.

O time do LangChain percebeu que poderia haver uma maneira melhor, mais intuitiva e mais poderosa. Uma maneira que fosse **declarativa**, onde você simplesmente descreve o fluxo de dados — como um diagrama de montagem — e o framework se encarrega da execução otimizada. LCEL permite propagação automática de configurações (RunnableConfig), facilitando logging, tracing e debugging em pipelines complexos.

Essa percepção deu origem à **LangChain Expression Language (LCEL)**, lançada em agosto de 2023. A LCEL é, sem dúvida, uma das inovações mais importantes do framework e é a maneira moderna e recomendada de construir qualquer tipo de pipeline.

Neste capítulo, vamos fazer uma viagem no tempo. Primeiro, vamos construir uma chain "à moda antiga" para entender as dores que a LCEL veio resolver. Depois, vamos mergulhar de cabeça na LCEL e ver como ela torna nossa vida muito mais fácil.

---

### O Jeito Clássico: LLMChain e SequentialChain (OBSOLETO)

Para entendermos o salto que a LCEL representa, vamos primeiro ver como as coisas eram feitas. É importante notar que as classes `LLMChain` e `SequentialChain` são consideradas **legadas** e **deprecadas** na versão 0.2+ do LangChain. Elas são apresentadas aqui apenas para fins de contexto histórico e para ilustrar os problemas que a LCEL veio resolver. **Não as utilize em novos projetos.**

A `LLMChain` era o bloco de construção mais básico: um prompt, um LLM e uma saída.

```python
# O jeito antigo com LLMChain (OBSOLETO)
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
prompt = PromptTemplate.from_template("Qual a capital de {pais}?")

# Criando a LLMChain
chain = LLMChain(llm=llm, prompt=prompt)
# print(chain.run("França")) # .run() era o método de invocação
```

Agora, e se quiséssemos fazer aquilo que discutimos no Capítulo 1: gerar uma pergunta e depois respondê-la? Precisávamos da `SequentialChain`.

**Observação:** O uso de APIs obsoletas pode dificultar manutenção e escalabilidade. Prefira LCEL para novos projetos.

**Exercício Prático: Chain Sequencial (O Jeito Antigo - OBSOLETO)**

*   **Objetivo:** Demonstrar como as chains eram construídas antes da LCEL usando LLMChain e SequentialChain. Este exemplo é **apenas para fins educacionais** e não deve ser replicado em código de produção.
*   **Nome do Arquivo:** `exercicios/capitulo_04/exercicio_1/main.py`
*   **Dependências:** `langchain`, `langchain-google-genai`, `python-dotenv`
*   **Comando de Instalação:** `uv add langchain langchain-google-genai python-dotenv`

```python
# exercicios/capitulo_04/exercicio_1/main.py (OBSOLETO)
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
```

**Comando de Execução (Linux/macOS):**
```sh
# Dê permissão de execução ao script
chmod +x exercicios/capitulo_04/exercicio_1/run.sh

# Execute o exercício
./exercicios/capitulo_04/exercicio_1/run.sh
```
**Comando de Execução (Windows):**
```bat
REM Execute o exercício no Windows
exercicios\capitulo_04\exercicio_1\run.bat
```
**Saída Esperada (pode variar):**
Resultado final com pergunta gerada e resposta elaborada sobre o tópico informado.

**Troubleshooting Comum:**
* `DeprecationWarning`: Aviso esperado ao usar classes legadas.
* `AuthenticationError` ou `GOOGLE_API_KEY` não configurada: Verifique o arquivo `.env`.
* Erros de Conexão: Verifique rede ou limites de uso da API.

---

### Por que usar LCEL?

A LCEL resolve muitos dos problemas das classes legadas, como LLMChain e SequentialChain, que são consideradas obsoletas na versão 0.2+ do LangChain. Com LCEL, você constrói pipelines de forma **declarativa**, focando no fluxo de dados e não na implementação detalhada de cada etapa. Configurações como logging e tracing são propagadas automaticamente.

A abordagem moderna da LCEL permite criar pipelines claros, concisos e escaláveis. Você descreve o que deseja fazer e o LangChain executa de forma otimizada, facilitando a leitura, manutenção e evolução do código.

Além da clareza, a LCEL traz ganhos de performance: é otimizada para execução eficiente, suporta paralelismo nativo (com `RunnableParallel`), streaming de respostas e integração direta com ferramentas como LangSmith. Isso permite lidar com grandes volumes de dados e operações complexas sem comprometer a velocidade ou a robustez.

---

### Hands-on: Exercício 2 — LCEL na Prática: Sinopse de Filme

A melhor forma de entender a LCEL é colocando a mão na massa. Vamos passar por uma série de exercícios que demonstram seus principais recursos.

**Dica:** Funções Python são automaticamente convertidas em `RunnableLambda` ao usar o operador `|`. Dicionários são convertidos em `RunnableParallel` para execução concorrente.

**Exemplo de streaming:**
```python
for chunk in chain.stream({"genero": "Comédia"}):
    print(chunk, end="|")
```

**Exercício 1: A Chain Mais Simples (com LCEL)**

* **Objetivo:** Criar uma chain básica que gera uma sinopse de filme a partir de um gênero.

```python
# exercicios/capitulo_04/exercicio_2/main.py  
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
```

**Comando de Execução (Linux/macOS):**
```sh
# Dê permissão de execução ao script
chmod +x exercicios/capitulo_04/exercicio_2/run.sh

# Execute o exercício
./exercicios/capitulo_04/exercicio_2/run.sh
```
**Comando de Execução (Windows):**
```bat
REM Execute o exercício no Windows
exercicios\capitulo_04\exercicio_2\run.bat
```
**Saída Esperada (pode variar):**
Sinopse de filme gerada para o gênero informado.

**Troubleshooting Comum:**
* `AuthenticationError` ou `GOOGLE_API_KEY` não configurada.
* `ValidationError` ou erros de schema.
* Erros de Conexão.
* Saída inesperada do LLM: ajuste o prompt ou a temperature.

---

### Hands-on: Exercício 3 — Passando Dados com RunnablePassthrough

**Dica:** Use `RunnablePassthrough.assign` para empacotar outputs em dicionários, útil para debugging e integração.

**Exercício 2: Passando Dados com RunnablePassthrough**

* **Objetivo:** Criar uma chain que gera uma pergunta sobre um tópico e depois responde a essa pergunta, usando o tópico original na resposta final.

```python
# exercicios/capitulo_04/exercicio_3/main.py  
from dotenv import load_dotenv  
from langchain_core.prompts import ChatPromptTemplate  
from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain_core.output_parsers import StrOutputParser  
from langchain_core.runnables import RunnablePassthrough

load_dotenv()  
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")  
parser = StrOutputParser()

prompt_pergunta = ChatPromptTemplate.from_template("Gere uma pergunta interessante sobre {topico}.")  
prompt_resposta = ChatPromptTemplate.from_template(  
    "Responda a pergunta: {pergunta}. Contexto original do tópico: {topico}"  
)

chain_pergunta = prompt_pergunta | model | parser

chain_completa = (  
    {"pergunta": chain_pergunta, "topico": RunnablePassthrough()}  
    | prompt_resposta  
    | model  
    | parser  
)

print(chain_completa.invoke("a filosofia estoica"))
```

**Comando de Execução (Linux/macOS):**
```sh
# Dê permissão de execução ao script
chmod +x exercicios/capitulo_04/exercicio_3/run.sh

# Execute o exercício
./exercicios/capitulo_04/exercicio_3/run.sh
```
**Comando de Execução (Windows):**
```bat
REM Execute o exercício no Windows
exercicios\capitulo_04\exercicio_3\run.bat
```
**Saída Esperada (pode variar):**
Pergunta gerada sobre o tópico e resposta contextualizada.

**Troubleshooting Comum:**
* `AuthenticationError` ou `GOOGLE_API_KEY` não configurada.
* `ValidationError` ou erros de schema.
* Erros de Conexão.
* Saída inesperada do LLM: ajuste o prompt ou a temperature.

---

### Hands-on: Exercício 4 — Execução Paralela com RunnableParallel

**Dica:** O uso de `RunnableParallel` permite que cada etapa receba o mesmo input e execute em paralelo, retornando um dicionário com os resultados.

**Exercício 3: Execução Paralela com RunnableParallel**

* **Objetivo:** Para um determinado país, buscar em paralelo sua capital, sua população e uma curiosidade.

```python
# exercicios/capitulo_04/exercicio_4/main.py  
from dotenv import load_dotenv  
from langchain_core.prompts import ChatPromptTemplate  
from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain_core.output_parsers import StrOutputParser  
from langchain_core.runnables import RunnableParallel

load_dotenv()  
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")  
parser = StrOutputParser()

chain_capital = ChatPromptTemplate.from_template("Qual é a capital de {pais}?") | model | parser  
chain_populacao = ChatPromptTemplate.from_template("Qual é a população aproximada de {pais}?") | model | parser  
chain_curiosidade = ChatPromptTemplate.from_template("Conte uma curiosidade sobre {pais}.") | model | parser

mapa_paralelo = RunnableParallel(  
    capital=chain_capital,  
    populacao=chain_populacao,  
    curiosidade=chain_curiosidade  
)

resultado = mapa_paralelo.invoke({"pais": "Egito"})  
print(resultado)
```

**Comando de Execução (Linux/macOS):**
```sh
# Dê permissão de execução ao script
chmod +x exercicios/capitulo_04/exercicio_4/run.sh

# Execute o exercício
./exercicios/capitulo_04/exercicio_4/run.sh
```
**Comando de Execução (Windows):**
```bat
REM Execute o exercício no Windows
exercicios\capitulo_04\exercicio_4\run.bat
```
**Saída Esperada (pode variar):**
Retorno paralelo: capital, população e curiosidade sobre o país informado.

**Troubleshooting Comum:**
* `AuthenticationError` ou `GOOGLE_API_KEY` não configurada.
* `ValidationError` ou erros de schema.
* Erros de Conexão.
* Saída inesperada do LLM: ajuste o prompt ou a temperature.

---

### Troubleshooting Comum
* `DeprecationWarning`: Aviso esperado ao usar classes legadas.
* `AuthenticationError` ou `GOOGLE_API_KEY` não configurada: Verifique o arquivo `.env`.
* Erros de Conexão: Verifique rede ou limites de uso da API.
* Ative tracing com LangSmith usando `LANGSMITH_TRACING=true`.
* Proteja chaves de API com Pydantic `SecretStr` ou arquivos `.env`.
* Implemente testes automatizados para chains customizadas.

---

### Pontos Chave
* LCEL é a abordagem moderna e recomendada para pipelines no LangChain.
* Streaming, paralelismo e integração com LangSmith são nativos na LCEL.
* Chains legadas são úteis para contexto histórico, mas não devem ser usadas em produção.
* Exercícios práticos demonstram as vantagens da LCEL em clareza, modularidade e performance.
* O uso de `RunnableParallel` e `RunnablePassthrough` facilita a modularização e reuso de componentes.

---

### Resumo do Capítulo
Neste capítulo, você aprendeu a diferença entre pipelines imperativos e declarativos, explorou a LCEL e suas vantagens, e colocou em prática a construção de chains modernas, paralelas e eficientes. Explore integrações avançadas como LangGraph e LangServe para projetos de maior escala.

---

### Teste seu Conhecimento
1. Qual é a principal vantagem da LCEL em relação às chains clássicas?
   a) Permite integração com LangSmith e streaming nativo.
   b) É mais difícil de usar.
   c) Não suporta paralelismo.
   d) Só funciona com LLMChain.
2. O que o RunnablePassthrough permite em uma chain LCEL?
   a) Executar múltiplos modelos em paralelo.
   b) Passar dados do input diretamente para etapas subsequentes.
   c) Validar a saída do modelo.
   d) Gerar prompts automaticamente.
3. Qual componente LCEL permite executar múltiplas chains ao mesmo tempo?
   a) RunnableLambda
   b) RunnableParallel
   c) RunnablePassthrough
   d) SequentialChain
4. Qual é o método recomendado para obter respostas token a token em LCEL?
   a) .run()
   b) .stream()
   c) .ainvoke()
   d) .output()
5. Por que as chains legadas como LLMChain e SequentialChain são consideradas obsoletas?
   a) Não funcionam com Python 3.12.
   b) Não suportam streaming, paralelismo e integração moderna.
   c) São mais rápidas que LCEL.
   d) Foram removidas do LangChain.
6. Como ativar tracing para inspeção de pipelines?
   a) Definindo LANGSMITH_TRACING=true no ambiente.
   b) Usando apenas SequentialChain.
   c) Removendo o arquivo .env.
   d) Desabilitando logs.

**Respostas:**
1. a
2. b
3. b
4. b
5. b
6. a

---

### Projeto Hands-on: Pipeline Inteligente

Coloque em prática os conceitos do capítulo criando um pipeline inteligente com LCEL. Implemente etapas paralelas, streaming de respostas e integração com LangSmith. Siga a estrutura sugerida:

- Estrutura de diretórios recomendada para projetos LCEL.
- Checklist de boas práticas: modularização, logging, versionamento, testes.
- Fluxograma do pipeline.
- Dicas para integração com APIs externas e testes automatizados.
- Orientação para uso de streaming e paralelismo.
- Passos para ativar tracing com LangSmith e compartilhar logs via GitHub.
- Proteja chaves de API com .env.
- Documente comandos de execução e compartilhe o projeto via GitHub usando SSH.

---