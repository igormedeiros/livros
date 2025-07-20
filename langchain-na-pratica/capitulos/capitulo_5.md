## Capítulo 5: Desenvolvimento de Agentes Autônomos e Multiagentes



Seja bem-vindo a um dos territórios mais fascinantes e, admito, mais complexos do LangChain: os agentes. Se o conceito parecer um pouco abstrato ou intimidador no começo, não se preocupe. É um salto conceitual significativo. Pense nisso como aprender a andar de bicicleta depois de só ter usado patinetes. Nos capítulos anteriores, construímos "patinetes": fluxos de trabalho lineares e previsíveis. Agora, vamos dar equilíbrio e autonomia à nossa criação.

O equilíbrio, assim como na bicicleta, vem com a prática. Vamos começar com calma, entender cada peça, e logo você estará pedalando por conta própria, criando sistemas que pensam e agem. Confie no processo, e vamos passo a passo.

### O que é um Agente? O LLM como Cérebro

Até agora, usamos LLMs para executar tarefas bem definidas dentro de um pipeline (uma Chain). O fluxo era fixo. Um agente, por outro lado, vira esse jogo de cabeça para baixo. Em um sistema agêntico, o LLM não é apenas um executor de tarefas, ele é o **cérebro**, o **motor de raciocínio** que decide o que fazer a seguir.

A principal diferença entre uma Chain e um Agente é a **autonomia**. Um agente é um sistema que usa um LLM como seu "motor de raciocínio" para determinar a sequência de ações a serem tomadas.

* Uma **Chain** segue um caminho predeterminado. Ex: Prompt \-\> LLM \-\> Parse. O caminho não muda.  
* Um **Agente** usa o LLM para escolher um caminho dinamicamente a partir de um conjunto de opções disponíveis (as ferramentas). O caminho pode ser diferente a cada execução.

Essa capacidade de tomar decisões em tempo de execução é o que permite que agentes resolvam problemas complexos, interajam com o mundo exterior e executem tarefas que não podem ser roteirizadas de antemão.

Pense na cena icônica de Matrix (1999), onde Morpheus oferece a Neo a pílula azul ou a pílula vermelha. Neo (o usuário) está buscando a verdade. Morpheus (o Agente) é o sistema que, com base em seu "raciocínio" e acesso a "ferramentas" (como o conhecimento da Matrix e a capacidade de manipular programas), decide qual "ação" tomar para guiar Neo. As "ferramentas" são os programas que Morpheus pode usar, e a "Matrix" é o ambiente onde essas ações acontecem. A pílula vermelha, que revela a verdade e dá a Neo a autonomia para ver o mundo como ele realmente é, pode ser comparada à autonomia que damos aos nossos agentes. Eles não apenas seguem instruções, mas "enxergam" o ambiente e tomam decisões para alcançar um objetivo.

Os efeitos inovadores dessa autonomia são visíveis em modelos como o Google vO3, que demonstram capacidades de raciocínio e interação com o ambiente que eram impensáveis há poucos anos.

### Engenharia de Contexto: A Evolução do Prompt

Quando falamos de agentes, especialmente sistemas com múltiplos agentes que colaboram e compartilham informações, a simples "Engenharia de Prompts" evolui para algo mais sofisticado: a **Engenharia de Contexto**.

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

### Exercício Prático: Agente de Pesquisa Simples

Vamos construir nosso primeiro agente. Ele terá uma única ferramenta: a capacidade de pesquisar na internet para responder a perguntas sobre eventos atuais ou informações que não estavam nos dados de treinamento do LLM. Usaremos a API da Tavily, que é otimizada para casos de uso de IA.

* **Objetivo:** Construir um agente simples que pode usar uma ferramenta de busca para responder a perguntas factuais.  
* **Nome do Arquivo:** `exercicios/capitulo_05/exercicio_1/main.py`  
* **Dependências:** `langchain`, `langchain-google-genai`, `langchain-tavily`, `python-dotenv`  
* **Comando de Instalação:** `uv add langchain langchain-google-genai langchain-tavily python-dotenv`  
* **Configuração Adicional:** Você precisará de uma chave de API da Tavily. Você pode obter uma gratuitamente em tavily.com. Adicione-a ao seu arquivo .env como `TAVILY_API_KEY`.

```python
# exercicios/capitulo_05/exercicio_1/main.py

import os  
from dotenv import load_dotenv  
from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain_tavily_search import TavilySearchResults  
from langchain.agents import AgentExecutor, create_tool_calling_agent  
from langchain_core.prompts import ChatPromptTemplate

# Carregar variáveis de ambiente  
load_dotenv()

# 1. Escolher o LLM que será o cérebro do nosso agente  
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 2\. Definir as ferramentas que o agente pode usar  
search_tool = TavilySearchResults(  
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
    print("Agente de Pesquisa pronto\! Faça sua pergunta.")  
      
    pergunta1 = "Qual foi o filme vencedor do Oscar de Melhor Filme em 2024?"  
    print(f"\\n\> Pergunta: {pergunta1}")  
    response1 = agent_executor.invoke({"input": pergunta1})  
    print(f"\\n\< Resposta Final: {response1['output']}")

    pergunta2 = "Qual é a cor do céu?"  
    print(f"\\n\> Pergunta: {pergunta2}")  
    response2 = agent_executor.invoke({"input": pergunta2})  
    print(f"\\n\< Resposta Final: {response2['output']}")

**Comando de Execução (Linux/macOS):**

```sh
# Dê permissão de execução ao script
chmod +x exercicios/capitulo_05/exercicio_1/run.sh

# Execute o exercício
./exercicios/capitulo_05/exercicio_1/run.sh
```

**Comando de Execução (Windows):**

```bat
REM Execute o exercício no Windows
exercicios\capitulo_05\exercicio_1\run.bat
```


Ao executar, observe a saída com verbose=True. Você verá o LLM raciocinando, decidindo chamar a ferramenta tavily_search_results_json, os resultados que a ferramenta retorna e, finalmente, a formulação da resposta final. Para a segunda pergunta, você verá que o LLM decide que não precisa de uma ferramenta e responde diretamente. Isso é autonomia em ação\!







### Sistemas Multiagentes e a Magia do LangGraph

E se um problema for tão complexo que um único agente não é suficiente? Entramos no mundo dos **sistemas multiagentes**. A ideia é criar um "time" de agentes especializados, cada um com suas próprias ferramentas e responsabilidades, que colaboram para resolver um problema maior.

Por exemplo, imagine um agente de pesquisa, um agente escritor e um agente crítico trabalhando juntos para criar um relatório. O orquestrador (ou "roteador") passaria a tarefa inicial para o pesquisador, o resultado para o escritor, a versão escrita para o crítico, e o feedback de volta para o escritor, em um ciclo.

Gerenciar esses fluxos complexos, que podem ter ciclos e condicionais, é um desafio. É para isso que o **LangGraph** foi criado. Ele é uma biblioteca construída sobre o LangChain que permite definir fluxos de trabalho de agentes como um **grafo**. Cada nó no grafo pode ser um agente ou uma função, e as arestas definem como o estado (as informações) flui entre eles.

O LangGraph é o estado da arte para construir sistemas multiagentes robustos e é um tópico avançado que exploraremos em projetos futuros, mas é fundamental que você saiba que ele existe e qual problema ele resolve.





### Pontos Chave
*   Agentes usam LLMs como "cérebros" para tomar decisões dinâmicas, diferentemente das Chains com fluxo fixo.
*   A Engenharia de Contexto é crucial para gerenciar informações em sistemas agênticos.
*   Ferramentas (Tools) e o Executor do Agente (Agent Executor) são componentes essenciais para a funcionalidade do agente.
*   O LangGraph é a ferramenta ideal para orquestrar sistemas multiagentes complexos.

### **Teste seu Conhecimento**

1. Qual é a característica que define um Agente e o diferencia de uma Chain?  
   a) O uso de modelos de linguagem do Google.  
   b) A capacidade de tomar decisões dinâmicas sobre qual ação executar a seguir.  
   c) A velocidade de processamento.  
   d) A capacidade de gerar texto.  
2. No padrão ReAct (Reason \+ Act), qual é o papel do LLM?  
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

*(Respostas: 1-b, 2-c, 3-b, 4-b, 5-c)*