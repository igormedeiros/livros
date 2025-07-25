## Capítulo 5: Desenvolvimento de Agentes Autônomos e Multiagentes

**Neste capítulo, você vai aprender:**

* O papel dos agentes autônomos e multiagentes em aplicações de IA modernas.
* Como construir agentes que tomam decisões dinâmicas usando ferramentas (Tools) e o padrão ReAct.
* Engenharia de contexto, uso de memória e o papel do RAG para ampliar o conhecimento dos agentes.
* Exercício prático de agente de pesquisa com integração de ferramentas externas e adaptação para LangGraph.
* Introdução ao LangGraph para orquestração de sistemas multiagentes complexos.
* Pontos chave, troubleshooting, checklist e teste de conhecimento para consolidar o aprendizado.

---

Seja bem-vindo a um dos territórios mais fascinantes e, admito, mais complexos do LangChain: os agentes. Se o conceito parecer um pouco abstrato ou intimidador no começo, não se preocupe. É um salto conceitual significativo. Pense nisso como aprender a andar de bicicleta depois de só ter usado patinetes. Nos capítulos anteriores, construímos "patinetes": fluxos de trabalho lineares e previsíveis. Agora, vamos dar equilíbrio e autonomia à nossa criação.

O equilíbrio, assim como na bicicleta, vem com a prática. Vamos começar com calma, entender cada peça, e logo você estará pedalando por conta própria, criando sistemas que pensam e agem. Confie no processo, e vamos passo a passo.

### O que é um Agente? O LLM como Cérebro

Até agora, usamos LLMs para executar tarefas bem definidas dentro de um pipeline (uma Chain). O fluxo era fixo. Um agente, por outro lado, vira esse jogo de cabeça para baixo. Em um sistema agêntico, o LLM não é apenas um executor de tarefas, ele é o **cérebro**, o **motor de raciocínio** que decide o que fazer a seguir.

A principal diferença entre uma Chain e um Agente é a **autonomia**. Um agente é um sistema que usa um LLM como seu "motor de raciocínio" para determinar a sequência de ações a serem tomadas. O padrão ReAct (Reason + Act) é implementado nativamente via `create_react_agent` no LangChain e LangGraph, permitindo raciocínio iterativo e uso dinâmico de ferramentas.

* Uma **Chain** segue um caminho predeterminado. Ex: Prompt -> LLM -> Parse. O caminho não muda.  
* Um **Agente** usa o LLM para escolher um caminho dinamicamente a partir de um conjunto de opções disponíveis (as ferramentas). O caminho pode ser diferente a cada execução.

Essa capacidade de tomar decisões em tempo de execução é o que permite que agentes resolvam problemas complexos, interajam com o mundo exterior e executem tarefas que não podem ser roteirizadas de antemão.

Pense na cena icônica de Matrix (1999), onde Morpheus oferece a Neo a pílula azul ou a pílula vermelha. Neo (o usuário) está buscando a verdade. Morpheus (o Agente) é o sistema que, com base em seu "raciocínio" e acesso a "ferramentas" (como o conhecimento da Matrix e a capacidade de manipular programas), decide qual "ação" tomar para guiar Neo. As "ferramentas" são os programas que Morpheus pode usar, e a "Matrix" é o ambiente onde essas ações acontecem. A pílula vermelha, que revela a verdade e dá a Neo a autonomia para ver o mundo como ele realmente é, pode ser comparada à autonomia que damos aos nossos agentes. Eles não apenas seguem instruções, mas "enxergam" o ambiente e tomam decisões para alcançar um objetivo.

Os efeitos inovadores dessa autonomia são visíveis em modelos como o Google vO3, que demonstram capacidades de raciocínio e interação com o ambiente que eram impensáveis há poucos anos.

### Engenharia de Contexto: A Evolução do Prompt

Quando falamos de agentes, especialmente sistemas com múltiplos agentes que colaboram e compartilham informações, a simples "Engenharia de Prompts" evolui para algo mais sofisticado: a **Engenharia de Contexto**. Componentes de memória e checkpointers (ex: `MemorySaver`) permitem que agentes mantenham histórico e colaboratividade, facilitando fluxos multiagentes.

Não se trata mais apenas de criar a instrução perfeita para uma única tarefa. Trata-se de gerenciar e moldar dinamicamente o contexto completo que cada agente recebe. Esse contexto pode incluir:

* O objetivo geral da missão.  
* O histórico da conversa até o momento (memória de curto prazo).  
* Os resultados e observações das ferramentas que já foram executadas.  
* Informações relevantes recuperadas de uma base de conhecimento (memória de longo prazo, ou RAG).  
* Uma "memória compartilhada" ou um "quadro branco" onde outros agentes deixaram notas.

A engenharia de contexto é a arte de garantir que o agente certo receba a informação certa no momento certo, sem sobrecarregá-lo com dados irrelevantes. É um desafio de design crucial para a eficiência de sistemas multiagentes.

### RAG (Retrieval-Augmented Generation): Ampliando o Conhecimento do LLM

Até agora, nossos LLMs operam com o conhecimento que foi "treinado" neles. Mas e se precisarmos que eles respondam a perguntas sobre dados muito específicos, privados ou que mudam constantemente? É aqui que entra o **RAG (Retrieval-Augmented Generation)**, um padrão arquitetural que permite aos LLMs acessar e utilizar informações externas e atualizadas.

Pense no RAG como dar ao seu LLM a capacidade de "consultar livros" antes de responder. O processo segue um fluxo lógico de quatro etapas:

1.  **Consulta (Query):** O usuário faz uma pergunta ou fornece uma entrada ao sistema.
2.  **Recuperação (Retrieval):** Em vez de o LLM tentar responder apenas com seu conhecimento interno, o sistema primeiro "recupera" informações relevantes de uma base de dados externa (como documentos, artigos, bancos de dados, etc.). Essa recuperação é feita buscando por similaridade semântica entre a consulta do usuário e os documentos na base de conhecimento.
3.  **Aumento (Augmentation):** As informações recuperadas são então "aumentadas" (adicionadas) ao prompt original do usuário. Isso cria um prompt mais rico e contextualizado, que é então enviado ao LLM.
4.  **Geração (Generation):** O LLM recebe o prompt aumentado e gera uma resposta que não apenas utiliza seu conhecimento interno, mas também incorpora e se baseia nas informações recuperadas externamente.

O RAG é crucial para construir aplicações de IA que precisam ser factualmente precisas, atualizadas e capazes de operar sobre grandes volumes de dados específicos de um domínio. Ele minimiza as "alucinações" (respostas inventadas) dos LLMs e os torna muito mais úteis em cenários corporativos e de dados sensíveis.

### Componentes de um Agente: Ferramentas e o Executor

Para construir um agente, precisamos de dois componentes principais:

1. **Ferramentas (Tools):** São as ações que o agente pode executar. Uma ferramenta é, essencialmente, uma função Python com uma descrição muito bem escrita. A descrição é crucial, pois é isso que o LLM lê para decidir se e quando deve usar aquela ferramenta. Exemplos de ferramentas:  
   * Uma busca na web.  
   * Uma calculadora.  
   * Uma função que lê um arquivo.  
   * Uma função que consulta uma API.  
   * Uma função que interage com um banco de dados.  
2. **Executor do Agente (Agent Executor):** É o runtime que orquestra o loop de raciocínio do agente. O padrão mais comum, conhecido como **ReAct (Thought \+ Action \+ Observation)**, funciona da seguinte maneira:
   * **Thought (Pensamento):** O LLM recebe o objetivo e a lista de ferramentas disponíveis. Ele então "pensa em voz alta" (*Chain of Thought*) para decidir qual ferramenta usar e com quais argumentos.
   * **Action (Ação):** O executor invoca a ferramenta escolhida com os argumentos definidos pelo LLM.
   * **Observation (Observação):** O resultado da ferramenta é retornado ao LLM como uma "observação".
   * **Repeat (Repetição):** O LLM analisa a observação e decide se a tarefa está concluída ou se precisa de mais um ciclo de Pensamento, Ação e Observação.

Ferramentas são funções Python decoradas ou instâncias de classes Tool, e descrições detalhadas são essenciais para o LLM decidir seu uso. O executor do agente pode ser criado com `create_react_agent` do LangGraph, integrando LLM, ferramentas, prompt e memória.

### Hands-on: Exercício — Agente de Pesquisa Simples

#### O que é a API da Tavily? Como obter e custos

* **Objetivo:** Construir um agente simples que pode usar uma ferramenta de busca para responder a perguntas factuais.
* **Nome do Arquivo:** `exercicios/capitulo_05/exercicio_1/main.py`
* **Dependências:** `langchain`, `langchain-google-genai`, `langchain-tavily`, `python-dotenv`
* **Comando de Instalação:**
```sh
uv add langchain langchain-google-genai langchain-tavily python-dotenv
```
* **Configuração Adicional:** Adicione sua chave de API da Tavily ao arquivo `.env` como `TAVILY_API_KEY`.

A **API da Tavily** é uma ferramenta de busca que permite ao seu agente LangChain pesquisar informações atualizadas na internet, especialmente sobre eventos recentes, pessoas, empresas e fatos que mudam rapidamente. Ela é usada como uma "ferramenta externa" para ampliar o conhecimento do agente além do que está disponível no modelo de linguagem.

- **Para que serve:** Permite que o agente realize buscas em tempo real, trazendo respostas baseadas em fontes confiáveis e atualizadas, reduzindo o risco de respostas desatualizadas ou inventadas.
- **Como obter:** 
   1. Acesse [https://app.tavily.com/](https://app.tavily.com/) e crie uma conta gratuita.
   2. No painel da Tavily, vá em "API Keys" e gere uma nova chave.
   3. Copie a chave e adicione ao seu arquivo `.env` como `TAVILY_API_KEY=suachaveaqui`.
- **Tem custo?**  
   - A Tavily oferece um plano gratuito com limite de buscas mensais (veja detalhes atualizados no site).
   - Para uso mais intenso ou comercial, existem planos pagos com limites maiores e recursos adicionais.

> **Dica:** Sempre proteja sua chave de API e nunca a compartilhe publicamente.


```python
# exercicios/capitulo_05/exercicio_1/main.py

import os  
from dotenv import load_dotenv  
from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain_tavily import TavilySearch
from langchain.agents import AgentExecutor, create_tool_calling_agent  
from langchain_core.prompts import ChatPromptTemplate

# Carregar variáveis de ambiente  
load_dotenv()

# 1. Escolher o LLM que será o cérebro do nosso agente  
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 2\. Definir as ferramentas que o agente pode usar  
search_tool = TavilySearch(
    max_results=2,
    description="Uma ferramenta de busca para encontrar informações na internet sobre eventos atuais, pessoas, lugares ou empresas."
)  
tools = [search_tool]

# 3. Criar o Prompt do Agente  
# Este prompt é um template especial que guia o agente, permitindo que ele "pense" e registre suas ações.  
# Os placeholders {chat_history} e {agent_scratchpad} são cruciais e gerenciados automaticamente pelo AgentExecutor.  
# O {agent_scratchpad} é onde o agente registra seu processo de raciocínio (Thought), as ferramentas que decide usar (Action)  
# e os resultados dessas ações (Observation), formando o ciclo ReAct que vimos anteriormente.  
prompt = ChatPromptTemplate.from_messages([  
    ("system", "Você é um assistente prestativo."),  
    ("placeholder", "{chat_history}"),  
    ("human", "{input}"),  
    ("placeholder", "{agent_scratchpad}"),  
])

# 4\. Criar o Agente  
# Esta função conecta o LLM, as ferramentas e o prompt  
agent = create_tool_calling_agent(llm, tools, prompt)

# 5\. Criar o Executor do Agente  
# O executor é o loop que roda o agente até a resposta final  
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# \--- Execução \---
if __name__ == "__main__":
    print("Agente de Pesquisa pronto! Faça sua pergunta.")

    pergunta1 = "Qual foi o filme vencedor do Oscar de Melhor Filme em 2024?"
    print(f"\n> Pergunta: {pergunta1}")
    response1 = agent_executor.invoke({"input": pergunta1})
    print(f"\n< Resposta Final: {response1['output']}")

    pergunta2 = "Qual é a cor do céu?"
    print(f"\n> Pergunta: {pergunta2}")
    response2 = agent_executor.invoke({"input": pergunta2})
    print(f"\n< Resposta Final: {response2['output']}")
```

**Comando de Execução (Linux/macOS):**
```sh
chmod +x exercicios/capitulo_05/exercicio_1/run.sh
./exercicios/capitulo_05/exercicio_1/run.sh
```
**Comando de Execução (Windows):**
```bat
REM Execute o exercício no Windows
exercicios\capitulo_05\exercicio_1\run.bat
```
**Saída Esperada (pode variar):**
```
Agente de Pesquisa pronto! Faça sua pergunta.
> Pergunta: Qual foi o filme vencedor do Oscar de Melhor Filme em 2024?
< Resposta Final: [Resposta baseada na busca Tavily]
> Pergunta: Qual é a cor do céu?
< Resposta Final: Azul
```
* **Dica:** O exercício pode ser facilmente adaptado para LangGraph usando `create_react_agent`, tornando o agente mais robusto e escalável. Exemplo:
```python
from langgraph.prebuilt import create_react_agent
agent_executor = create_react_agent(llm, tools)
response = agent_executor.invoke({"messages": [("human", pergunta1)]})
print(response["messages"][-1].content)
```
* **Dica:** Use streaming para inspecionar o raciocínio do agente passo a passo:
```python
for event in agent_executor.stream({"messages": [("human", pergunta1)]}, stream_mode="values"):
    print(event["messages"][-1].content)
```
* Proteja chaves de API com arquivos `.env` e configure tracing conforme necessário.

---

### Sistemas Multiagentes e a Magia do LangGraph

E se um problema for tão complexo que um único agente não é suficiente? Entramos no mundo dos **sistemas multiagentes**. A ideia é criar um "time" de agentes especializados, cada um com suas próprias ferramentas e responsabilidades, que colaboram para resolver um problema maior.

Por exemplo, imagine um agente de pesquisa, um agente escritor e um agente crítico trabalhando juntos para criar um relatório. O orquestrador (ou "roteador") passaria a tarefa inicial para o pesquisador, o resultado para o escritor, a versão escrita para o crítico, e o feedback de volta para o escritor, em um ciclo.

Gerenciar esses fluxos complexos, que podem ter ciclos e condicionais, é um desafio. É para isso que o **LangGraph** foi criado. Ele é uma biblioteca construída sobre o LangChain que permite definir fluxos de trabalho de agentes como um **grafo**. Cada nó no grafo pode ser um agente ou uma função, e as arestas definem como o estado (as informações) flui entre eles.

O LangGraph é o estado da arte para construir sistemas multiagentes robustos e é um tópico avançado que exploraremos em projetos futuros, mas é fundamental que você saiba que ele existe e qual problema ele resolve.

---

### Troubleshooting Comum
* Instale o LangGraph com `pip install langgraph`.
* Configure memória e checkpointers para agentes multiagentes.
* Debug de fluxos multiagentes pode ser feito inspecionando o histórico de mensagens e eventos.
* Proteja chaves de API e configure tracing para inspeção detalhada.

---

### Pontos Chave
* Agentes usam LLMs como "cérebros" para tomar decisões dinâmicas, diferentemente das Chains com fluxo fixo.
* Engenharia de Contexto e uso de memória são cruciais para gerenciar informações em sistemas agênticos.
* Ferramentas (Tools) e o Executor do Agente (Agent Executor) são componentes essenciais para a funcionalidade do agente.
* O LangGraph é o padrão para orquestrar sistemas multiagentes complexos.
* O uso de ferramentas bem descritas e engenharia de contexto são diferenciais para agentes eficientes.

---

### Resumo do Capítulo
Neste capítulo, você aprendeu sobre agentes autônomos e multiagentes no LangChain, entendendo como eles diferem das chains tradicionais ao tomar decisões dinâmicas. Explorou o padrão ReAct, engenharia de contexto, o papel do RAG para ampliar o conhecimento dos agentes, e construiu um agente de pesquisa hands-on. Conheceu o LangGraph para orquestração de sistemas multiagentes e revisou os principais conceitos para consolidar o aprendizado.

> **Nota do autor:** O tema de sistemas multiagentes e orquestração com LangGraph é vasto e está em rápida evolução. Se você se interessa por arquiteturas avançadas de IA, vale considerar um livro dedicado ao LangGraph. Ele permitiria explorar casos de uso, padrões de design, integração com outras ferramentas e exemplos práticos em profundidade. O interesse por sistemas multiagentes está crescendo, e um material aprofundado pode ser muito útil para a comunidade.

---

### Teste seu Conhecimento
1. Qual é a característica que define um Agente e o diferencia de uma Chain?
   a) O uso de modelos de linguagem do Google.
   b) A capacidade de tomar decisões dinâmicas sobre qual ação executar a seguir.
   c) A velocidade de processamento.
   d) A capacidade de gerar texto.
2. No padrão ReAct (Reason + Act), qual é o papel do LLM?
   a) Apenas executar a ferramenta (Act).
   b) Apenas raciocinar sobre qual ferramenta usar (Reason).
   c) Raciocinar sobre qual ferramenta usar e, em seguida, formular a resposta final com base na observação.
   d) Armazenar os resultados em um banco de dados.
3. O que é uma "Tool" (Ferramenta) no contexto de um agente LangChain?
   a) Um modelo de linguagem específico para uma tarefa.
   b) Uma função Python com uma boa descrição que o agente pode decidir invocar.
   c) A interface de usuário do agente.
   d) Um tipo especial de prompt.
4. No exercício do agente de pesquisa, por que o agente não usou a ferramenta de busca para responder "Qual é a cor do céu?"
   a) Porque a API da Tavily estava offline.
   b) Porque o LLM "sabia" a resposta e julgou que não precisava de informações externas.
   c) Porque a pergunta estava mal formulada.
   d) Porque a ferramenta de busca não funciona para perguntas sobre cores.
5. Para qual tipo de problema o LangGraph é a ferramenta mais indicada?
   a) Para criar prompts simples.
   b) Para construir um pipeline linear com duas etapas.
   c) Para orquestrar sistemas complexos com múltiplos agentes que podem interagir em ciclos.
   d) Para treinar um novo modelo de linguagem.
6. Como agentes podem manter histórico e contexto?
   a) Usando checkpointers e componentes de memória como MemorySaver.
   b) Apenas com prompts fixos.
   c) Ignorando o histórico de mensagens.
   d) Usando apenas ferramentas externas.

**Respostas:**
1. b
2. c
3. b
4. b
5. c
6. a

---

### Projeto Hands-on: Orquestrando Agentes Inteligentes

Coloque em prática os conceitos do capítulo criando um projeto Python que utiliza LangChain para construir um sistema multiagente. Implemente pelo menos dois agentes especializados (ex: pesquisador e escritor), cada um com suas próprias ferramentas. Use LangGraph para orquestrar o fluxo entre eles, proteja suas chaves de API com .env e documente todos os comandos usados. Siga a estrutura sugerida:

- Estrutura de diretórios para sistemas multiagentes.
- Checklist de boas práticas: modularização, logging, versionamento, testes.
- Fluxograma do grafo de agentes.
- Dicas para integração de múltiplas ferramentas e fontes de dados.
- Passos para ativar tracing e compartilhar logs via GitHub.
- Experimente rodar o projeto em diferentes versões do Python usando pyenv.

---