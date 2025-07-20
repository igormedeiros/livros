## **Glossário**

*   **Agente (Agent):** Sistema que usa um LLM como "cérebro" para decidir ações, utilizando ferramentas e raciocínio dinâmico.
*   **Agent Executor:** Componente que orquestra o ciclo ReAct de um agente, invocando ferramentas e processando observações.
*   **Chain:** Sequência predefinida de operações ou chamadas a modelos de linguagem para formar um pipeline inteligente.
*   **Engenharia de Contexto:** Disciplina de gerenciar e moldar dinamicamente o contexto recebido por agentes para otimizar raciocínio e ações.
*   **Engenharia de Prompts:** Arte de projetar e otimizar instruções para LLMs, visando obter respostas precisas e relevantes.
*   **Ferramenta (Tool):** Função ou ação que um agente pode executar, geralmente uma função Python com descrição clara, permitindo interação com sistemas externos.
*   **LangChain Expression Language (LCEL):** Linguagem declarativa para compor Runnables no LangChain, permitindo criação de pipelines flexíveis, paralelos e eficientes usando o operador pipe (|).
*   **LLM (Large Language Model):** Modelo de linguagem de grande escala, como Gemini, GPT-4, Claude, capaz de entender e gerar texto.
*   **Memória:** Mecanismo que permite agentes reterem informações, histórico de conversas ou fatos, como ConversationBufferMemory, GenerativeAgentMemory, VectorStore e Knowledge Triples.
*   **Multiagente:** Sistema composto por múltiplos agentes especializados que colaboram para resolver problemas complexos, orquestrados por fluxos como LangGraph.
*   **Pipeline:** Fluxo de processamento de dados, composto por etapas encadeadas (chains, agentes, ferramentas) para realizar tarefas complexas.
*   **Prompt:** Instrução ou entrada de texto fornecida a um LLM para gerar uma resposta.
*   **RAG (Retrieval-Augmented Generation):** Padrão arquitetural que permite aos LLMs acessar e utilizar informações externas e atualizadas antes de gerar uma resposta.
*   **ReAct (Thought + Action + Observation):** Padrão de raciocínio para agentes, onde o LLM pensa, executa uma ação e observa o resultado em ciclo iterativo.
*   **Runnable:** Interface padronizada no LangChain que permite encadear componentes usando o operador pipe (|), incluindo prompts, modelos, parsers e funções Python.
*   **uv:** Gerenciador de pacotes e ambientes virtuais escrito em Rust, conhecido por alta performance e compatibilidade com pyproject.toml.
*   **VectorStore:** Estrutura para armazenar e buscar memórias semânticas usando embeddings, utilizada em RAG e recuperação de contexto.
*   **WSL (Windows Subsystem for Linux):** Camada de compatibilidade que permite executar ambiente Linux diretamente no Windows.
*   **LangSmith:** Plataforma para tracing, logging e observabilidade de pipelines LangChain em produção.
*   **LangGraph:** Biblioteca para orquestração de sistemas multiagentes via grafos, permitindo fluxos complexos e colaborativos entre agentes.
