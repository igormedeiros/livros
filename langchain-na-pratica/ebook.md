# **LangChain na Prática: O primeiro passo com Agentes de IA**

**Igor Medeiros**

## **Informações de Copyright**

© 2025 Igor Medeiros. Todos os direitos reservados.

Este livro faz parte da série "IA na Prática".
Lançamento: Julho de 2025.

Nenhuma parte desta publicação pode ser reproduzida, distribuída ou transmitida por qualquer forma ou meio, incluindo fotocópia, gravação ou outros métodos eletrônicos ou mecânicos, sem a permissão prévia por escrito do autor, exceto no caso de breves citações incorporadas em resenhas críticas e outros usos não comerciais permitidos pela lei de direitos autorais.

ISBN: [A SER DEFINIDO]
Créditos de Design e Edição: [A SER DEFINIDO]

Contato: igor@igormedeiros.com.br  
Website: https://igormedeiros.com.br

## **Aviso Legal (Disclaimer)**

Este livro e seu conteúdo são fornecidos "como estão", sem garantias de qualquer tipo, expressas ou implícitas. O autor e o editor não se responsabilizam por quaisquer erros ou omissões, ou por quaisquer danos resultantes do uso das informações contidas neste livro. Os exemplos de código são fornecidos para fins educacionais e podem exigir modificação para uso em produção. A execução dos códigos e a utilização das chaves de API são de inteira responsabilidade do leitor.

## **Prefácio**

[Este prefácio será escrito por Felipe Gagliazzo.]

## **Dedicatória**

Aos meus pais, José Maurício e Genilda, a quem busco honrar todos os dias sendo um ser humano melhor.

À minha filha Melissa, a luz que ilumina minha jornada e me inspira todos os dias a ser melhor.

Ao Dr. Paulo H Pires de Aguiar, o médico e amigo que, com maestria e humanidade, orquestrou o salvamento da minha vida.

## **Agradecimentos**

Nenhum livro é escrito no vácuo, e este não é exceção. Minha gratidão transborda por aqueles que, de formas distintas, mas igualmente importantes, tornaram esta obra possível.

A **Felipe Gagliazzo**, meu Mestre Jedi particular. Sua sabedoria e paciência são um farol. Obrigado pelo aprendizado contínuo e por me dar o apoio necessário para me sentir mais confiante no trabalho e na vida. Sua mentoria é um presente que valorizo imensamente.

A **Nicolli Botelho**, por enxergar além e me confiar desafios que são muito mais que uma declaração de confiança no meu trabalho; são oportunidades generosas de crescimento que me impulsionam a cada dia. Sua liderança inspiradora me motiva a ser um profissional melhor.

A **Marcus Borin**, pelo encorajamento constante e por sempre me empurrar a subir um degrau a mais na infinita escada do conhecimento. Sua crença no meu potencial é um motor poderoso que me faz acreditar que posso ir mais longe.

A **Emilly Gomes**, por uma amizade e um apoio incondicional que me fazem sentir parte de uma comunidade verdadeiramente acolhedora. Sua presença torna a jornada muito mais leve e divertida, e sou grato por cada conversa e risada.

A **Anne Aguiar**, pelo encorajamento sincero e por acreditar em meu trabalho mesmo quando eu duvidava. Sua fé foi um combustível essencial para que este projeto saísse do papel e se tornasse realidade.

Ao **Flavio Pires**, pela amizade inestimável e pela paciência de um monge ao escutar meus longos e intermináveis áudios no WhatsApp divagando sobre agentes de IA. Suas perguntas e insights sempre me ajudaram a clarear as ideias.

Ao **Fernando Fish**, por ser um exemplo tão forte de rigor técnico e científico. Seu profissionalismo, aliado a um carinho e uma inspiração contagianes, são uma referência que busco seguir em minha própria carreira.

À **Patricia Baena**, por acreditar em mim desde o início, por confiar no meu trabalho e por ter a generosidade de sempre buscar me apresentar portas que só eu poderia abrir. Sua mentoria e visão de futuro foram cruciais em minha trajetória.

À **Giselle Arruma**, por segurar minha mão em momentos difíceis, quando precisei de ajuda para me reerguer profissionalmente. Você foi a pessoa que me aparou e me guiou com uma força e uma empatia que jamais esquecerei.

Ao **Fernando Lopes Jr.**, por ser um amigo e um incentivador, sempre me apoiando nos momentos mais difíceis.

Ao **Eduardo Bregaida**, que confiou em mim e me apresentou uma possibilidade de recomeço quando eu mais precisei, enquanto enfrentava uma terrível fase de problemas de saúde mental e buscava um caminho de volta ao mercado de TI. Sua confiança foi um ponto de virada.

À vasta e vibrante comunidade open source do LangChain e de todas as bibliotecas e ferramentas que tornaram este livro possível. Seu trabalho incansável e colaboração são a verdadeira força motriz por trás da inovação em IA.

A cada um de vocês, meu mais profundo e sincero obrigado.

## **Índice Detalhado**

* **Página de Rosto**  
* **Informações de Copyright**  
* **Prefácio**  
* **Dedicatória**  
* **Agradecimentos**  
* **Índice Detalhado**  
* **Introdução**  
  * A Revolução Silenciosa dos LLMs  
  * Por que LangChain? O Poder da Orquestração  
  * Uma Visão de Resolvedor de Problemas  
  * Como Aproveitar ao Máximo Este Livro  
* **Capítulo 1: Introdução ao LangChain — Fundamentos e Conceitos Essenciais**  
  * O que é LangChain? Uma Breve História em Meio à Tempestade da IA  
  * O Problema da Conversa Iterativa e o Nascimento das "Chains"  
  * Exercício Prático: Hello, LangChain\!  
  * A Arquitetura Central: Os Componentes Essenciais  
  * O Ecossistema LangChain: Mais que uma Biblioteca  
  * Tabela 1: LangChain vs. Frameworks Concorrentes  
  * Resumo do Capítulo  
  * Teste seu Conhecimento  
* **Capítulo 2: Configurando o Ambiente de Desenvolvimento Python para LangChain**  
    
  * Meu Ambiente de Batalha: Por que Linux e Ferramentas de Linha de Comando  
  * Gerenciando Versões do Python como um Profissional: pyenv  
  * Um Terminal com Superpoderes: zsh e Oh My Zsh  
  * Segurança e Conveniência com Git: Chaves SSH  
  * Minhas Ferramentas de Batalha: VS Code  
  * Gerenciando Dependências: A Revolução do uv e pyproject.toml  
  * Gerenciando Segredos: Chaves de API e Variáveis de Ambiente  
  * Checklist de Configuração do Ambiente  
  * Resumo do Capítulo  
  * Teste seu Conhecimento  
* **Capítulo 3: Manipulação de Prompts e Modelos de Linguagem com LangChain**  
  * A Arte e a Ciência da Engenharia de Prompts  
  * Templates de Prompt: Reutilização e Dinamismo  
  * Integrando LLMs  
  * Exercício Prático: Um Tradutor Multilíngue Dinâmico  
  * Resumo do Capítulo  
  * Teste seu Conhecimento  
* **Capítulo 4: Construção de Pipelines: Da SequentialChain à LCEL**  
  * A Evolução das Chains: Do Imperativo ao Declarativo  
  * O Jeito Clássico: LLMChain e SequentialChain  
  * A Revolução da LCEL: Por que Devemos Usá-la?  
  * LCEL na Prática: Exercícios Essenciais  
  * Checklist de Construção de Pipelines  
  * Resumo do Capítulo  
  * Teste seu Conhecimento  
* **Capítulo 5: Desenvolvimento de Agentes Autônomos e Multiagentes**  
    
  * O que é um Agente? O LLM como Cérebro  
  * Engenharia de Contexto: A Evolução do Prompt  
  * Componentes de um Agente: Ferramentas e o Executor  
  * Exercício Prático: Agente de Pesquisa Simples  
  * Sistemas Multiagentes e a Magia do LangGraph  
  * Resumo do Capítulo  
  * Teste seu Conhecimento  
* **Capítulo 6: Integração com Bases de Dados e Sistemas Externos**  
  * Trazendo o Mundo Real para a IA  
  * Conectando a Bancos de Dados SQL  
  * Exercício Prático: Agente de Análise de Vendas SQL
  * Integração com APIs REST
  * Exercício Prático: Ferramenta de Cotação de Moedas
  * Checklist de Integração com Sistemas Externos
  * Resumo do Capítulo
  * Teste seu Conhecimento
* **Capítulo 6: Integração com Bases de Dados e Sistemas Externos**

### **Trazendo o Mundo Real para a IA**

Até agora, nossos agentes e chains operaram principalmente com informações que já estavam em seu "conhecimento" ou que podiam ser inferidas. Mas o verdadeiro poder dos agentes de IA se manifesta quando eles podem interagir com o mundo real, acessando e manipulando dados de sistemas externos. Isso inclui bancos de dados, APIs REST, serviços de nuvem, e muito mais.

Neste capítulo, vamos explorar como o LangChain facilita essa integração, transformando seus LLMs em verdadeiros "operadores" de sistemas, capazes de buscar informações, executar ações e automatizar fluxos de trabalho complexos.

### **Conectando a Bancos de Dados SQL**

Muitas empresas possuem uma vasta quantidade de informações armazenadas em bancos de dados relacionais. Capacitar um LLM a interagir com esses bancos de dados, traduzindo perguntas em linguagem natural para consultas SQL e interpretando os resultados, é um caso de uso extremamente poderoso.

O LangChain oferece ferramentas para interagir com bancos de dados SQL, permitindo que o agente construa e execute consultas de forma autônoma.

**Exercício Prático: Agente de Análise de Vendas SQL**

Vamos construir um agente que pode responder a perguntas sobre dados de vendas armazenados em um banco de dados SQLite. O agente usará uma ferramenta customizada para executar consultas SQL.

*   **Objetivo:** Criar um agente que interage com um banco de dados SQL para responder a perguntas sobre vendas.
*   **Nome do Arquivo:** `exercicios/capitulo_06/exercicio_1/main.py`
*   **Dependências:** `langchain`, `langchain-google-genai`, `python-dotenv`
*   **Comando de Instalação:** `uv add langchain langchain-google-genai python-dotenv`

```python
# exercicios/capitulo_06/exercicio_1/main.py

import os
import sqlite3
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool

# Carregar variáveis de ambiente
load_dotenv()

# 1. Configurar o banco de dados SQLite em memória
def setup_database():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY,
            produto TEXT,
            quantidade INTEGER,
            preco REAL,
            data TEXT
        )
    ''')
    vendas_data = [
        ('Laptop', 2, 1200.00, '2024-01-15'),
        ('Mouse', 5, 25.00, '2024-01-15'),
        ('Teclado', 3, 75.00, '2024-01-16'),
        ('Monitor', 1, 300.00, '2024-01-17'),
        ('Laptop', 1, 1200.00, '2024-01-18'),
        ('Webcam', 4, 50.00, '2024-01-18'),
    ]
    cursor.executemany('INSERT INTO vendas (produto, quantidade, preco, data) VALUES (?, ?, ?, ?)', vendas_data)
    conn.commit()
    return conn

# 2. Definir a ferramenta SQL para o agente
@tool
def execute_sql_query(query: str) -> str:
    """
    Executa uma consulta SQL no banco de dados de vendas e retorna o resultado.
    Use esta ferramenta para responder a perguntas sobre dados de vendas.
    O banco de dados contém uma tabela 'vendas' com as colunas:
    'id', 'produto', 'quantidade', 'preco', 'data'.
    Exemplo de uso: SELECT SUM(quantidade) FROM vendas WHERE produto = 'Laptop';
    """
    conn = setup_database()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return str(results)
    except sqlite3.Error as e:
        conn.close()
        return f"Erro ao executar a consulta SQL: {e}"

# 3. Escolher o LLM que será o cérebro do nosso agente
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# 4. Definir as ferramentas que o agente pode usar
tools = [execute_sql_query]

# 5. Criar o Prompt do Agente
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente especializado em analisar dados de vendas. Use a ferramenta 'execute_sql_query' para responder a perguntas sobre vendas. Se a pergunta não puder ser respondida com os dados de vendas, diga que não tem informações."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# 6. Criar o Agente
agent = create_tool_calling_agent(llm, tools, prompt)

# 7. Criar o Executor do Agente
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- Execução ---
if __name__ == "__main__":
    print("Agente de Análise de Vendas pronto! Faça sua pergunta.")

    perguntas = [
        "Qual a quantidade total de Laptops vendidos?",
        "Qual o produto mais vendido em termos de quantidade?",
        "Qual o valor total de vendas?",
        "Quantos itens foram vendidos em 2024-01-18?",
        "Qual o nome do meu cachorro?"
    ]

    for pergunta in perguntas:
        print(f"\n> Pergunta: {pergunta}")
        response = agent_executor.invoke({"input": pergunta})
        print(f"\n< Resposta Final: {response['output']}")
```

**Comando de Execução (Linux/macOS):**

```sh
# Dê permissão de execução ao script
```sh
# Dê permissão de execução ao script
chmod +x exercicios/capitulo_06/exercicio_1/run.sh

# Execute o exercício
./exercicios/capitulo_06/exercicio_1/run.sh
```
```

**Comando de Execução (Windows):**

```bat
REM Execute o exercício no Windows
exercicios\capitulo_06\exercicio_1\run.bat
```
```

**Saída Esperada (pode variar ligeiramente):**

```text
Agente de Análise de Vendas pronto! Faça sua pergunta.

> Pergunta: Qual a quantidade total de Laptops vendidos?
... (saída verbose do agente) ...
< Resposta Final: 3

> Pergunta: Qual o produto mais vendido em termos de quantidade?
... (saída verbose do agente) ...
< Resposta Final: Mouse

> Pergunta: Qual o valor total de vendas?
... (saída verbose do agente) ...
< Resposta Final: 1850.0

> Pergunta: Quantos itens foram vendidos em 2024-01-18?
... (saída verbose do agente) ...
< Resposta Final: 5

> Pergunta: Qual o nome do meu cachorro?
... (saída verbose do agente) ...
< Resposta Final: Não tenho informações sobre o nome do seu cachorro, pois minha base de dados contém apenas informações de vendas.
```

**Troubleshooting Comum:**

*   **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Certifique-se de que sua `GOOGLE_API_KEY` está corretamente configurada no arquivo `.env` na raiz do projeto.
*   **`ModuleNotFoundError`:** Verifique se todas as dependências (`langchain`, `langchain-google-genai`, `python-dotenv`) foram instaladas corretamente usando `uv add` ou `pip install`.
*   **Erros de Conexão:** Problemas de rede ou limites de taxa da API podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.
*   **Agente não usando a ferramenta SQL:** Se o agente não estiver chamando a ferramenta `execute_sql_query` quando esperado, revise a `description` da ferramenta. Ela deve ser clara e concisa, indicando exatamente o que a ferramenta faz e quando deve ser usada. O LLM usa essa descrição para decidir se a ferramenta é relevante para a tarefa.
*   **Erros de SQL:** Se o agente gerar consultas SQL inválidas, revise o `system prompt` para fornecer instruções mais claras sobre o schema do banco de dados e os tipos de consultas esperadas. O `temperature=0` no modelo ajuda a torná-lo mais determinístico na geração de SQL.  
* **Capítulo 7: Técnicas Avançadas: Memória, Feedback e Aprendizado Contínuo** (Conteúdo a ser expandido)
* **Capítulo 8: Testes, Debugging e Otimização de Aplicações LangChain** (Conteúdo a ser expandido)

## **Introdução**

A vida nos conduz por caminhos únicos. Antes de mergulharmos no código e nos conceitos que preenchem as páginas a seguir, gostaria que você fizesse uma pequena pausa. Reflita sobre as razões que te trouxeram até aqui, até este livro. Foi a curiosidade sobre o boom da Inteligência Artificial? A necessidade de resolver um problema específico no seu trabalho? Ou talvez um desejo profundo de criar algo novo, algo que possa, de alguma forma, impactar o mundo?

Seja qual for a sua motivação, saiba que ela é a faísca inicial de uma jornada transformadora. Este livro nasceu de uma motivação parecida: a necessidade de criar uma ponte. Uma ponte entre a teoria complexa dos Modelos de Linguagem de Grande Escala (LLMs) e a prática diária de nós, desenvolvedores Python. O LangChain surgiu como uma ferramenta revolucionária, uma espécie de canivete suíço que nos permite orquestrar, conectar e dar superpoderes a esses LLMs. Mas, como toda ferramenta poderosa, ela vem com sua própria curva de aprendizado.

Minha intenção aqui não é apenas entregar um manual técnico. É compartilhar a experiência vivida na trincheira, criando agentes inteligentes que resolvem problemas reais de negócios e, o que mais me move, que têm o potencial de impactar vidas. Minha grande paixão é a área da saúde, um campo onde a tecnologia, quando aplicada com propósito e empatia, pode reescrever histórias.

Espero que este guia seja um farol na sua jornada. Que ele te dê a confiança para transformar teoria em código, e código em soluções elegantes e eficientes. E para que nossa conversa não termine na última página, criei um espaço para continuarmos essa troca: um "Gêmeo Digital" deste livro, um assistente com quem você pode conversar, tirar dúvidas e explorar os conceitos que veremos aqui. Ele é a alma viva deste projeto, e você pode acessá-lo em: http://chat.com/gemini-ebook-com-alma.

Vamos começar?

### **A Revolução Silenciosa dos LLMs**

Se você é um desenvolvedor Python, provavelmente sentiu a terra tremer nos últimos anos. O que antes parecia ficção científica — máquinas que conversam, escrevem código, criam imagens e raciocinam sobre dados complexos — de repente se tornou parte do nosso kit de ferramentas diário. Os Modelos de Linguagem de Grande Escala (LLMs), como os da família GPT, Gemini, Claude e Llama, não são apenas chatbots glorificados; eles representam uma mudança fundamental na forma como construímos software.

A ascensão dos LLMs não é apenas uma evolução tecnológica; é uma **revolução silenciosa** que está redefinindo a interação humano-computador e a própria engenharia de software. Eles não são apenas ferramentas, mas parceiros de raciocínio que amplificam nossa capacidade de criar e inovar.

Lembro-me do meu primeiro contato com um "prompt" em 1996, no MS-DOS. Aquela tela preta com um cursor piscando, esperando um comando. A palavra "prompt" vem do latim "promptus", que significa "pronto", "disposto", "rápido". No contexto da computação, era o sinal de que o sistema estava pronto para receber uma instrução. Hoje, com os LLMs, o conceito de "prompt" evoluiu, mas a essência permanece: é a nossa forma de dar uma instrução, de iniciar um diálogo com a máquina.

É importante notar que um produto como o ChatGPT não é apenas um LLM (como o GPT-4o) isolado. Ele é uma aplicação completa e complexa, que já utiliza internamente muitos dos conceitos que vamos aprender aqui: RAG para buscar informações atualizadas, ferramentas (Tools) para executar ações, e memória para manter o contexto da conversa. Essa complexidade por trás de uma interface aparentemente simples é o que torna a engenharia de LLMs tão fascinante e desafiadora.

Estamos saindo de uma era puramente imperativa, onde dizemos à máquina *como* fazer cada passo, para uma era mais declarativa, onde descrevemos *o que* queremos e o modelo nos ajuda a chegar lá. Essa mudança de paradigma exige uma nova forma de pensar e de construir software. Isso abre um universo de possibilidades, mas também traz um novo conjunto de desafios:

*   **Conectar LLMs a dados privados:** Como fazer com que esses cérebros de IA poderosos, mas isolados, acessem e utilizem nossos dados internos e proprietários de forma segura e eficiente?
*   **Interagir com APIs externas:** Como permitir que os LLMs executem ações no mundo real, como enviar e-mails, consultar bancos de dados ou interagir com sistemas legados?
*   **Gerenciar memória e contexto:** Como dar-lhes memória para que possam manter uma conversa coerente e contextualizada ao longo do tempo, sem "esquecer" o que foi dito anteriormente?
*   **Orquestrar tarefas complexas:** Como encadear múltiplos passos e decisões para resolver problemas que exigem mais do que uma única interação?

É crucial, no entanto, manter uma perspectiva crítica. Como o renomado filósofo Luciano Floridi adverte, a inteligência artificial, se mal compreendida ou aplicada sem ética, pode levar à "idiotice artificial" – a automação de processos sem discernimento ou sabedoria. Nosso objetivo com este livro é ir além da mera automação, buscando a amplificação da inteligência humana, não sua substituição cega.

É exatamente aqui que a nossa história começa, e onde o LangChain se torna uma ferramenta indispensável.

### **Por que LangChain? O Poder da Orquestração**

Em meio a essa explosão de possibilidades, surgiu o LangChain. Pense no seu LLM favorito como um motor de Fórmula 1: incrivelmente potente, mas inútil sem um chassi, um sistema de transmissão, fiação e um painel de controle. O LangChain é exatamente isso: o framework que fornece a "transmissão, a fiação e o sistema de controle" para o motor do LLM.

Lançado no final de 2022, o LangChain rapidamente se tornou o padrão *de fato* para desenvolvedores que desejam construir aplicações robustas e "conscientes de dados" com LLMs. Ele não é apenas mais uma biblioteca; é um framework de orquestração completo. Seu objetivo é simplificar cada estágio do ciclo de vida de uma aplicação de IA, desde a prototipagem rápida até a implantação em produção:

*   **Desenvolvimento Acelerado:** O LangChain oferece uma vasta coleção de componentes modulares e reutilizáveis. Isso inclui modelos (para interagir com diferentes LLMs), prompts (para gerenciar e otimizar as instruções), chains (para encadear operações complexas) e agentes (para dar autonomia aos LLMs, permitindo que eles tomem decisões e usem ferramentas). Essa modularidade permite que você construa aplicações complexas de forma muito mais rápida e eficiente, reutilizando blocos de construção testados e otimizados.
*   **Consciência de Dados (Data-Awareness):** Um dos maiores desafios ao trabalhar com LLMs é conectá-los aos seus dados privados e em tempo real. O LangChain se destaca por facilitar a integração com diversas fontes de dados, como bancos de dados, APIs, documentos e sistemas de armazenamento de vetores. Isso é crucial para construir aplicações que não apenas geram texto, mas que também compreendem e interagem com o mundo real através dos seus próprios dados.
*   **Agentes Autônomos e Ferramentas:** O framework eleva o LLM de um simples gerador de texto para um "motor de raciocínio". Com o LangChain, você pode capacitar seu LLM a usar ferramentas externas (como motores de busca, calculadoras, APIs de terceiros) e a tomar decisões sobre qual ação executar para atingir um objetivo. Isso abre as portas para a criação de agentes verdadeiramente autônomos e sistemas multiagentes complexos.
*   **Observabilidade e Avaliação em Produção:** Através de ferramentas complementares como o LangSmith, o LangChain permite inspecionar, monitorar e avaliar suas aplicações em tempo real. Isso é absolutamente crucial para identificar gargalos, depurar comportamentos inesperados e garantir a qualidade e a confiabilidade das suas aplicações de IA em ambientes de produção.
*   **Implantação Simplificada:** O framework facilita a transformação de suas lógicas complexas em APIs prontas para produção, permitindo que você integre suas aplicações de IA em sistemas existentes com facilidade.

Em resumo, o LangChain nos dá os blocos de construção e a cola para criar aplicações que vão muito além de uma simples chamada de API para um LLM. Seu sucesso e abordagem pioneira inspiraram o surgimento de diversos outros frameworks fantásticos, como CrewAI, Microsoft Autogen, Pydantic AI e Praison AI, que hoje compõem um ecossistema rico e vibrante para o desenvolvimento de agentes. O LangChain se mantém como uma base sólida e flexível para a inovação em IA.

### **Uma Visão de Resolvedor de Problemas**

Antes de escrever a primeira linha de código com LangChain, quero te propor uma mudança de mentalidade. Muitas vezes, ficamos fascinados com a tecnologia pela tecnologia. Mas a verdadeira magia acontece quando usamos essa tecnologia para resolver um problema real, seja ele seu, da sua empresa ou de outra pessoa.

Antes de codificar, é preciso ter uma visão de resolvedor de problemas.

Cada novo conhecimento que você adquirir neste livro não é apenas um conceito teórico; é uma nova ferramenta na sua caixa. Pense em um problema que te incomoda. Um processo manual e repetitivo no seu trabalho? A dificuldade de encontrar informações em uma base de dados interna gigante? A vontade de criar um assistente pessoal que realmente te entenda?

Eu, por exemplo, aprendi sobre visão computacional e frameworks como o YOLO não por um interesse puramente acadêmico, mas porque queria resolver um problema que me toca profundamente. Vendo a luta diária do meu pai com o Alzheimer, comecei a desenvolver um projeto para usar câmeras de segurança internas para monitorar idosos com demência, alertando familiares ou cuidadores sobre quedas ou situações de risco diretamente em seus celulares. O problema real me deu a motivação e o contexto para aprender a ferramenta.

Mantenha essa abordagem em mente enquanto avança pelos capítulos. Tente conectar cada conceito — Chains, Agents, RAG — a uma possível solução para um problema que importa para você. Essa abordagem transforma o aprendizado passivo em uma busca ativa por soluções, tornando a jornada muito mais significativa e eficaz.

No fundo, a programação e a filosofia compartilham um terreno comum: ambas buscam entender e moldar a realidade através da lógica e da abstração. Assim como um filósofo constrói argumentos para desvendar verdades, um programador constrói algoritmos para resolver problemas. A IA, nesse sentido, é a materialização de um pensamento filosófico antigo: a busca por inteligência e autonomia. Ao programar com IA, estamos não apenas escrevendo código, mas participando de um diálogo contínuo com a natureza da inteligência e da criação.

### **Como Aproveitar ao Máximo Este Livro**

Este livro foi projetado para ser uma jornada prática e interativa. Lembro-me vividamente de uma aula no meu primeiro ano de Ciência da Computação. A sala estava barulhenta, a turma dispersa, e o professor, Kao Jin Kan, um mestre sábio, parou de escrever na lousa, virou-se para nós e disse um provérbio chinês que nunca mais esqueci:

*Eu ouço, e eu esqueço. Eu vejo, e eu me lembro. Eu faço, e eu aprendo.*

Essa é a filosofia deste livro. Para você realmente aprender, você precisa *fazer*.

* **Mão na Massa:** Não apenas leia. Abra seu editor de código, crie o ambiente virtual (como veremos no Capítulo 2\) e execute cada exemplo. Modifique os exercícios, quebre o código e tente consertá-lo. É na prática que o conhecimento se solidifica.  
* **Use o Repositório de Exercícios:** Todos os códigos práticos deste livro estão disponíveis em um repositório no GitHub. Use-o como ponto de partida e como referência. Você pode encontrá-lo em: https://github.com/igormedeiros/livros/blob/main/langchain-na-pratica/.  
* **Conecte-se com a Comunidade:** Aprender junto é sempre mais poderoso. Criei uma comunidade no Telegram para que possamos trocar ideias, tirar dúvidas e compartilhar nossos projetos. A jornada continua lá: https://t.me/igormedeiros\_comunidade.  
* **Abrace os Desafios:** Haverá momentos em que um conceito parecerá abstrato ou um código não funcionará de primeira. Isso é normal, e faz parte do processo de crescimento. Lembre-se: 'A persistência é o caminho do êxito.' As "Notas de Acolhimento" e as histórias pessoais que compartilho ao longo do livro estão aqui para te lembrar que a jornada de aprendizado tem seus altos e baixos, e que a perseverança é a chave para superar qualquer obstáculo. Não hesite em buscar ajuda na comunidade ou revisitar os conceitos. Estamos aqui para apoiar você em cada passo.

Estamos prontos? Então, vamos começar a construir coisas incríveis.



## **Capítulo 1: Introdução ao LangChain — Fundamentos e Conceitos Essenciais**

**Neste capítulo, você vai aprender:**

*   O que é LangChain e como ele surgiu para resolver problemas reais na era da IA.
*   Os conceitos fundamentais de Chains, Prompts, Models e Agents.
*   Como o LangChain se posiciona no ecossistema de IA, comparado a outros frameworks.
*   Seu primeiro código prático com LangChain, usando a sintaxe moderna da LCEL.

**Resumo Executivo:** Este capítulo serve como a porta de entrada para o universo LangChain. Abordaremos a história e a motivação por trás do framework, seus componentes essenciais e como ele se encaixa no cenário atual da inteligência artificial. Ao final, você terá uma compreensão sólida dos pilares do LangChain e estará pronto para construir suas primeiras aplicações.

### **O que é LangChain? Uma Breve História em Meio à Tempestade da IA**

Antes de mergulharmos, quero que saiba: é normal se sentir um pouco sobrecarregado no início. O mundo da IA avança a passos largos, e o LangChain, como uma ferramenta poderosa, pode parecer complexo. Mas lembre-se, cada grande jornada começa com um primeiro passo. E você já deu o seu ao abrir este livro. Vamos desmistificar cada conceito, juntos. Respire fundo, e vamos nessa!

Para entender o LangChain, vamos simplificar. Imagine que você tem um supercomputador que sabe conversar, escrever e até criar coisas, mas ele está isolado. Ele não consegue acessar a internet, nem seus documentos, nem interagir com outros programas. O LangChain é como a "ponte" que conecta esse supercomputador (o Modelo de Linguagem, ou LLM) ao mundo real.

Ele surgiu no final de 2022, um pouco antes do ChatGPT "explodir" e mostrar a todos o poder dos LLMs. Naquela época, um engenheiro chamado Harrison Chase percebeu que, para construir aplicações realmente úteis com esses modelos, precisávamos de uma forma fácil de:

*   **Conectá-los a informações externas:** Como fazer o LLM "ler" seus e-mails ou documentos?
*   **Permitir que eles usem ferramentas:** Como fazer o LLM "clicar" em um botão ou "enviar" uma mensagem?
*   **Organizar tarefas complexas:** Como fazer o LLM seguir uma série de passos para resolver um problema grande?

O LangChain foi a resposta para essas perguntas. Ele se tornou incrivelmente popular porque oferecia uma maneira de "orquestrar" os LLMs, transformando-os de meros geradores de texto em "cérebros" capazes de interagir com o mundo. Em pouco tempo, o projeto de código aberto cresceu tanto que se tornou uma empresa, a LangChain AI, atraindo grandes investimentos.

Em resumo, o LangChain é a ferramenta que nos permite construir aplicações de IA que vão muito além de uma simples conversa, conectando os LLMs a dados e ferramentas para resolver problemas do dia a dia.

### **O Problema da Conversa Iterativa e o Nascimento das "Chains"**

Se você já usou o ChatGPT, provavelmente já passou por este processo: você tem uma ideia, mas a primeira resposta do modelo não é exatamente o que você queria. Então, você começa um diálogo para refinar o resultado.

Imagine que você quer um poema. Sua conversa pode ser algo assim:

* **Você:** "Escreva um poema sobre a chuva."  
* *O modelo responde com um poema de quatro estrofes.*  
* **Você:** "Gostei, mas está um pouco longo. Você pode deixar mais conciso, com apenas duas estrofes?"  
* *O modelo responde com uma versão mais curta.*  
* **Você:** "Perfeito. Agora, reescreva essa versão mais curta, mas adicione um sentimento de melancolia e a imagem de alguém olhando pela janela."  
* *O modelo finalmente entrega o poema que você tinha em mente.*

O que você acabou de fazer foi um **refinamento iterativo**. Você "encadeou" seus pensamentos, usando a saída de um passo como entrada para o próximo, para guiar o modelo até o resultado desejado. Esse processo é poderoso, mas é manual.

É exatamente aqui que a genialidade do LangChain se revela. O nome **LangChain** significa literalmente "Language Chain" (Chain de Linguagem). A ideia central do framework é permitir que nós, desenvolvedores, automatizemos esse processo de encadeamento.

Em vez de você refinar manualmente o poema, você poderia construir uma "Chain" no LangChain que faz isso programaticamente:

1. **Passo 1:** Um prompt que gera um poema sobre um tópico.  
2. **Passo 2:** A saída do Passo 1 (o poema) é automaticamente enviada para um segundo prompt que o torna mais conciso.  
3. **Passo 3:** A saída do Passo 2 (o poema conciso) é enviada para um terceiro prompt que adiciona um sentimento específico.

Isso é uma **Chain**: uma sequência de operações ou chamadas a modelos de linguagem para formar um pipeline inteligente. É o conceito fundamental que nos permite construir aplicações complexas que vão muito além de uma única pergunta e resposta.

### **Exercício Prático: Hello, LangChain\!**

Vamos colocar a mão na massa com o nosso primeiro código. Este será o "Hello, World\!" do LangChain. Ele vai demonstrar, da forma mais simples possível, o conceito de chain que acabamos de discutir. Para este e os demais exemplos do livro, usaremos os modelos Gemini do Google, especificamente o gemini-1.5-flash, que é incrivelmente rápido e oferece uma camada gratuita generosa para desenvolvedores.

* **Objetivo:** Fazer a primeira chamada a um LLM usando a sintaxe de chain do LangChain para ver o conceito em ação.  
* **Nome do Arquivo:** `exercicios/capitulo_01/exercicio_1/main.py`  
* **Dependências:** `langchain`, `langchain-google-genai`, `python-dotenv`  
* **Comando de Instalação:** `uv add langchain langchain-google-genai python-dotenv`  

```python
# exercicios/capitulo_01/exercicio_1/main.py

import os  
from dotenv import load_dotenv  
from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain_core.prompts import ChatPromptTemplate  
from langchain_core.output_parsers import StrOutputParser

# Carrega as variáveis de ambiente (necessário para a chave do Google)  
# Certifique-se de ter um arquivo .env como explicado no Capítulo 2  
load_dotenv()

# 1. Crie um template de prompt.  
#    Pense nisso como o "molde" para a sua pergunta.  
#    A variável {topico} será preenchida dinamicamente.  
prompt_template = ChatPromptTemplate.from_template(  
    "Escreva uma única frase engraçada sobre o tópico: {topico}"  
)

# 2. Inicialize o LLM.  
#    Este é o "cérebro" que vai gerar a resposta. Usaremos o Gemini Flash.  
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 3. Crie um parser de saída.  
#    Ele vai extrair apenas o texto da resposta do modelo.  
output_parser = StrOutputParser()

# 4. Crie a "Chain" usando o operador pipe (|).  
#    Esta é a mágica da LangChain Expression Language (LCEL)!
#    O fluxo é: prompt -> modelo -> parser  
chain = prompt_template | model | output_parser

# 5. Invoque a chain com um tópico.  
#    O LangChain cuida de passar o resultado de um passo para o outro.  
print("Executando a chain...")  
resposta = chain.invoke({"topico": "desenvolvedores Python"})

# Imprime o resultado final  
print("\nResposta da Chain:")  
print(resposta)
```
```


**Comando de Execução (Linux/macOS):**

```sh
# Dê permissão de execução ao script
chmod +x exercicios/capitulo_01/exercicio_1/run.sh

# Execute o exercício
./exercicios/capitulo_01/exercicio_1/run.sh
```
```

**Comando de Execução (Windows):**

```bat
REM Execute o exercício no Windows
exercicios\capitulo_01\exercicio_1\run.bat
```

**Saída Esperada (pode variar):**

```
Executando a chain...

Resposta da Chain:  
Um desenvolvedor Python não tem medo de cobras, mas treme na base quando vê um erro de indentação.
```

Parabéns\! Você acabou de executar sua primeira Chain. Observe a linha chain \= prompt\_template | model | output\_parser. Essa sintaxe elegante, chamada **LangChain Expression Language (LCEL)**, é a representação visual do encadeamento que discutimos. É a base sobre a qual construiremos aplicações muito mais poderosas.

**Troubleshooting Comum:**

*   **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Certifique-se de que você obteve sua `GOOGLE_API_KEY` do Google AI Studio e a adicionou corretamente ao seu arquivo `.env` na raiz do projeto. Lembre-se de que o arquivo `.env` não deve ser versionado no Git.
*   **`ModuleNotFoundError`:** Verifique se todas as dependências (`langchain`, `langchain-google-genai`, `python-dotenv`) foram instaladas corretamente usando `uv add` ou `pip install`.
*   **Erros de Conexão:** Problemas de rede ou limites de taxa da API podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.


### **A Arquitetura Central: Os Componentes Essenciais**

Agora que você já viu uma chain em ação, vamos formalizar os blocos de construção fundamentais. Pense neles como peças de Lego que podemos combinar de infinitas maneiras.

**1\. Models (LLMs e Chat Models)**

O coração de qualquer aplicação LangChain é um modelo de linguagem. O LangChain fornece uma interface padronizada para interagir com dezenas de modelos diferentes, desde os da OpenAI (GPT-3.5, GPT-4), Google (Gemini), Anthropic (Claude), até modelos de código aberto disponíveis no Hugging Face. Isso significa que você pode trocar o modelo subjacente da sua aplicação com pouquíssimas alterações no código, o que é fantástico para experimentação e otimização de custos.

Existem dois tipos principais de modelos no LangChain:

* **LLMs:** Modelos mais antigos que recebem uma string como entrada e retornam uma string como saída.  
* **Chat Models:** Modelos mais modernos e poderosos que recebem uma lista de mensagens (com papéis como "system", "human" e "ai") e retornam uma mensagem. Hoje, a maioria das aplicações utiliza Chat Models.

**2. Prompts**

Um prompt é a instrução que damos ao modelo de IA. Para conseguir as melhores respostas, precisamos ser claros e específicos. O LangChain nos ajuda a fazer isso de forma inteligente com os **Prompt Templates**.

Pense em um Prompt Template como um "formulário" que você preenche. Ele tem espaços em branco (variáveis) que você pode preencher dinamicamente. Assim, você não precisa escrever a mesma instrução várias vezes, tornando seu código mais organizado e fácil de usar.

**3. Chains**

Já falamos sobre as Chains, mas vamos reforçar: uma Chain é como uma "linha de montagem" para o seu LLM. Ela conecta diferentes componentes (como prompts, modelos e ferramentas) em uma sequência lógica para realizar uma tarefa. A forma mais moderna e recomendada de construir essas "linhas de montagem" é usando a **LangChain Expression Language (LCEL)**, que usa o símbolo `|` (pipe) para conectar as peças. Isso torna o fluxo de trabalho muito mais claro e eficiente.

**4. Agentes (Agents)**

Se as Chains são como roteiros de filme, onde cada passo é predefinido, os Agentes são como atores de improviso. Um Agente usa o LLM não apenas para gerar texto, mas como um "cérebro" que decide o que fazer a seguir. Você dá um objetivo ao Agente e um conjunto de "ferramentas" (como uma busca na internet, uma calculadora, ou acesso a uma API) que ele pode usar. O Agente então "pensa" e decide qual ferramenta usar para alcançar o objetivo. Essa capacidade de tomar decisões dinâmicas é o que permite a criação de sistemas verdadeiramente autônomos e poderosos.

**Nota Pessoal:** Aprender uma tecnologia tão disruptiva quanto o LangChain pode parecer, por vezes, uma batalha íngreme e cheia de imprevistos. Em 2012, a vida me apresentou um desafio que não estava em nenhum manual. Fui diagnosticado com um neurinoma do acústico, um tumor gigante na cabeça, que exigiu uma cirurgia complexa. No pós-operatório, enfrentei uma embolia pulmonar que quase me levou. A batalha pela vida deixou marcas permanentes: uma paralisia facial e surdez total no lado direito do rosto.

Assim como precisei me adaptar a limitações permanentes e encontrar novas formas de seguir em frente, nesta jornada com LangChain, encontraremos obstáculos. Haverá bugs, conceitos que parecem abstratos e momentos de frustração. Esta é a natureza do aprendizado, especialmente em um campo que muda semanalmente. A resiliência que desenvolvemos ao superar esses pequenos desafios técnicos é a mesma força que nos impulsiona na vida. Cada erro corrigido, cada conceito compreendido, é uma pequena vitória que nos fortalece para o próximo passo. Lembre-se disso quando as coisas parecerem difíceis.

### **O Ecossistema LangChain: Mais que uma Biblioteca**

É importante entender que o LangChain evoluiu para ser mais do que apenas a biblioteca principal. O ecossistema hoje é composto por várias partes:

* **langchain-core:** Contém as abstrações e interfaces base (como Runnable, BaseMessage, etc.). É o núcleo leve do framework. Para mais detalhes, consulte a [documentação oficial do LangChain Core](https://python.langchain.com/v0.2/docs/concepts/#langchain-core).
* **langchain-community:** Abriga uma vasta coleção de integrações com ferramentas, modelos e bancos de dados mantidos pela comunidade.  
* **langchain:** O pacote principal que contém as cadeias, agentes e estratégias de recuperação de alto nível que compõem a arquitetura cognitiva de uma aplicação.  
* **LangGraph:** Uma extensão do LangChain para construir agentes *stateful* e sistemas multiagentes complexos, representando os fluxos como grafos. É a ferramenta de ponta para os casos de uso mais avançados.  
* **LangSmith:** Uma plataforma de observabilidade, depuração e avaliação. Se você está levando o desenvolvimento com LangChain a sério, o LangSmith não é opcional, é essencial. Ele te dá uma visão de raio-x de tudo o que acontece dentro de suas chains e agentes, tornando o debugging de sistemas não-determinísticos muito mais gerenciável.

### **Tabela 1: LangChain vs. Frameworks Concorrentes**

Para situar o LangChain no cenário atual, é útil compará-lo com outras ferramentas populares.

| Framework | Foco Principal | Pontos Fortes | Caso de Uso Típico |
| :---- | :---- | :---- | :---- |
| **LangChain** | Orquestração de LLMs e Agentes | Flexibilidade, ecossistema de agentes, vastas integrações, LangGraph | Chatbots complexos, agentes autônomos, assistentes de código |
| **LlamaIndex** | Indexação e Preparação de Dados para RAG | Otimização de dados para RAG, conectores de dados, índices hierárquicos | Aplicações RAG sobre grandes volumes de documentos |
| **CrewAI** | Orquestração de Agentes Colaborativos | Foco em colaboração entre agentes, definição de papéis e tarefas, processos sequenciais | Equipes de agentes autônomos para pesquisa, escrita e análise |
| **Microsoft Autogen** | Framework de Multiagentes Conversacionais | Agentes conversáveis, flexibilidade na definição de padrões de interação | Simulações complexas, resolução de problemas em grupo, jogos |
| **Pydantic AI** | Geração de Saídas Estruturadas (JSON) | Integração com Pydantic, garantia de conformidade com schemas JSON | Extração de dados, saídas de API, integração com sistemas legados |
| **Praison AI** | Orquestração de Multi-Agentes LLM (Low-Code) | Facilidade de uso, customização, integração com outros frameworks, suporte a múltiplos LLMs | Automação de processos, chatbots, pesquisa multi-agente, análise de dados |

*Fonte: Análise do autor.*

É importante notar que, embora o LangChain seja uma ferramenta poderosa e flexível, a escolha do framework ideal depende muito do caso de uso específico. LlamaIndex, por exemplo, brilha em cenários de RAG complexos, enquanto CrewAI e Microsoft Autogen oferecem abordagens mais especializadas para orquestração multiagente. Pydantic AI foca na garantia de saídas estruturadas, crucial para integração com sistemas legados. Praison AI, por sua vez, se destaca pela facilidade de uso e orquestração de multi-agentes com foco em low-code.

O LangChain se posiciona como uma ferramenta modular de propósito geral, permitindo a construção de uma vasta gama de aplicações de IA. A escolha entre esses frameworks envolve um trade-off entre flexibilidade, facilidade de uso e especialização. Enquanto frameworks como CrewAI e AutoGen oferecem soluções mais prontas para orquestração multiagente e colaboração, o LangChain fornece os blocos de construção fundamentais para criar soluções altamente customizadas e complexas, sendo a base para muitos desses outros frameworks. Compreender esses trade-offs é fundamental para escolher a ferramenta certa para o trabalho.



### **Pontos Chave**

*   LangChain simplifica a orquestração de LLMs, permitindo a construção de aplicações complexas.
*   O conceito de "Chain" automatiza sequências de chamadas a LLMs, tornando o desenvolvimento mais estruturado.
*   Os componentes fundamentais (Models, Prompts, Chains, Agents) são blocos de construção modulares.
*   A LCEL (LangChain Expression Language) é a forma moderna e eficiente de construir pipelines no LangChain.



### **Teste seu Conhecimento**

1. Qual foi o principal problema que o LangChain buscou resolver em sua criação?  
   a) A falta de modelos de linguagem poderosos.  
   b) A dificuldade de treinar novos LLMs.  
   c) A necessidade de automatizar e estruturar sequências de chamadas para LLMs.  
   d) A ausência de interfaces de chat como o ChatGPT.  
2. O que é uma "Chain" no contexto do LangChain?  
   a) Um tipo específico de LLM.  
   b) Uma sequência de componentes (prompts, modelos, etc.) conectados para executar uma tarefa complexa.  
   c) Uma ferramenta para buscar informações na internet.  
   d) A interface de usuário de uma aplicação de IA.  
3. Qual dos seguintes NÃO é um componente central da arquitetura LangChain?  
   a) Models  
   b) Prompts  
   c) Agents  
   d) Database  
4. No exercício "Hello, LangChain\!", qual operador foi usado para conectar o prompt, o modelo e o parser?  
   a) \+ (adição)  
   b) \-\> (seta)  
   c) | (pipe)  
   d) & (e comercial)  
5. Qual a principal diferença entre uma Chain e um Agent?  
   a) Agents são mais rápidos que Chains.  
   b) Chains usam múltiplos modelos, enquanto Agents usam apenas um.  
   c) Chains seguem um fluxo predefinido, enquanto Agents usam um LLM para decidir dinamicamente qual ação tomar.  
   d) Agents só podem ser usados para chatbots, enquanto Chains são de uso geral.

*(Respostas: 1-c, 2-b, 3-d, 4-c, 5-c)*

## **Projeto Hands-on: Construindo um Chatbot Simples**

Neste projeto, você vai integrar tudo o que aprendeu no Capítulo 1 para construir um chatbot simples que pode responder a perguntas básicas. Este será o seu primeiro passo para criar aplicações mais complexas com LangChain.

**Objetivo:** Criar um chatbot que interage com o usuário, mantendo um histórico de conversas e respondendo a perguntas gerais.

**Nome do Arquivo:** `exercicios/capitulo_01/exercicio_2/main.py`

**Dependências:** `langchain`, `langchain-google-genai`, `python-dotenv`, `langchain-community`

**Comando de Instalação:** `uv add langchain langchain-google-genai python-dotenv langchain-community`

```python
# exercicios/capitulo_01/exercicio_2/main.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

# Carrega as variáveis de ambiente
load_dotenv()

# Inicializa o LLM
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

# Cria um template de prompt com um placeholder para o histórico de chat
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente prestativo. Responda às perguntas de forma concisa e útil."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
])

# Cria o parser de saída
output_parser = StrOutputParser()

# Cria a chain
chain = prompt | model | output_parser

# Histórico de chat (simulado por enquanto)
chat_history = []

print("Chatbot Simples. Digite 'sair' para encerrar.")

while True:
    user_input = input("Você: ")
    if user_input.lower() == 'sair':
        break

    # Invoca a chain com a entrada do usuário e o histórico de chat
    response = chain.invoke({
        "input": user_input,
        "chat_history": chat_history
    })

    print(f"Bot: {response}")

    # Atualiza o histórico de chat
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response))

print("Chatbot encerrado.")
```

**Comando de Execução (Linux/macOS):**

```sh
# Dê permissão de execução ao script
chmod +x exercicios/capitulo_01/exercicio_2/run.sh

# Execute o exercício
./exercicios/capitulo_01/exercicio_2/run.sh
```
```

**Comando de Execução (Windows):**

```bat
REM Execute o exercício no Windows
exercicios\capitulo_01\exercicio_2\run.bat
```


**Troubleshooting Comum:**

*   **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Certifique-se de que você obteve sua `GOOGLE_API_KEY` do Google AI Studio e a adicionou corretamente ao seu arquivo `.env` na raiz do projeto. Lembre-se de que o arquivo `.env` não deve ser versionado no Git.
*   **`ModuleNotFoundError`:** Verifique se todas as dependências (`langchain`, `langchain-google-genai`, `python-dotenv`, `langchain-community`) foram instaladas corretamente usando `uv add` ou `pip install`.
*   **Erros de Conexão:** Problemas de rede ou limites de taxa da API podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.
*   **Comportamento Inesperado do Chatbot:** Se o chatbot não estiver mantendo o contexto ou respondendo de forma estranha, revise o `system prompt` e a forma como o `chat_history` está sendo passado para a chain. A clareza das instruções no prompt é fundamental.

## **Capítulo 2: Configurando o Ambiente de Desenvolvimento Python para LangChain**



Então, antes de começarmos, respire fundo. Pegue um café (ou um chá, no meu caso, já que ironicamente não sou fã de café) e vamos passar por isso juntos, passo a passo. Lembro-me de um colega que passou horas depurando um erro complexo, apenas para descobrir que era um ponto e vírgula faltando. Ou, pior, um espaço a mais na indentação em Python. A máquina é implacável com a sintaxe, mas a satisfação de encontrar o erro é indescritível! A paciência que você exercita aqui será sua maior aliada em toda a jornada com IA. Prometo que, ao final deste capítulo, você terá uma base sólida e organizada para construir todos os projetos incríveis que virão.

### **Meu Ambiente de Batalha: Por que Linux e Ferramentas de Linha de Comando**

Sei que muitos desenvolvedores, especialmente no mundo corporativo, estão acostumados com o Windows e o PowerShell. E eu entendo perfeitamente, são ferramentas poderosas e familiares. No entanto, para o tipo de desenvolvimento que faremos aqui, e para o desenvolvimento de software em geral, eu recomendo fortemente que você abrace o ambiente Linux.

**Por que Linux?** A grande maioria das ferramentas de desenvolvimento, servidores de produção, contêineres (Docker) e tecnologias de nuvem rodam nativamente em Linux. Desenvolver em um ambiente semelhante ao de produção economiza uma quantidade enorme de dores de cabeça com compatibilidade, permissões de arquivo e pequenas diferenças que podem quebrar sua aplicação quando você for para o *deploy*.

**"Mas Igor, eu uso Windows\!"** Sem problemas\! A melhor invenção da Microsoft para desenvolvedores nos últimos anos foi o **Windows Subsystem for Linux (WSL)**. Ele permite que você rode uma distribuição Linux completa diretamente no seu Windows, com integração total. É o melhor dos dois mundos. Pessoalmente, eu uso o Kali Linux, que está disponível gratuitamente na Microsoft Store, por sua robustez e conjunto de ferramentas, mas distribuições como Ubuntu também são excelentes escolhas.

(E, parafraseando um meme clássico da comunidade de desenvolvimento: "Pare de Programar no Windows!")

### **Gerenciando Versões do Python como um Profissional: pyenv**

Outro ponto crucial é o gerenciamento de versões do Python. Um projeto pode precisar do Python 3.11, outro do 3.12, e o seu sistema operacional pode depender de uma versão específica para funcionar. Instalar múltiplas versões globalmente é uma receita para o desastre.

A solução para isso é o **pyenv**. Ele é uma ferramenta fantástica que permite instalar e gerenciar múltiplas versões do Python no seu espaço de usuário, sem interferir com o Python do sistema. Com um simples comando, você pode definir qual versão do Python usar globalmente, por pasta de projeto ou até mesmo por sessão de terminal.

**Vantagens do pyenv:**

* **Isolamento:** Cada versão do Python é instalada em seu próprio diretório, evitando conflitos.  
* **Flexibilidade:** Teste seu código em diferentes versões do Python com facilidade.  
* **Consistência:** Garanta que toda a sua equipe use exatamente a mesma versão do Python para um projeto.

Exercício Prático: Instalando pyenv e Python no Kali Linux (WSL)  
Este script automatiza a instalação de todas as dependências necessárias, do pyenv e da versão mais recente do Python no Kali Linux.

* **Objetivo:** Preparar um ambiente Linux robusto com a versão correta do Python gerenciada pelo pyenv.  
* **Nome do Arquivo:** `setup_python_kali.sh`  
* **Dependências:** git, curl, build-essential e outras dependências de compilação.  
* **Comando de Execução:** ````sh
bash setup_python_kali.sh
````

```sh
#!/bin/bash

# Script DEFINITIVO para instalar Python 3.12.9 no Kali Linux com pyenv  
# Versão 3: Lida com a ausência do comando 'gpg'.

# O comando 'set -e' garante que o script pare se algum comando falhar.  
set -e

echo "--- PASSO 1: Corrigindo o 'apt' (Lidando com a falta de 'gpg') ---"  
# Temporariamente, dizemos ao apt para confiar no repositório sem verificar a assinatura.  
# ISSO É INSEGURO, mas necessário para quebrar o ciclo e poder instalar o gpg.  
echo "deb [trusted=yes] http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list

echo ""  
echo "--- PASSO 2: Instalando 'gpg' e 'wget' ---"  
sudo apt update  
# Agora que o apt funciona (de forma insegura), instalamos o gnupg (que contém o gpg) e o wget.  
sudo apt install -y gnupg wget

echo ""  
echo "--- PASSO 3: Consertando a segurança do 'apt' DE FORMA PERMANENTE ---"  
# 3.1: Agora que temos o 'gpg', podemos baixar e instalar a chave de segurança oficial.  
wget -q -O - https://archive.kali.org/archive-key.asc | sudo gpg --dearmor -o /usr/share/keyrings/kali-archive-keyring.gpg

# 3.2: Reescrevemos o arquivo de repositórios para o modo SEGURO, forçando a verificação com a chave que acabamos de baixar.  
echo "deb [signed-by=/usr/share/keyrings/kali-archive-keyring.gpg] http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list

echo "Segurança do APT restaurada."

echo ""  
echo "--- PASSO 4: Atualizando pacotes (agora de forma segura) e instalando TODAS as dependências ---"  
sudo apt update  
sudo apt install -y build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl llvm \
libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev \
liblzma-dev python3-openssl git

echo ""  
echo "--- PASSO 5: Instalando o pyenv (se necessário) ---"  
if [ ! -d "$HOME/.pyenv" ]; then  
    curl https://pyenv.run | bash  
else  
    echo "O pyenv já está instalado. Pulando a instalação."  
fi

echo ""  
echo "--- PASSO 6: Configurando o ambiente do pyenv ---"  
if ! grep -qF 'PYENV_ROOT' ~/.zshrc; then  
  echo -e '\n# Configuração do Pyenv' >> ~/.zshrc  
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc  
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc  
  echo 'eval "$(pyenv init -)"' >> ~/.zshrc  
fi  
export PYENV_ROOT="$HOME/.pyenv"  
export PATH="$PYENV_ROOT/bin:$PATH"  
eval "$(pyenv init -)"

echo ""  
echo "--- PASSO 7: Instalando o Python 3.12.9 (Isso pode levar alguns minutos) ---"  
pyenv install 3.12.9

echo ""  
echo "--- PASSO 8: Definindo o Python 3.12.9 como padrão global ---"  
pyenv global 3.12.9

echo "--- PASSO 9: Atualizando o pip"  
pip install --upgrade pip

echo ""  
echo "-------------------------------------------------------------"  
echo " SUCESSO! Ambiente corrigido e Python 3.12.9 instalado."  
echo "-------------------------------------------------------------"  
echo ""  
echo "Feche e reabra seu terminal para que tudo funcione corretamente, então verifique com:"  
echo "python --version"  
echo ""
```

### **Um Terminal com Superpoderes: zsh e Oh My Zsh**

Sou muito exigente com meu terminal. É onde passo boa parte do meu dia, e ele precisa ser rápido, inteligente e visualmente agradável. Por isso, a primeira coisa que faço em qualquer ambiente novo é substituir o bash padrão pelo zsh e turbiná-lo com o framework **Oh My Zsh**.

O zsh por si só já é um shell mais poderoso, mas com Oh My Zsh e alguns plugins, ele se transforma. Meus plugins indispensáveis são:

* **zsh-syntax-highlighting:** Colore os comandos em tempo real, te mostrando se um comando existe ou se você digitou algo errado antes mesmo de apertar Enter.  
* **zsh-autosuggestions:** Sugere comandos com base no seu histórico enquanto você digita, como um autocompletar mágico.

Exercício Prático: Instalando o Terminal Perfeito  
Este script instala o zsh, o Oh My Zsh e os plugins que eu uso.

* **Objetivo:** Configurar um terminal moderno e productivo.  
* **Nome do Arquivo:** `setup_zsh.sh`  
* **Dependências:** zsh, git, curl  
* **Comando de Execução:** ````sh
bash setup_zsh.sh
````

```sh
#!/bin/bash

# Atualiza os pacotes e instala o Zsh  
sudo apt update  
sudo apt install -y zsh

# Define o Zsh como o shell padrão para o usuário atual  
# Pode ser necessário inserir a senha aqui, dependendo das permissões do sudo  
sudo usermod -s /usr/bin/zsh $(whoami)

# Instala o Oh My Zsh sem iniciar um novo shell  
export RUNZSH=no  
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Clona os plugins do zsh-syntax-highlighting e zsh-autosuggestions  
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting  
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Edita a linha de plugins no ~/.zshrc usando sed  
sed -i 's/^plugins=(.*/plugins=(git zsh-syntax-highlighting zsh-autosuggestions)/' ~/.zshrc

source ~/.zshrc

echo "Instalação e configuração do Zsh e Oh My Zsh concluídas!"  
echo "Por favor, reinicie seu terminal ou faça logout e login para que as alterações entrem em vigor."

# Inicia uma nova sessão Zsh para aplicar as alterações (opcional)  
exec zsh
```

### **Segurança e Conveniência com Git: Chaves SSH**

Quando você clona, faz *push* ou *pull* de um repositório no GitHub, você precisa se autenticar. A forma mais comum é via HTTPS, que te pede o nome de usuário e senha (ou um token de acesso pessoal) toda vez. É seguro, mas repetitivo.

Uma forma muito mais segura e conveniente é usar **chaves SSH**. Você gera um par de chaves: uma pública, que você adiciona à sua conta do GitHub, e uma privada, que fica segura no seu computador. Quando você se conecta, o Git usa esse par de chaves para te autenticar sem que você precise digitar nada.

**Vantagens de usar SSH:**

* **Conveniência:** Chega de digitar senhas. Uma vez configurado, é automático.  
* **Segurança Aprimorada:** Chaves SSH são criptograficamente muito mais fortes que senhas. É praticamente impossível alguém adivinhar sua chave privada.  
* **Gerenciamento:** Você pode ter múltiplas chaves para diferentes máquinas e revogar o acesso de uma delas a qualquer momento sem afetar as outras.

**Exercício Prático: Gerando sua Chave SSH para o GitHub**

* **Objetivo:** Criar um par de chaves SSH e exibi-lo para que possa ser adicionado ao GitHub.  
* **Nome do Arquivo:** generate\_ssh\_key.sh  
* **Dependências:** openssh-client  
* **Comando de Execução:** ```sh
bash generate_ssh_key.sh
```

```sh
#!/bin/bash  
# Substitua o email pelo seu email do GitHub  
ssh-keygen -t rsa -b 4096 -C "igor@igormedeiros.com.br"

# Inicia o ssh-agent em background  
eval "$(ssh-agent -s)"

# Adiciona sua chave SSH privada ao ssh-agent  
ssh-add ~/.ssh/id_rsa

# Exibe a chave pública para que você possa copiá-la  
echo "Copie a chave pública abaixo e cole nas configurações do seu GitHub:"  
cat ~/.ssh/id_rsa.pub
```

Depois de executar o script, copie a saída (que começa com ssh-rsa...) e cole-a na seção "SSH and GPG keys" das configurações da sua conta no GitHub. A partir de agora, ao clonar repositórios, use a URL SSH em vez da HTTPS.

### **Minhas Ferramentas de Batalha: VS Code**

Meu editor de código de escolha é o **Visual Studio Code**. Ele é leve, rápido e insanamente extensível. Mas, assim como o terminal, eu tenho minhas manias e customizações.

A primeira coisa que faço em uma instalação nova é instalar o tema **Dracula Official**. Não sei se tenho algum grau de dislexia, mas suspeito que sim, pois o contraste visual é extremamente importante para mim. O tema Dracula, com seu fundo escuro e cores vibrantes, torna o código muito mais legível e menos cansativo para os meus olhos.

A segunda extensão é o **Eclipse Keymap**. Confesso: programei em Java usando o Eclipse por mais de 12 anos. Os atalhos de teclado estão gravados na minha memória muscular. Tentar me adaptar aos atalhos padrão do VS Code seria uma batalha perdida. Essa extensão me permite usar todos os atalhos do Eclipse que eu amo, tornando a transição para o Python muito mais suave. Um dia eu encaro o desafio de mudar para não depender de mais uma extensão, mas esse dia ainda não chegou.

### **Gerenciando Dependências: A Revolução do uv e pyproject.toml**

Agora que temos o Python certo e um terminal turbinado, precisamos falar sobre como gerenciar as bibliotecas do nosso projeto (as dependências). Por muito tempo, o mundo Python viveu com o arquivo requirements.txt e o comando pip. Funcionava, mas era lento e, às vezes, levava a inconsistências.

A comunidade Python, sempre em evolução, nos deu uma solução muito mais moderna e robusta. A conversa começou com a PEP 518, que introduziu o arquivo **pyproject.toml**. A ideia era simples: ter um único arquivo para declarar as dependências de construção do projeto. Isso resolveu o problema de "como instalar as ferramentas para construir o seu projeto?". Depois, a PEP 621 expandiu isso, permitindo que a gente definisse quase todas as metadados do projeto (nome, versão, autor, e claro, as dependências) nesse mesmo arquivo. O pyproject.toml se tornou o padrão para projetos Python modernos.

Mas faltava uma peça: uma ferramenta que fosse rápida e inteligente para ler esse arquivo e gerenciar nosso ambiente. E então, os criadores do ruff (um linter de Python absurdamente rápido) nos deram o **uv**.

uv é um gerenciador de pacotes e ambientes virtuais escrito em Rust. E, meu amigo, ele é rápido. Coisas que levavam minutos com pip agora levam segundos. Ele foi projetado para ser um substituto direto para pip e virtualenv, mas com uma performance de 10 a 100 vezes melhor.

**Por que usar uv?**

* **Velocidade:** É a maior vantagem. Instalar e resolver dependências é incrivelmente rápido.  
* **Tudo em um:** uv cria e gerencia ambientes virtuais automaticamente. Você não precisa mais de python \-m venv e pip como ferramentas separadas.  
* **Cache Inteligente:** Ele usa um cache global para evitar baixar a mesma dependência várias vezes, economizando disco e tempo.  
* **Compatibilidade:** Ele entende pyproject.toml e também os antigos requirements.txt, então a migração é super tranquila.

A partir de agora, todos os nossos comandos de instalação usarão uv. Ele vai criar um ambiente virtual para nós na primeira vez que adicionarmos uma dependência e manter tudo organizado no pyproject.toml.

### **Gerenciando Segredos: Chaves de API e Variáveis de Ambiente**

Para usar modelos de IA como os do Google Gemini, você precisará de uma **chave de API (API Key)**. É extremamente importante que você **nunca, jamais, em hipótese alguma**, coloque sua chave de API diretamente no seu código-fonte, especialmente se você planeja compartilhar esse código ou versioná-lo com o Git. Isso seria como deixar a chave da sua casa debaixo do tapete da porta.

A prática correta é usar **variáveis de ambiente**. A biblioteca python-dotenv nos ajuda a carregar essas variáveis de um arquivo para o nosso ambiente.

Como obter sua chave de API gratuita do Google Gemini:  
O Google oferece uma camada gratuita muito generosa para desenvolvedores que querem experimentar a API Gemini. A maneira mais fácil de obter uma chave é através do Google AI Studio.

1. Vá para aistudio.google.com/apikey.  
2. Faça login com sua conta do Google.  
3. Clique em "Create API key in new project".  
4. Copie a chave gerada. É isso\! Você não precisa configurar um projeto complexo no Google Cloud ou adicionar um cartão de crédito para começar.

**Configurando a chave no seu projeto:**

1. **Crie um arquivo .env:** Na raiz da pasta do seu projeto, crie um arquivo chamado .env.  
2. **Adicione sua chave de API ao arquivo .env:** Abra o arquivo .env e adicione sua chave da seguinte forma:  
   GOOGLE\_API\_KEY="sua\_chave\_api\_aqui"

3. **Ignore o arquivo .env no Git:** Para garantir que você nunca envie acidentalmente seus segredos para um repositório público, crie um arquivo chamado .gitignore na raiz do seu projeto e adicione a seguinte linha a ele:  
   # Ambiente virtual  
   .venv/

   # Arquivo de segredos  
   .env

   # Cache do Python  
   \_\_pycache\_\_/

É fundamental ir além de apenas esconder as chaves. Adote o **princípio do menor privilégio**: suas chaves de API devem ter apenas as permissões mínimas necessárias para a tarefa que irão executar. Por exemplo, se uma chave só precisa ler dados, ela não deve ter permissão para escrever ou deletar. Para ambientes de produção, considere o uso de serviços de gerenciamento de segredos como Azure KeyVault ou AWS Secret Manager. É crucial entender que o ambiente de estudos e prototipagem, onde a conveniência é prioridade, difere significativamente de um ambiente de produção, que exige rigorosas práticas de segurança corporativa, como auditorias regulares, controle de acesso baseado em função (RBAC) e monitoramento contínuo. Além disso, a **rotação periódica de chaves** é uma boa prática de segurança. Defina um cronograma para gerar novas chaves e invalidar as antigas, minimizando o risco em caso de vazamento.

### **Considerações sobre Hardware**

Antes de encerrar este capítulo sobre ambiente, é importante tocar em um ponto que muitos desenvolvedores de IA enfrentam: o hardware. Especialmente se você planeja experimentar com modelos de linguagem locais (como os que rodam via Ollama, que abordaremos mais adiante), a capacidade da sua máquina se torna um fator crucial.

Eu, por exemplo, tenho um PC servidor de LLM em casa. É uma máquina modesta, com uma RTX 4060 de 8GB de VRAM. Para muitos, 8GB pode parecer pouco, e de fato, limita o tamanho dos modelos que consigo rodar eficientemente (geralmente até modelos de 8 bilhões de parâmetros). Mas mesmo com essa configuração, consigo gerar respostas a uma taxa de 40+ tokens por segundo, o que é incrivelmente rápido para experimentação e desenvolvimento local. Essa experiência me ensinou que não é preciso ter um supercomputador para começar a explorar o mundo dos LLMs locais, mas entender as limitações do seu hardware é fundamental para gerenciar as expectativas e otimizar seus experimentos.

**Troubleshooting Comum:**

*   **`command not found: pyenv` ou `python: command not found`:** Certifique-se de que você fechou e reabriu seu terminal após a instalação do `pyenv` e a configuração do `.zshrc` (ou `.bashrc`). O `pyenv init` precisa ser executado para que o `pyenv` seja carregado corretamente no seu shell.
*   **`pip is configured with locations that require TLS/SSL, however the ssl module in Python was not available`:** Este erro geralmente ocorre em ambientes Linux onde as bibliotecas SSL necessárias para compilar o Python não estão instaladas. Certifique-se de que você executou o script `setup_python_kali.sh` e que todas as dependências (`libssl-dev`, `zlib1g-dev`, etc.) foram instaladas com sucesso.
*   **Problemas com `uv` ou `pip`:** Se você encontrar erros ao instalar pacotes, verifique sua conexão com a internet. Para problemas persistentes, tente limpar o cache do `uv` (`uv cache clean`) ou do `pip` (`pip cache purge`).
*   **Variáveis de Ambiente não Carregadas:** Se seu código Python não conseguir encontrar a `GOOGLE_API_KEY` ou outras variáveis de ambiente, verifique se o arquivo `.env` está na raiz do seu projeto ou no diretório do capítulo. Certifique-se de que o nome da variável no `.env` corresponde exatamente ao que você está tentando acessar no código (ex: `GOOGLE_API_KEY`).
*   **Permissões de Execução em Scripts Shell:** Lembre-se de dar permissão de execução aos scripts `.sh` com `chmod +x nome_do_script.sh` antes de executá-los.

### **Resumo do Capítulo**

Neste capítulo, montamos um ambiente de desenvolvimento Python profissional, robusto e seguro, preparando o terreno para construir aplicações de IA de alta qualidade.

* **Ambiente Linux:** Discutimos as vantagens de desenvolver em um ambiente Linux (via WSL) para garantir compatibilidade com as ferramentas e servidores de produção.  
* **Gerenciamento de Versões com pyenv:** Aprendemos a instalar e usar o pyenv para gerenciar múltiplas versões do Python sem conflitos, garantindo consistência entre projetos e equipes.  
* **Terminal e Git:** Turbinamos nosso terminal com zsh e Oh My Zsh para maior produtividade e configuramos chaves SSH para interagir com o GitHub de forma mais segura e conveniente.  
* **Gerenciamento de Dependências com uv:** Exploramos a evolução do gerenciamento de pacotes em Python, desde o setup.py até o moderno pyproject.toml (PEPs 518 e 621), e adotamos o uv como nossa ferramenta principal por sua velocidade e simplicidade.  
* **Gerenciamento de Segredos:** Vimos a importância de nunca expor chaves de API no código e aprendemos o passo a passo para obter uma chave gratuita do Google AI Studio e configurá-la de forma segura usando um arquivo .env.



### **Pontos Chave**

*   Um ambiente de desenvolvimento bem configurado (Linux/WSL, pyenv, zsh) é crucial para produtividade em IA.
*   Gerenciamento de dependências com `uv` e `pyproject.toml` oferece velocidade e consistência.
*   A segurança das chaves de API (variáveis de ambiente, `.env`, `.gitignore`) é fundamental para qualquer projeto de IA.
*   Compreender as limitações de hardware é importante ao trabalhar com LLMs locais.

### **Teste seu Conhecimento**

1. Qual é a principal vantagem de usar o WSL (Windows Subsystem for Linux) para desenvolvimento Python?  
   a) Ele permite rodar jogos de Windows no Linux.  
   b) Ele oferece um ambiente de desenvolvimento semelhante ao de produção, evitando problemas de compatibilidade.  
   c) Ele é a única forma de instalar o Python no Windows.  
   d) Ele melhora a performance gráfica de aplicações.  
2. Para que serve a ferramenta pyenv?  
   a) Para escrever código Python mais rápido.  
   b) Para gerenciar as dependências de um projeto, como o LangChain.  
   c) Para instalar e alternar entre múltiplas versões do Python no mesmo sistema.  
   d) Para criar interfaces gráficas para aplicações Python.  
3. Qual arquivo é o padrão moderno para definir as dependências e metadados de um projeto Python, conforme as PEPs 518 e 621?  
   a) requirements.txt  
   b) setup.py  
   c) config.yml  
   d) pyproject.toml  
4. Por que é recomendado usar chaves SSH em vez de HTTPS para interagir com o GitHub?  
   a) Porque é mais rápido para baixar arquivos grandes.  
   b) Porque é mais seguro e evita a necessidade de digitar a senha a cada interação.  
   c) Porque o HTTPS não funciona com repositorios privados.  
   d) Porque o SSH permite editar arquivos diretamente no GitHub.  
5. Qual comando você usaria com uv para adicionar uma nova dependência a um projeto e registrá-la no pyproject.toml?  
   a) uv install \<pacote\>  
   b) uv pip install \<pacote\>  
   c) uv add \<pacote\>  
   d) uv sync \<pacote\>

*(Respostas: 1-b, 2-c, 3-d, 4-b, 5-c)*

## **Capítulo 3: Manipulação de Prompts e Modelos de Linguagem com LangChain**

### **A Arte e a Ciência da Engenharia de Prompts**

Se os modelos de linguagem são como gênios poderosos, os prompts são os nossos pedidos. A forma como fazemos o pedido — as palavras que usamos, a estrutura que damos, o contexto que fornecemos — determina drasticamente a qualidade da resposta que recebemos. Isso é o que chamamos de **Engenharia de Prompts**: a disciplina de projetar e otimizar as instruções dadas aos modelos de linguagem para obter os resultados desejados.

Não se trata de "adivinhar" as palavras mágicas. É uma disciplina que mistura criatividade, lógica e experimentação. Um bom prompt é claro, conciso e específico. Ele guia o modelo, em vez de deixá-lo vagando. O LangChain nos oferece ferramentas fantásticas para elevar nossa engenharia de prompts de simples strings para templates dinâmicos e reutilizáveis.

### **Templates de Prompt: Reutilização e Dinamismo**

Imagine que você está construindo um assistente que resume artigos. Uma abordagem ingênua seria escrever o prompt toda vez no código:

```python
# Abordagem ingênua (não faça isso!)
artigo = "..." # texto longo do artigo
prompt_texto = f"Resuma o seguinte artigo em três pontos principais: {artigo}"
```

Isso funciona, mas é inflexível e ruim de manter. E se você quiser mudar o estilo do resumo? Ou o número de pontos? Você teria que caçar e alterar essa string em todo o seu código.

É aqui que os PromptTemplate do LangChain entram em cena. Eles nos permitem criar um modelo para nossos prompts, com espaços reservados (variáveis) que preenchemos depois.

Vamos ver como funciona. A classe principal para isso é a ChatPromptTemplate, projetada para os modernos modelos de chat.

```python
from langchain_core.prompts import ChatPromptTemplate

# Criando um template para um sistema de resumo
template_string = """Você é um assistente especialista em resumir textos.
Resuma o texto a seguir em {numero_de_pontos} pontos principais, em um tom {tom}.

Texto:
{texto_do_artigo}
"""

prompt_template = ChatPromptTemplate.from_template(template_string)

# Agora, podemos usar o template para formatar um prompt dinamicamente
artigo_exemplo = "A inteligência artificial está transformando indústrias, desde a saúde até as finanças, automatizando tarefas e gerando novos insights."
prompt_formatado = prompt_template.format(
    numero_de_pontos="dois",
    tom="profissional",
    texto_do_artigo=artigo_exemplo
)

print(prompt_formatado)
```

A saída será o prompt completo, pronto para ser enviado ao modelo:

text='Você é um assistente especialista em resumir textos.\\nResuma o texto a seguir em dois pontos principais, em um tom profissional.\\n\\nTexto:\\nA inteligência artificial está transformando indústrias, desde a saúde até as finanças, automatizando tarefas e gerando novos insights.\\n'

A beleza disso é a modularidade. Podemos facilmente mudar o número de pontos, o tom ou o artigo sem tocar na estrutura do template.

**Nota Pessoal:** Para alguns, um terminal de computador é uma tela preta, fria e sem vida. Para mim, quando estou no meu terminal Linux Kali com o shell Zsh todo customizado, me sinto como se estivesse prestes a tocar o solo de guitarra de "Hotel California" dos Eagles. Existe uma fluidez, uma arte, um prazer em fazer as ferramentas responderem exatamente como você quer, com o mínimo de esforço. É uma dança entre o homem e a máquina.

A engenharia de prompts é exatamente assim. Não é apenas sobre a técnica de encaixar variáveis em um template. É sobre encontrar o "feeling" certo, a combinação de palavras e estrutura que faz o modelo "cantar". É sobre a elegância de criar um prompt tão bem construído que a resposta do LLM parece mágica, mas na verdade é o resultado de um design cuidadoso.

Neste capítulo, vamos aprender a ser os guitarristas dos nossos LLMs. Vamos afinar nossos instrumentos (os templates) e aprender as escalas (as técnicas de prompt) para criar solos de informação que sejam precisos, criativos e impactantes.

### **Integrando Modelos de Linguagem (LLMs)**

Um prompt, por si só, é apenas texto. Ele precisa ser enviado a um modelo para ganhar vida. Como vimos, vamos usar o Gemini do Google.

```python
# Supondo que você já configurou seu ambiente como no Capítulo 2
from langchain_google_genai import ChatGoogleGenerativeAI

# Inicializa o modelo
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
# 'temperature' é um parâmetro que controla a criatividade da resposta.
# 0 é mais determinístico, 1 é mais criativo.

Agora, como conectamos nosso prompt_template com nosso llm? A maneira moderna de fazer isso no LangChain é usando a **LangChain Expression Language (LCEL)**, que utiliza o operador pipe (|). Vamos ter um capítulo inteiro sobre isso (Capítulo 4), mas já vou te dar um gostinho.

# Conectando o prompt ao modelo usando LCEL
chain = prompt_template | llm

# Agora, podemos invocar a "chain" diretamente com as variáveis
response = chain.invoke({
    "numero_de_pontos": "três",
    "tom": "entusiasmado",
    "texto_do_artigo": "O LangChain permite construir aplicações de IA complexas de forma modular e eficiente, abrindo um novo mundo de possibilidades para desenvolvedores Python."
})

print(response.content)
```
```

Veja como ficou limpo e legível? prompt\_template | llm cria um pipeline onde a saída do template (o prompt formatado) se torna a entrada para o modelo. A mágica da orquestração do LangChain em ação\!

### **Exercício Prático: Um Tradutor Multilíngue Dinâmico**

Vamos solidificar esses conceitos com um exercício prático. Construiremos uma pequena aplicação que traduz uma frase para um idioma de destino especificado pelo usuário.

* **Objetivo:** Criar uma chain que usa um ChatPromptTemplate dinâmico para instruir um LLM a realizar traduções.  
* **Nome do Arquivo:** `exercicios/capitulo_03/exercicio_1/main.py`  
* **Dependências:** `langchain`, `langchain-google-genai`, `python-dotenv`  
* **Comando de Instalação:** `uv add langchain langchain-google-genai python-dotenv`

```python
# exercicios/capitulo_03/exercicio_1/main.py

import os  
from dotenv import load_dotenv  
from langchain_core.prompts import ChatPromptTemplate  
from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain_core.output_parsers import StrOutputParser

# Carregar variáveis de ambiente do arquivo .env  
load_dotenv()

def traduzir_texto(texto_original: str, idioma_destino: str) -> str:  
    """  
    Traduz um texto para o idioma de destino usando LangChain e Google Gemini.

    Args:  
        texto_original: O texto a ser traduzido.  
        idioma_destino: O idioma para o qual o texto será traduzido.

    Returns:  
        O texto traduzido.  
    """  
    print(f"Traduzindo '{texto_original}' para {idioma_destino}...")

    # 1. Definir o template do prompt  
    template = """  
    Sua tarefa é ser um tradutor expert.  
    Traduza o seguinte texto para o idioma '{idioma}':  
      
    Texto Original: "{texto}"  
      
    Tradução:  
    """  
    prompt = ChatPromptTemplate.from_template(template)

    # 2. Inicializar o modelo  
    # A temperatura 0 torna a tradução mais literal e menos "criativa"  
    modelo = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

    # 3. Inicializar o parser de saída para obter uma string como resultado  
    output_parser = StrOutputParser()

    # 4. Criar a chain usando LangChain Expression Language (LCEL)  
    chain = prompt | modelo | output_parser

    # 5. Invocar a chain com os parâmetros necessários  
    try:  
        resultado = chain.invoke({
            "idioma": idioma_destino,  
            "texto": texto_original  
        })  
        return resultado  
    except Exception as e:  
        return f"Ocorreu um erro durante a tradução: {e}"

# --- Execução do Exemplo ---
if __name__ == "__main__":  
    # Exemplo 1: Traduzindo para o Francês  
    frase_pt = "A inteligência artificial está mudando o mundo."  
    traducao_fr = traduzir_texto(frase_pt, "Francês")  
    print(f"Resultado: {traducao_fr}\n")

    # Exemplo 2: Traduzindo para o Japonês  
    frase_en = "Python is a powerful programming language."  
    traducao_jp = traduzir_texto(frase_en, "Japonês")  
    print(f"Resultado: {traducao_jp}\n")  
      
    # Exemplo 3: Traduzindo para o Klingon (para testar a criatividade do modelo)  
    frase_nerd = "Hello, world!"  
    traducao_klingon = traduzir_texto(frase_nerd, "Klingon")  
    print(f"Resultado: {traducao_klingon}\n")
```
```

**Comando de Execução (Linux/macOS):**

```sh
# Dê permissão de execução ao script
chmod +x exercicios/capitulo_03/exercicio_1/run.sh

# Execute o exercício
./exercicios/capitulo_03/exercicio_1/run.sh
```
```

**Comando de Execução (Windows):**

```bat
REM Execute o exercício no Windows
exercicios\capulo_03\exercicio_1\run.bat
```

**Saída Esperada (pode variar ligeiramente):**

Traduzindo 'A inteligência artificial está mudando o mundo.' para Francês...
Resultado: L'intelligence artificielle change le monde.

Traduzindo 'Python is a powerful programming language.' para Japonês...
Resultado: パイソンは強力なプログラミング言語です。

Traduzindo 'Hello, world\!' para Klingon...
Resultado: nuqneH, yaj\!

Este simples exercício demonstra o poder da combinação de prompts dinâmicos e modelos de linguagem, orquestrados de forma limpa e eficiente pelo LangChain. Agora que dominamos os blocos de construção individuais, estamos prontos para o próximo capítulo, onde aprenderemos a construir pipelines muito mais complexos e inteligentes.

**Troubleshooting Comum:**

*   **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Certifique-se de que você obteve sua `GOOGLE_API_KEY` do Google AI Studio e a adicionou corretamente ao seu arquivo `.env` na raiz do projeto. Este erro é comum se a chave estiver ausente ou incorreta.
*   **Respostas Inesperadas/"Alucinações":** Se o modelo não traduzir corretamente ou "inventar" algo, verifique a clareza do seu `prompt_template`. Para tarefas de tradução, uma `temperature=0` (como usado no exemplo) ajuda a tornar a resposta mais literal e menos criativa. Se o problema persistir, o modelo pode não ter sido treinado para o idioma específico (como Klingon, que é um teste de criatividade).
*   **Erros de Conexão:** Problemas de rede ou limites de taxa da API podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.

### **Resumo do Capítulo**

Neste capítulo, mergulhamos na arte e ciência da engenharia de prompts e como o LangChain nos ajuda a dominar essa habilidade.

* **Engenharia de Prompts:** Entendemos que a qualidade da nossa interação com um LLM depende diretamente da clareza e estrutura das nossas instruções (prompts).  
* **Templates de Prompt:** Vimos como os PromptTemplates do LangChain nos permitem criar prompts dinâmicos e reutilizáveis, evitando código repetitivo e tornando nossas aplicações mais modulares.  
* **Integração de LLMs:** Aprendemos a inicializar um LLM (especificamente o gemini-1.5-flash do Google) e a conectá-lo a um prompt template.  
* **Primeiro Vislumbre da LCEL:** Tivemos uma prévia da LangChain Expression Language (LCEL) e seu operador pipe (|), que cria um pipeline legível e elegante para conectar os componentes.  
* **Exercício Prático:** Construímos um tradutor multilíngue, solidificando o conhecimento de como usar variáveis dinâmicas em um prompt para criar uma aplicação flexível.



### **Pontos Chave**

*   A Engenharia de Prompts é crucial para obter respostas de qualidade dos LLMs.
*   `PromptTemplates` no LangChain permitem prompts dinâmicos e reutilizáveis.
*   LLMs são integrados e orquestrados eficientemente com o LangChain.
*   A LCEL simplifica a construção de pipelines, tornando-os mais legíveis e eficientes.
*   A prática com exercícios como o tradutor multilíngue solidifica o aprendizado dos conceitos de prompts e modelos.

### **Teste seu Conhecimento**

1. Qual é o principal benefício de usar PromptTemplates em vez de strings formatadas (f-strings)?  
   a) PromptTemplates são mais rápidos de executar.  
   b) Eles permitem criar prompts modulares, reutilizáveis e mais fáceis de manter.  
   c) Apenas PromptTemplates podem ser usados com modelos de chat.  
   d) Eles usam menos tokens de API.  
2. No exemplo do tradutor, qual componente foi responsável por transformar a saída do modelo de um objeto de mensagem para uma string simples?  
   a) ChatGoogleGenerativeAI  
   b) ChatPromptTemplate  
   c) StrOutputParser  
   d) load\_dotenv  
3. O que o parâmetro temperature em um LLM geralmente controla?  
   a) A velocidade da resposta.  
   b) O custo da chamada de API.  
   c) O quão criativa ou determinística é a resposta (aleatoriedade).  
   d) O idioma da resposta.  
4. Qual é a principal função da LangChain Expression Language (LCEL) e seu operador |?  
   a) Realizar operações matemáticas.  
   b) Conectar (encadear) diferentes componentes do LangChain, como prompts e modelos, em um pipeline.  
   c) Definir variáveis de ambiente.  
   d) Imprimir a saída no console.  
5. No exemplo do tradutor, se você quisesse que a tradução fosse o mais literal e menos criativa possível, qual valor você escolheria para temperature?  
   a) 1.0  
   b) 0.7  
   c) 0.5  
   d) 0.0

*(Respostas: 1-b, 2-c, 3-c, 4-b, 5-d)*

## **Capítulo 4: Construção de Pipelines: Da SequentialChain à LCEL**

### **A Evolução das Chains: Do Imperativo ao Declarativo**

Nos primeiros dias do LangChain, a forma de construir fluxos de trabalho era através de classes como LLMChain e SequentialChain. Essa abordagem, embora funcional, era o que chamamos de **imperativa**: você instanciava objetos e os conectava de forma mais verbosa, o que tornava o código mais difícil de ler e manter. Era como dar instruções passo a passo para montar um móvel, detalhando cada parafuso.

O time do LangChain percebeu que poderia haver uma maneira melhor, mais intuitiva e mais poderosa. Uma maneira que fosse **declarativa**, onde você simplesmente descreve o fluxo de dados — como um diagrama de montagem — e o framework se encarrega da execução otimizada.

Essa percepção deu origem à **LangChain Expression Language (LCEL)**, lançada em agosto de 2023\. A LCEL é, sem dúvida, uma das inovações mais importantes do framework e é a maneira moderna e recomendada de construir qualquer tipo de pipeline.

Neste capítulo, vamos fazer uma viagem no tempo. Primeiro, vamos construir uma chain "à moda antiga" para entender as dores que a LCEL veio resolver. Depois, vamos mergulhar de cabeça na LCEL e ver como ela torna nossa vida muito mais fácil.

### **O Jeito Clássico: LLMChain e SequentialChain (OBSOLETO)**

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
```

**Comando de Execução (Windows):**

```bat
REM Execute o exercício no Windows
exercicios\capitulo_04\exercicio_1\run.bat
```

Isso funciona, mas note a verbosidade. Precisamos definir `output_key` para cada `LLMChain` e depois listar todas as `input_variables` e `output_variables` na `SequentialChain`. Fica complexo rapidamente. A LCEL resolve isso de forma muito mais elegante e eficiente.

**Troubleshooting Comum:**

*   **`DeprecationWarning`:** Este é um aviso esperado, pois estamos usando classes legadas (`LLMChain`, `SequentialChain`). Ele serve para reforçar a importância de migrar para a LCEL em novos projetos.
*   **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Certifique-se de que sua chave de API do Google está corretamente configurada no arquivo `.env`.
*   **Erros de Conexão:** Problemas de rede ou limites de taxa da API podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.


### **A Revolução da LCEL: Por que Devemos Usá-la?**

A LCEL não é apenas uma "sintaxe mais bonita"; ela é uma **linguagem declarativa para compor Runnables**, destravando funcionalidades cruciais de forma quase automática e transformando o LangChain de uma ferramenta de prototipagem para uma ferramenta pronta para produção.

* **Streaming Nativo:** Obtenha respostas do modelo token a token com o método .stream(). Isso melhora drasticamente a experiência do usuário em aplicações de chat, que não precisa mais esperar a resposta completa.  
* **Suporte Assíncrono Garantido:** Qualquer chain LCEL pode ser executada de forma não-bloqueante com .ainvoke(). Isso é essencial para servidores web que precisam lidar com múltiplas requisições simultaneamente.  
* **Execução Paralela Otimizada:** A LCEL pode executar múltiplos componentes ao mesmo tempo para otimizar a latência, simplesmente definindo um dicionário de Runnables.  
* **Integração Total com LangSmith:** Tenha rastreabilidade completa de cada passo do seu pipeline, facilitando o debug e a observabilidade, algo que era muito mais complexo com as chains antigas.  
* **Interface Unificada (Runnable):** Quase tudo no LangChain moderno implementa a interface Runnable. Isso significa que prompts, modelos, parsers e até funções Python podem ser encadeados da mesma forma, usando o operador pipe (|), tornando o código mais limpo, legível e modular.

### **LCEL na Prática: Exercícios Essenciais**

A melhor forma de entender a LCEL é colocando a mão na massa. Vamos passar por uma série de exercícios que demonstram seus principais recursos.

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
```

**Comando de Execução (Windows):**

```bat
REM Execute o exercício no Windows
exercicios\capitulo_04\exercicio_2\run.bat
```


**Troubleshooting Comum para Exercícios LCEL (Capítulo 4):**

*   **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Verifique se sua `GOOGLE_API_KEY` está corretamente configurada no arquivo `.env`.
*   **`ValidationError` ou Erros de Schema:** Se você estiver usando parsers de saída (como `JsonOutputParser`), certifique-se de que o formato da saída do LLM corresponde ao schema esperado. Pequenas variações na resposta do modelo podem causar esses erros.
*   **Erros de Conexão:** Problemas de rede ou limites de taxa da API podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.
*   **Saída Inesperada do LLM:** Se o LLM não estiver respondendo como esperado, revise o `ChatPromptTemplate`. A clareza e especificidade do prompt são cruciais. Experimente ajustar a `temperature` do modelo (um valor mais baixo, como `0.0`, torna o modelo mais determinístico).
*   **Problemas com `RunnablePassthrough` ou `RunnableParallel`:** Verifique se as chaves dos dicionários de entrada e saída estão corretas e se os dados estão fluindo conforme o esperado entre os componentes da chain. Use `chain.invoke({'input': ...})` e inspecione a saída de cada etapa se possível.

```
```

**Comando de Execução:**

```sh
chmod +x execucao_exercicio_4_1.sh
./execucao_exercicio_4_1.sh
```


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
```

**Comando de Execução (Windows):**

```bat
REM Execute o exercício no Windows
exercicios\capitulo_04\exercicio_3\run.bat
```

**Troubleshooting Comum para Exercícios LCEL (Capítulo 4):**

*   **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Verifique se sua `GOOGLE_API_KEY` está corretamente configurada no arquivo `.env`.
*   **`ValidationError` ou Erros de Schema:** Se você estiver usando parsers de saída (como `JsonOutputParser`), certifique-se de que o formato da saída do LLM corresponde ao schema esperado. Pequenas variações na resposta do modelo podem causar esses erros.
*   **Erros de Conexão:** Problemas de rede ou limites de taxa da API podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.
*   **Saída Inesperada do LLM:** Se o LLM não estiver respondendo como esperado, revise o `ChatPromptTemplate`. A clareza e especificidade do prompt são cruciais. Experimente ajustar a `temperature` do modelo (um valor mais baixo, como `0.0`, torna o modelo mais determinístico).
*   **Problemas com `RunnablePassthrough` ou `RunnableParallel`:** Verifique se as chaves dos dicionários de entrada e saída estão corretas e se os dados estão fluindo conforme o esperado entre os componentes da chain. Use `chain.invoke({'input': ...})` e inspecione a saída de cada etapa se possível.

**Troubleshooting Comum para Exercícios LCEL (Capítulo 4):**

*   **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Verifique se sua `GOOGLE_API_KEY` está corretamente configurada no arquivo `.env`.
*   **`ValidationError` ou Erros de Schema:** Se você estiver usando parsers de saída (como `JsonOutputParser`), certifique-se de que o formato da saída do LLM corresponde ao schema esperado. Pequenas variações na resposta do modelo podem causar esses erros.
*   **Erros de Conexão:** Problemas de rede ou limites de taxa da API podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.
*   **Saída Inesperada do LLM:** Se o LLM não estiver respondendo como esperado, revise o `ChatPromptTemplate`. A clareza e especificidade do prompt são cruciais. Experimente ajustar a `temperature` do modelo (um valor mais baixo, como `0.0`, torna o modelo mais determinístico).
*   **Problemas com `RunnablePassthrough` ou `RunnableParallel`:** Verifique se as chaves dos dicionários de entrada e saída estão corretas e se os dados estão fluindo conforme o esperado entre os componentes da chain. Use `chain.invoke({'input': ...})` e inspecione a saída de cada etapa se possível.


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
```

**Comando de Execução (Windows):**

```bat
REM Execute o exercício no Windows
exercicios\capitulo_04\exercicio_4\run.bat
```

**Troubleshooting Comum para Exercícios LCEL (Capítulo 4):**

*   **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Verifique se sua `GOOGLE_API_KEY` está corretamente configurada no arquivo `.env`.
*   **`ValidationError` ou Erros de Schema:** Se você estiver usando parsers de saída (como `JsonOutputParser`), certifique-se de que o formato da saída do LLM corresponde ao schema esperado. Pequenas variações na resposta do modelo podem causar esses erros.
*   **Erros de Conexão:** Problemas de rede ou limites de taxa da API podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.
*   **Saída Inesperada do LLM:** Se o LLM não estiver respondendo como esperado, revise o `ChatPromptTemplate`. A clareza e especificidade do prompt são cruciais. Experimente ajustar a `temperature` do modelo (um valor mais baixo, como `0.0`, torna o modelo mais determinístico).
*   **Problemas com `RunnablePassthrough` ou `RunnableParallel`:** Verifique se as chaves dos dicionários de entrada e saída estão corretas e se os dados estão fluindo conforme o esperado entre os componentes da chain. Use `chain.invoke({'input': ...})` e inspecione a saída de cada etapa se possível.

**Exercício 4: Usando Funções Python com RunnableLambda**

* **Objetivo:** Criar uma chain que recebe uma lista de números, calcula o quadrado de cada um e depois pede ao LLM para descrever o resultado.

```python
# exercicios/capitulo_04/exercicio_5/main.py  
from dotenv import load_dotenv  
from langchain_core.prompts import ChatPromptTemplate  
from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain_core.output_parsers import StrOutputParser  
from langchain_core.runnables import RunnableLambda

load_dotenv()

def calcular_quadrados(numeros: list[int]) -> list[int]:  
    print("Executando a função Python para calcular quadrados...")  
    return [n*n for n in numeros]

prompt = ChatPromptTemplate.from_template("Descreva esta lista de números de forma poética: {lista_quadrados}")  
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")  
parser = StrOutputParser()

chain = (  
    RunnableLambda(calcular_quadrados)  
    | (lambda quadrados: {"lista_quadrados": quadrados})  
    | prompt  
    | model  
    | parser  
)

print(chain.invoke([1, 2, 3, 4, 5]))
```

**Comando de Execução (Linux/macOS):**

```sh
# Dê permissão de execução ao script
chmod +x exercicios/capitulo_04/exercicio_5/run.sh

# Execute o exercício
./exercicios/capitulo_04/exercicio_5/run.sh
```
```

**Comando de Execução (Windows):**

```bat
REM Execute o exercício no Windows
exercicios\capitulo_04\exercicio_5\run.bat
```

**Troubleshooting Comum para Exercícios LCEL (Capítulo 4):**

*   **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Verifique se sua `GOOGLE_API_KEY` está corretamente configurada no arquivo `.env`.
*   **`ValidationError` ou Erros de Schema:** Se você estiver usando parsers de saída (como `JsonOutputParser`), certifique-se de que o formato da saída do LLM corresponde ao schema esperado. Pequenas variações na resposta do modelo podem causar esses erros.
*   **Erros de Conexão:** Problemas de rede ou limites de taxa da API podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.
*   **Saída Inesperada do LLM:** Se o LLM não estiver respondendo como esperado, revise o `ChatPromptTemplate`. A clareza e especificidade do prompt são cruciais. Experimente ajustar a `temperature` do modelo (um valor mais baixo, como `0.0`, torna o modelo mais determinístico).
*   **Problemas com `RunnablePassthrough` ou `RunnableParallel`:** Verifique se as chaves dos dicionários de entrada e saída estão corretas e se os dados estão fluindo conforme o esperado entre os componentes da chain. Use `chain.invoke({'input': ...})` e inspecione a saída de cada etapa se possível.
*   **Problemas com `RunnableLambda`:** Certifique-se de que a função Python que você está passando para `RunnableLambda` está retornando o tipo de dado esperado pela próxima etapa da chain. Erros de tipo ou formato de dados são comuns aqui.


**Exercício 5: Streaming de Respostas**

* **Objetivo:** Criar uma chain que faz streaming da resposta do LLM, imprimindo-a token por token.

```python
# exercicios/capitulo_04/exercicio_6/main.py  
from dotenv import load_dotenv  
from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain_core.prompts import ChatPromptTemplate  
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_template("Conte uma história curta sobre um robô que aprendeu a sonhar.")  
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")  
parser = StrOutputParser()

chain = prompt | model | parser

print("--- Resposta em Streaming ---")  
for chunk in chain.stream({}):  
    print(chunk, end="", flush=True)  
print("\n--- Fim do Streaming ---")

**Troubleshooting Comum para Exercícios LCEL (Capítulo 4):**

*   **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Verifique se sua `GOOGLE_API_KEY` está corretamente configurada no arquivo `.env`.
*   **`ValidationError` ou Erros de Schema:** Se você estiver usando parsers de saída (como `JsonOutputParser`), certifique-se de que o formato da saída do LLM corresponde ao schema esperado. Pequenas variações na resposta do modelo podem causar esses erros.
*   **Erros de Conexão:** Problemas de rede ou limites de taxa da API podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.
*   **Saída Inesperada do LLM:** Se o LLM não estiver respondendo como esperado, revise o `ChatPromptTemplate`. A clareza e especificidade do prompt são cruciais. Experimente ajustar a `temperature` do modelo (um valor mais baixo, como `0.0`, torna o modelo mais determinístico).
*   **Problemas com `RunnablePassthrough` ou `RunnableParallel`:** Verifique se as chaves dos dicionários de entrada e saída estão corretas e se os dados estão fluindo conforme o esperado entre os componentes da chain. Use `chain.invoke({'input': ...})` e inspecione a saída de cada etapa se possível.
*   **Problemas com `RunnableLambda`:** Certifique-se de que a função Python que você está passando para `RunnableLambda` está retornando o tipo de dado esperado pela próxima etapa da chain. Erros de tipo ou formato de dados são comuns aqui.
*   **Streaming não funciona:** Verifique se você está usando o método `.stream()` corretamente e se o LLM que você está utilizando suporta streaming. Nem todos os LLMs ou APIs oferecem streaming de forma nativa.

**Comando de Execução (Linux/macOS):**

```sh
# Dê permissão de execução ao script
chmod +x exercicios/capitulo_04/exercicio_6/run.sh

# Execute o exercício
./exercicios/capitulo_04/exercicio_6/run.sh
```
```

**Comando de Execução (Windows):**

```bat
REM Execute o exercício no Windows
exercicios\capitulo_04\exercicio_6\run.bat
```
```

Falando em combinar coisas que parecem não combinar, vou contar uma pequena curiosidade sobre mim: eu adoro o ambiente de cafeterias para trabalhar. Aquele burburinho de fundo, a energia das pessoas ao redor... tudo isso me ajuda a focar de uma maneira que o silêncio do escritório em casa não consegue. A ironia? Eu não sou fã de café. Sou o cara estranho em um canto, com uma xícara de chá de camomila, programando freneticamente.

Essa minha peculiaridade me rendeu o apelido de "cliente diferentão" em algumas cafeterias. Mas, assim como a LCEL nos mostra que a combinação de elementos aparentemente díspares pode gerar resultados poderosos e harmoniosos, minha xícara de chá em meio a um mar de expressos é a prova de que a produtividade pode vir de onde menos se espera.

Às vezes, em LangChain, vamos combinar componentes de maneiras inesperadas, como fizemos com a RunnableParallel. Podemos achar que executar tarefas em paralelo pode criar confusão, mas, na verdade, quando orquestrado corretamente, o resultado é surpreendentemente eficiente e harmonioso. É como a minha produtividade movida a chá em meio a um mar de expressos: funciona, e funciona muito bem.

### **Checklist de Construção de Pipelines**

* \[ \] Definir claramente o objetivo do pipeline e as etapas necessárias para alcançá-lo.  
* \[ \] Usar a sintaxe LCEL (|) para compor Runnables (prompts, modelos, parsers, funções).  
* \[ \] Garantir a passagem correta de dados entre as etapas, usando dicionários e RunnablePassthrough quando necessário.  
* \[ \] Utilizar RunnableParallel para otimizar a latência executando tarefas independentes ao mesmo tempo.  
* \[ \] Integrar lógica customizada usando RunnableLambda quando necessário.  
* \[ \] Implementar streaming (.stream()) para melhorar a experiência do usuário em aplicações interativas.  
* \[ \] Incluir monitoramento e logging (idealmente com LangSmith) para acompanhar a execução e identificar falhas.  
* \[ \] Testar o pipeline com diferentes entradas para validar a robustez e a eficiência.  
* \[ \] Documentar o fluxo e as dependências para facilitar a manutenção futura.





### **Pontos Chave**
*   A LCEL é a forma moderna e recomendada de construir pipelines no LangChain, oferecendo streaming, suporte assíncrono e execução paralela nativamente.
*   `RunnablePassthrough`, `RunnableParallel`, e `RunnableLambda` são componentes chave para construir pipelines flexíveis e eficientes.
*   A transição de abordagens imperativas para declarativas (LCEL) simplifica o código e melhora a performance.

### **Teste seu Conhecimento**

1. Qual era a principal desvantagem da abordagem clássica com SequentialChain?  
   a) Não era possível conectar mais de duas chains.  
   b) Era verbosa e exigia a definição manual de input\_variables e output\_variables.  
   c) Não funcionava com modelos de chat.  
   d) Era mais rápida que a LCEL.  
2. Qual dos seguintes é um benefício fundamental da LCEL que não estava facilmente disponível nas chains clássicas?  
   a) A capacidade de usar prompts.  
   b) Suporte nativo para streaming, batch e execução assíncrona.  
   c) A capacidade de usar modelos do Google.  
   d) A necessidade de definir output\_key.  
3. No contexto da LCEL, o que o RunnablePassthrough faz?  
   a) Ignora completamente a entrada e passa um valor fixo.  
   b) Passa a entrada original de uma chain para uma etapa posterior, sem modificá-la.  
   c) Executa uma função Python.  
   d) Converte a saída para uma string.  
4. Se você tem duas tarefas independentes que podem ser executadas ao mesmo tempo para economizar tempo, qual componente da LCEL você usaria?  
   a) RunnableLambda  
   b) RunnablePassthrough  
   c) RunnableParallel  
   d) SequentialChain  
5. Qual método você chamaria em uma chain LCEL para obter a resposta token a token, em vez de esperar a resposta completa?  
   a) .invoke()  
   b) .run()  
   c) .batch()  
   d) .stream()

*(Respostas: 1-b, 2-b, 3-b, 4-c, 5-d)*

## **Capítulo 5: Desenvolvimento de Agentes Autônomos e Multiagentes**



Seja bem-vindo a um dos territórios mais fascinantes e, admito, mais complexos do LangChain: os agentes. Se o conceito parecer um pouco abstrato ou intimidador no começo, não se preocupe. É um salto conceitual significativo. Pense nisso como aprender a andar de bicicleta depois de só ter usado patinetes. Nos capítulos anteriores, construímos "patinetes": fluxos de trabalho lineares e previsíveis. Agora, vamos dar equilíbrio e autonomia à nossa criação.

O equilíbrio, assim como na bicicleta, vem com a prática. Vamos começar com calma, entender cada peça, e logo você estará pedalando por conta própria, criando sistemas que pensam e agem. Confie no processo, e vamos passo a passo.

### **O que é um Agente? O LLM como Cérebro**

Até agora, usamos LLMs para executar tarefas bem definidas dentro de um pipeline (uma Chain). O fluxo era fixo. Um agente, por outro lado, vira esse jogo de cabeça para baixo. Em um sistema agêntico, o LLM não é apenas um executor de tarefas, ele é o **cérebro**, o **motor de raciocínio** que decide o que fazer a seguir.

A principal diferença entre uma Chain e um Agente é a **autonomia**. Um agente é um sistema que usa um LLM como seu "motor de raciocínio" para determinar a sequência de ações a serem tomadas.

* Uma **Chain** segue um caminho predeterminado. Ex: Prompt \-\> LLM \-\> Parse. O caminho não muda.  
* Um **Agente** usa o LLM para escolher um caminho dinamicamente a partir de um conjunto de opções disponíveis (as ferramentas). O caminho pode ser diferente a cada execução.

Essa capacidade de tomar decisões em tempo de execução é o que permite que agentes resolvam problemas complexos, interajam com o mundo exterior e executem tarefas que não podem ser roteirizadas de antemão.

Pense na cena icônica de Matrix (1999), onde Morpheus oferece a Neo a pílula azul ou a pílula vermelha. Neo (o usuário) está buscando a verdade. Morpheus (o Agente) é o sistema que, com base em seu "raciocínio" e acesso a "ferramentas" (como o conhecimento da Matrix e a capacidade de manipular programas), decide qual "ação" tomar para guiar Neo. As "ferramentas" são os programas que Morpheus pode usar, e a "Matrix" é o ambiente onde essas ações acontecem. A pílula vermelha, que revela a verdade e dá a Neo a autonomia para ver o mundo como ele realmente é, pode ser comparada à autonomia que damos aos nossos agentes. Eles não apenas seguem instruções, mas "enxergam" o ambiente e tomam decisões para alcançar um objetivo.

Os efeitos inovadores dessa autonomia são visíveis em modelos como o Google vO3, que demonstram capacidades de raciocínio e interação com o ambiente que eram impensáveis há poucos anos.

### **Engenharia de Contexto: A Evolução do Prompt**

Quando falamos de agentes, especialmente sistemas com múltiplos agentes que colaboram e compartilham informações, a simples "Engenharia de Prompts" evolui para algo mais sofisticado: a **Engenharia de Contexto**.

Não se trata mais apenas de criar a instrução perfeita para uma única tarefa. Trata-se de gerenciar e moldar dinamicamente o contexto completo que cada agente recebe. Esse contexto pode incluir:

* O objetivo geral da missão.  
* O histórico da conversa até o momento (memória de curto prazo).  
* Os resultados e observações das ferramentas que já foram executadas.  
* Informações relevantes recuperadas de uma base de conhecimento (memória de longo prazo, ou RAG).  
* Uma "memória compartilhada" ou um "quadro branco" onde outros agentes deixaram notas.

A engenharia de contexto é a arte de garantir que o agente certo receba a informação certa no momento certo, sem sobrecarregá-lo com dados irrelevantes. É um desafio de design crucial para a eficiência de sistemas multiagentes.

### **RAG (Retrieval-Augmented Generation): Ampliando o Conhecimento do LLM**

Até agora, nossos LLMs operam com o conhecimento que foi "treinado" neles. Mas e se precisarmos que eles respondam a perguntas sobre dados muito específicos, privados ou que mudam constantemente? É aqui que entra o **RAG (Retrieval-Augmented Generation)**, um padrão arquitetural que permite aos LLMs acessar e utilizar informações externas e atualizadas.

Pense no RAG como dar ao seu LLM a capacidade de "consultar livros" antes de responder. O processo segue um fluxo lógico de quatro etapas:

1.  **Consulta (Query):** O usuário faz uma pergunta ou fornece uma entrada ao sistema.
2.  **Recuperação (Retrieval):** Em vez de o LLM tentar responder apenas com seu conhecimento interno, o sistema primeiro "recupera" informações relevantes de uma base de dados externa (como documentos, artigos, bancos de dados, etc.). Essa recuperação é feita buscando por similaridade semântica entre a consulta do usuário e os documentos na base de conhecimento.
3.  **Aumento (Augmentation):** As informações recuperadas são então "aumentadas" (adicionadas) ao prompt original do usuário. Isso cria um prompt mais rico e contextualizado, que é então enviado ao LLM.
4.  **Geração (Generation):** O LLM recebe o prompt aumentado e gera uma resposta que não apenas utiliza seu conhecimento interno, mas também incorpora e se baseia nas informações recuperadas externamente.

O RAG é crucial para construir aplicações de IA que precisam ser factualmente precisas, atualizadas e capazes de operar sobre grandes volumes de dados específicos de um domínio. Ele minimiza as "alucinações" (respostas inventadas) dos LLMs e os torna muito mais úteis em cenários corporativos e de dados sensíveis.

### **Componentes de um Agente: Ferramentas e o Executor**

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

### **Exercício Prático: Agente de Pesquisa Simples**

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
search\_tool \= TavilySearchResults(  
    max\_results=2,  
    description="Uma ferramenta de busca para encontrar informações na internet sobre eventos atuais, pessoas, lugares ou empresas."  
)  
tools \= \[search\_tool\]

# 3\. Criar o Prompt do Agente  
# Este prompt é um template especial que guia o agente, permitindo que ele "pense" e registre suas ações.  
# Os placeholders {chat\_history} e {agent\_scratchpad} são cruciais e gerenciados automaticamente pelo AgentExecutor.  
# O {agent\_scratchpad} é onde o agente registra seu processo de raciocínio (Thought), as ferramentas que decide usar (Action)  
# e os resultados dessas ações (Observation), formando o ciclo ReAct que vimos anteriormente.  
prompt \= ChatPromptTemplate.from\_messages(\[  
    ("system", "Você é um assistente prestativo."),  
    ("placeholder", "{chat\_history}"),  
    ("human", "{input}"),  
    ("placeholder", "{agent\_scratchpad}"),  
\])

# 4\. Criar o Agente  
# Esta função conecta o LLM, as ferramentas e o prompt  
agent \= create\_tool\_calling\_agent(llm, tools, prompt)

# 5\. Criar o Executor do Agente  
# O executor é o loop que roda o agente até a resposta final  
agent\_executor \= AgentExecutor(agent=agent, tools=tools, verbose=True)

# \--- Execução \---
if \_\_name\_\_ \== "\_\_main\_\_":  
    print("Agente de Pesquisa pronto\! Faça sua pergunta.")  
      
    pergunta1 \= "Qual foi o filme vencedor do Oscar de Melhor Filme em 2024?"  
    print(f"\\n\> Pergunta: {pergunta1}")  
    response1 \= agent\_executor.invoke({"input": pergunta1})  
    print(f"\\n\< Resposta Final: {response1\['output'\]}")

    pergunta2 \= "Qual é a cor do céu?"  
    print(f"\\n\> Pergunta: {pergunta2}")  
    response2 \= agent\_executor.invoke({"input": pergunta2})  
    print(f"\\n\< Resposta Final: {response2\['output'\]}")

**Comando de Execução (Linux/macOS):**

```sh
# Dê permissão de execução ao script
```sh
chmod +x exercicios/capitulo_05/exercicio_1/run.sh

# Execute o exercício
./exercicios/capitulo_05/exercicio_1/run.sh
```
```

**Comando de Execução (Windows):**

```bat
REM Execute o exercício no Windows
exercicios\capitulo_05\exercicio_1\run.bat
```


Ao executar, observe a saída com verbose=True. Você verá o LLM raciocinando, decidindo chamar a ferramenta tavily\_search\_results\_json, os resultados que a ferramenta retorna e, finalmente, a formulação da resposta final. Para a segunda pergunta, você verá que o LLM decide que não precisa de uma ferramenta e responde diretamente. Isso é autonomia em ação\!







### **Sistemas Multiagentes e a Magia do LangGraph**

E se um problema for tão complexo que um único agente não é suficiente? Entramos no mundo dos **sistemas multiagentes**. A ideia é criar um "time" de agentes especializados, cada um com suas próprias ferramentas e responsabilidades, que colaboram para resolver um problema maior.

Por exemplo, imagine um agente de pesquisa, um agente escritor e um agente crítico trabalhando juntos para criar um relatório. O orquestrador (ou "roteador") passaria a tarefa inicial para o pesquisador, o resultado para o escritor, a versão escrita para o crítico, e o feedback de volta para o escritor, em um ciclo.

Gerenciar esses fluxos complexos, que podem ter ciclos e condicionais, é um desafio. É para isso que o **LangGraph** foi criado. Ele é uma biblioteca construída sobre o LangChain que permite definir fluxos de trabalho de agentes como um **grafo**. Cada nó no grafo pode ser um agente ou uma função, e as arestas definem como o estado (as informações) flui entre eles.

O LangGraph é o estado da arte para construir sistemas multiagentes robustos e é um tópico avançado que exploraremos em projetos futuros, mas é fundamental que você saiba que ele existe e qual problema ele resolve.





### **Pontos Chave**
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

## **Capítulo 9: Projeto Final Integrador: Assistente de Viagem Inteligente**

Neste capítulo final, vamos consolidar todo o conhecimento adquirido ao longo do livro, construindo um projeto prático e funcional: um Assistente de Viagem Inteligente. Este agente será capaz de interagir com o usuário para planejar viagens, pesquisar informações em tempo real e gerenciar um orçamento, demonstrando a sinergia entre LLMs, ferramentas e a LangChain Expression Language (LCEL).

### **Visão Geral do Projeto**

O Assistente de Viagem será um agente que utiliza:
*   Um LLM (Gemini 2.5 Flash) como seu cérebro de raciocínio.
*   Uma ferramenta de busca na internet (Tavily) para obter informações atualizadas sobre destinos, clima, atrações, etc.
*   Ferramentas customizadas para adicionar itens a um orçamento de viagem e consultar o total.
*   A arquitetura de agentes do LangChain (`create_tool_calling_agent` e `AgentExecutor`) para orquestrar as interações.

### **Exercício Prático: Assistente de Viagem Inteligente**

*   **Objetivo:** Desenvolver um agente completo que auxilia no planejamento de viagens, combinando pesquisa e gerenciamento de orçamento.
*   **Nome do Arquivo:** `exercicios/capitulo_09/exercicio_1/main.py`
*   **Dependências:** `langchain`, `langchain-google-genai`, `langchain-tavily`, `python-dotenv`
*   **Comando de Instalação:** `uv add langchain langchain-google-genai langchain-tavily python-dotenv`
*   **Configuração Adicional:** Você precisará de uma chave de API da Tavily. Você pode obter uma gratuitamente em [tavily.com](https://tavily.com/). Adicione-a ao seu arquivo `.env` como `TAVILY_API_KEY`.

```python
# capitulo_09/assistente_viagem.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearchResults
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool

# Carregar variáveis de ambiente
load_dotenv()

# --- Ferramentas ---

# Ferramenta de busca na internet
search_tool = TavilySearchResults(
    max_results=3,
    description="Uma ferramenta de busca para encontrar informações na internet sobre destinos de viagem, clima, atrações, etc."
)

# Ferramenta customizada para gerenciar orçamento de viagem (simulado em memória)
class OrcamentoViagem:
    def __init__(self):
        self.orcamento = {}

    @tool
    def adicionar_item_orcamento(self, item: str, custo: float) -> str:
        """
        Adiciona um item e seu custo ao orçamento de viagem.
        Útil para planejar gastos.
        Exemplo: adicionar_item_orcamento("Passagem Aérea", 1500.00)
        """
        self.orcamento[item] = self.orcamento.get(item, 0.0) + custo
        return f"Item '{item}' com custo de R${costo:.2f} adicionado ao orçamento. Orçamento atual: {self.orcamento}"

    @tool
    def ver_orcamento_total(self) -> str:
        """
        Retorna o total do orçamento de viagem e a lista de itens.
        """
        total = sum(self.orcamento.values())
        if not self.orcamento:
            return "O orçamento de viagem está vazio."
        return f"Orçamento total: R${total:.2f}. Itens: {self.orcamento}"

orcamento_viagem = OrcamentoViagem()

tools = [search_tool, orcamento_viagem.adicionar_item_orcamento, orcamento_viagem.ver_orcamento_total]

# --- LLM ---
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# --- Prompt do Agente ---
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente de planejamento de viagens. Use as ferramentas disponíveis para ajudar o usuário a planejar sua viagem, pesquisar informações e gerenciar o orçamento. Seja prestativo e informativo."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# --- Agente e Executor ---
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- Execução ---
if __name__ == "__main__":
    print("Assistente de Viagem pronto! Como posso ajudar a planejar sua próxima aventura?")

    perguntas = [
        "Qual o clima em Paris em agosto?",
        "Quais são as principais atrações turísticas em Roma?",
        "Adicione 'Passagem Aérea' com custo de 2500.00 ao orçamento.",
        "Adicione 'Hospedagem' com custo de 1200.00 ao orçamento.",
        "Qual o meu orçamento total até agora?",
        "Preciso de ideias para uma viagem de aventura na América do Sul.",
        "Qual o custo de um jantar em um restaurante médio em Tóquio?",
        "Qual o meu orçamento total?",
    ]

    for pergunta in perguntas:
        print(f"\n> Pergunta: {pergunta}")
        response = agent_executor.invoke({"input": pergunta})
        print(f"\n< Resposta Final: {response['output']}")
```

**Comando de Execução:**

```sh
```sh
chmod +x capitulo_09/execucao_exercicio_9_1.sh
./capitulo_09/execucao_exercicio_9_1.sh
```
```

**Saída Esperada (pode variar ligeiramente):**

```text
Assistente de Viagem pronto! Como posso ajudar a planejar sua próxima aventura?

> Pergunta: Qual o clima em Paris em agosto?
... (saída verbose do agente) ...
< Resposta Final: Em agosto, o clima em Paris é geralmente quente e ensolarado, com temperaturas médias variando de 16°C a 25°C. É um dos meses mais quentes do ano, ideal para atividades ao ar livre.

> Pergunta: Quais são as principais atrações turísticas em Roma?
... (saída verbose do agente) ...
< Resposta Final: As principais atrações turísticas em Roma incluem o Coliseu, o Fórum Romano, o Panteão, a Fontana di Trevi, a Praça de São Pedro e os Museus do Vaticano, que abrigam a Capela Sistina.

> Pergunta: Adicione 'Passagem Aérea' com custo de 2500.00 ao orçamento.
... (saída verbose do agente) ...
< Resposta Final: Item 'Passagem Aérea' com custo de R$2500.00 adicionado ao orçamento. Orçamento atual: {'Passagem Aérea': 2500.0}

> Pergunta: Adicione 'Hospedagem' com custo de 1200.00 ao orçamento.
... (saída verbose do agente) ...
< Resposta Final: Item 'Hospedagem' com custo de R$1200.00 adicionado ao orçamento. Orçamento atual: {'Passagem Aérea': 2500.0, 'Hospedagem': 1200.0}

> Pergunta: Qual o meu orçamento total até agora?
... (saída verbose do agente) ...
< Resposta Final: Orçamento total: R$3700.00. Itens: {'Passagem Aérea': 2500.0, 'Hospedagem': 1200.0}

> Pergunta: Preciso de ideias para uma viagem de aventura na América do Sul.
... (saída verbose do agente) ...
< Resposta Final: Para uma viagem de aventura na América do Sul, você pode considerar destinos como a Patagônia (Argentina/Chile) para trekking e paisagens deslumbrantes, a Amazônia (Brasil/Peru/Equador) para ecoturismo e vida selvagem, ou a Bolívia para explorar o Salar de Uyuni e a cultura andina.

> Pergunta: Qual o custo de um jantar em um restaurante médio em Tóquio?
... (saída verbose do agente) ...
< Resposta Final: O custo de um jantar em um restaurante médio em Tóquio pode variar bastante, mas geralmente fica entre 2.000 a 5.000 ienes por pessoa, o que equivale a aproximadamente R$70 a R$175, dependendo da cotação atual.

> Pergunta: Qual o meu orçamento total?
... (saída verbose do agente) ...
< Resposta Final: Orçamento total: R$3700.00. Itens: {'Passagem Aérea': 2500.0, 'Hospedagem': 1200.0}
```

**Troubleshooting Comum:**

*   **`AuthenticationError` ou `TAVILY_API_KEY` não configurada:** Certifique-se de que você obteve sua `TAVILY_API_KEY` do Tavily e a adicionou corretamente ao seu arquivo `.env` na raiz do projeto.
*   **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Verifique se sua `GOOGLE_API_KEY` está corretamente configurada no arquivo `.env`.
*   **`ModuleNotFoundError`:** Verifique se todas as dependências (`langchain`, `langchain-google-genai`, `langchain-tavily`, `python-dotenv`) foram instaladas corretamente usando `uv add` ou `pip install`.
*   **Erros de Conexão:** Problemas de rede ou limites de taxa da API (Tavily ou Google Gemini) podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.
*   **Agente não usando a ferramenta:** Se o agente não estiver chamando as ferramentas quando esperado, revise as `description` das ferramentas. Elas devem ser claras e concisas, indicando exatamente o que a ferramenta faz e quando deve ser usada. O LLM usa essa descrição para decidir se a ferramenta é relevante para a tarefa.
*   **Saída Inesperada do Agente:** Se a resposta final do agente não for a esperada, ative `verbose=True` no `AgentExecutor` para inspecionar o processo de raciocínio do LLM e as chamadas de ferramentas. Isso ajudará a identificar onde o fluxo está se desviando.

### **Resumo do Capítulo**

Neste capítulo, você aplicou todos os conceitos aprendidos ao longo do livro para construir um Assistente de Viagem Inteligente. Este projeto final demonstrou como:

*   **Orquestrar Agentes:** Utilizar o LLM como um motor de raciocínio para tomar decisões dinâmicas.
*   **Integrar Múltiplas Ferramentas:** Capacitar o agente a interagir com o mundo externo através de ferramentas de busca e ferramentas customizadas para gerenciamento de dados.
*   **Aplicar LCEL:** Compor um pipeline complexo de forma elegante e eficiente.
*   **Gerenciar Segredos:** Manter as chaves de API seguras usando variáveis de ambiente.

Este projeto é um exemplo claro do poder do LangChain para construir aplicações de IA que resolvem problemas reais, combinando diferentes capacidades para criar soluções inteligentes e autônomas.

### **Pontos Chave**
*   Projetos integradores são a melhor forma de consolidar o aprendizado de múltiplos conceitos.
*   Agentes com ferramentas são poderosos para interagir com o mundo real e dados externos.
*   A LCEL facilita a construção de pipelines complexos e legíveis.
*   A segurança no gerenciamento de chaves de API é fundamental em qualquer aplicação.

### **Teste seu Conhecimento**

1. Qual o principal benefício de usar múltiplas ferramentas em um agente, como demonstrado no Assistente de Viagem?
   a) Reduz o custo das chamadas de API.
   b) Permite que o agente execute tarefas mais complexas e diversificadas.
   c) Aumenta a velocidade de resposta do LLM.
   d) Elimina a necessidade de um LLM.
2. No projeto do Assistente de Viagem, qual ferramenta seria usada para descobrir "Qual o clima em Paris em agosto?"
   a) `adicionar_item_orcamento`
   b) `ver_orcamento_total`
   c) `search_tool`
   d) Nenhuma das anteriores.
3. Por que é importante usar `load_dotenv()` e um arquivo `.env` para as chaves de API?
   a) Para tornar o código mais curto.
   b) Para melhorar a performance do agente.
   c) Para evitar que as chaves de API sejam expostas no código-fonte e versionadas.
   d) Para que o agente possa se conectar à internet.
4. Se o Assistente de Viagem não estivesse usando a ferramenta `adicionar_item_orcamento` quando solicitado, qual seria a primeira coisa a verificar?
   a) A versão do Python.
   b) A descrição da ferramenta `adicionar_item_orcamento`.
   c) A conexão com a internet.
   d) O modelo do LLM.
5. Qual o conceito central do LangChain que permite ao agente decidir dinamicamente qual ferramenta usar?
   a) Prompt Templates.
   b) Output Parsers.
   c) O loop de raciocínio (ReAct) do agente.
   d) Streaming de respostas.

*(Respostas: 1-b, 2-c, 3-c, 4-b, 5-c)*

## **Referências Bibliográficas e Próximos Passos**

### **Documentação Oficial e Ferramentas**
*   **Documentação Oficial do LangChain:** A fonte mais completa e atualizada para todos os componentes e funcionalidades do LangChain. Essencial para aprofundamento e consulta: [https://python.langchain.com/](https://python.langchain.com/)
*   **Documentação do Google AI Studio:** Para explorar os modelos Gemini e obter chaves de API: [https://aistudio.google.com/](https://aistudio.google.com/)
*   **Documentação da Tavily API:** Para detalhes sobre a ferramenta de busca utilizada nos exemplos: [https://tavily.com/](https://tavily.com/)

### **Livros Recomendados**
*   **"Generative AI with LangChain" de Ben Stokes:** Um excelente recurso para aprofundar seus conhecimentos em LangChain.
*   **"Building LLM Powered Applications" de Josh Star:** Outro recurso valioso para construir aplicações com LLMs.

### **Artigos e Pesquisas Fundamentais**
*   **"Attention Is All You Need" (Vaswani et al., 2017):** O artigo seminal que introduziu a arquitetura Transformer, base de muitos LLMs modernos.
*   **"Language Models are Few-Shot Learners" (Brown et al., 2020):** Apresenta o conceito de few-shot learning e o impacto dos modelos de grande escala.
*   **"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (Wei et al., 2022):** Explora como o Chain-of-Thought melhora a capacidade de raciocínio dos LLMs.
*   **"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (Lewis et al., 2020):** O artigo original que introduziu o padrão RAG.
*   **"ReAct: Synergizing Reasoning and Acting in Language Models" (Yao et al., 2022):** O artigo original que introduziu o padrão ReAct, fundamental para entender o raciocínio dos agentes: [https://react-lm.github.io/](https://react-lm.github.io/)

*   **Créditos de Tutoriais e Recursos:** Reconhecimento a todos os tutoriais, artigos de blog, vídeos e cursos online que serviram de inspiração e fonte de aprendizado para a criação deste conteúdo. A comunidade de IA é vasta e generosa, e este livro é um reflexo do conhecimento compartilhado por muitos.

### **Próximos Passos na sua Jornada**

Parabéns! Você chegou ao final deste livro e, mais importante, deu um passo gigantesco na sua jornada com a Inteligência Artificial e o LangChain. Mas lembre-se, o aprendizado é contínuo. Aqui estão algumas sugestões para seus próximos passos:

1.  **Explore o LangGraph:** Para sistemas multiagentes ainda mais complexos e com estados, o LangGraph é o próximo nível.
2.  **Aprofunde-se em RAG:** Experimente diferentes tipos de `Vector Stores`, `Embeddings` e estratégias de recuperação.
3.  **Construa seus Próprios Projetos:** A melhor forma de aprender é fazendo. Pense em problemas reais que você enfrenta e tente resolvê-los com agentes de IA.
4.  **Contribua para a Comunidade:** Compartilhe seu conhecimento, ajude outros desenvolvedores e contribua para projetos de código aberto.
5.  **Mantenha-se Atualizado:** O campo da IA avança rapidamente. Siga blogs, participe de conferências e continue experimentando.

## **Glossário**

*   **Agente (Agent):** Um sistema que usa um LLM como seu "cérebro" para decidir a sequência de ações a serem tomadas, utilizando um conjunto de ferramentas.
*   **Chain:** Uma sequência predefinida de operações ou chamadas a modelos de linguagem para formar um pipeline inteligente.
*   **Engenharia de Contexto:** A disciplina de gerenciar e moldar dinamicamente o contexto completo que um agente recebe para otimizar seu raciocínio e ações.
*   **Engenharia de Prompts:** A disciplina de projetar e otimizar as instruções dadas aos modelos de linguagem para obter os resultados desejados.
*   **Executor do Agente (Agent Executor):** O runtime que orquestra o loop de raciocínio (ReAct) de um agente, invocando ferramentas e processando observações.
*   **LangChain Expression Language (LCEL):** Uma linguagem declarativa para compor Runnables no LangChain, permitindo a criação de pipelines flexíveis e eficientes.
*   **LLM (Large Language Model):** Um modelo de linguagem de grande escala, como Gemini, GPT-4, Claude, capaz de entender e gerar texto.
*   **Prompt:** A instrução ou entrada de texto fornecida a um LLM para gerar uma resposta.
*   **RAG (Retrieval-Augmented Generation):** Um padrão arquitetural que permite aos LLMs acessar e utilizar informações externas e atualizadas antes de gerar uma resposta.
*   **ReAct (Thought + Action + Observation):** Um padrão de raciocínio para agentes onde o LLM pensa (Thought), executa uma ação (Action) e observa o resultado (Observation) em um ciclo iterativo.
*   **Runnable:** Uma interface padronizada no LangChain que permite que componentes sejam encadeados usando o operador pipe (|).
*   **Tool (Ferramenta):** Uma ação que um agente pode executar, geralmente uma função Python com uma descrição clara, que permite ao agente interagir com o mundo externo.
*   **uv:** Um gerenciador de pacotes e ambientes virtuais escrito em Rust, conhecido por sua alta performance e compatibilidade com `pyproject.toml`.
*   **WSL (Windows Subsystem for Linux):** Uma camada de compatibilidade que permite aos usuários executar um ambiente Linux diretamente no Windows.

## **Apêndice: Checklists Consolidados**

### **Checklist de Configuração do Ambiente**

*   [ ] Instalar WSL (Windows Subsystem for Linux) e uma distribuição Linux (ex: Kali Linux, Ubuntu).
*   [ ] Instalar `pyenv` para gerenciar versões do Python.
*   [ ] Instalar a versão do Python desejada com `pyenv` (ex: `pyenv install 3.12.9`).
*   [ ] Configurar `pyenv` no seu shell (`.zshrc` ou `.bashrc`).
*   [ ] Instalar `zsh` e `Oh My Zsh` (opcional, mas recomendado para produtividade).
*   [ ] Instalar plugins úteis para `zsh` (ex: `zsh-syntax-highlighting`, `zsh-autosuggestions`).
*   [ ] Gerar e configurar chaves SSH para o GitHub (ou outro serviço Git).
*   [ ] Instalar `uv` como gerenciador de pacotes e ambientes virtuais.
*   [ ] Criar um arquivo `.env` na raiz do projeto para variáveis de ambiente.
*   [ ] Adicionar `GOOGLE_API_KEY` (e outras chaves, como `TAVILY_API_KEY`) ao `.env`.
*   [ ] Adicionar `.env` e `.venv/` ao `.gitignore`.

### **Checklist de Construção de Pipelines**

*   [ ] Definir claramente o objetivo do pipeline e as etapas necessárias para alcançá-lo.
*   [ ] Usar a sintaxe LCEL (`|`) para compor `Runnables` (prompts, modelos, parsers, funções).
*   [ ] Garantir a passagem correta de dados entre as etapas, usando dicionários e `RunnablePassthrough` quando necessário.
*   [ ] Utilizar `RunnableParallel` para otimizar a latência executando tarefas independentes ao mesmo tempo.
*   [ ] Integrar lógica customizada usando `RunnableLambda` quando necessário.
*   [ ] Implementar streaming (`.stream()`) para melhorar a experiência do usuário em aplicações interativas.
*   [ ] Incluir monitoramento e logging (idealmente com LangSmith) para acompanhar a execução e identificar falhas.
*   [ ] Testar o pipeline com diferentes entradas para validar a robustez e a eficiência.
*   [ ] Documentar o fluxo e as dependências para facilitar a manutenção futura.

## **Sobre o Autor**

A jornada de Igor Medeiros é movida por um propósito forjado no amor, na dor e na superação. Filho de um herói que, em suas palavras, “samba todo dia na cara do Alzheimer”, e pai da Melissa, “a luz de sua jornada”, ele carrega em sua história a força desses dois pilares. Sua trajetória profissional de mais de duas décadas foi profundamente ressignificada após um grave desafio de saúde em 2012, que incluiu um tumor gigante na cabeça e uma embolia pulmonar no pós-operatório. **A batalha pela vida deixou marcas permanentes: a paralisia facial e a surdez unilateral total, ambas do lado direito do rosto.**

A experiência de quase morte e a reabilitação que se seguiu não foram uma pausa, mas o ponto de ignição para uma nova missão. Nesse período, sua jornada incluiu um corajoso pivô de carreira, no qual atuou como executivo de marketing e vendas. Essa imersão no lado do negócio ensinou-lhe lições valiosas sobre a importância da qualidade da entrega final e a perspectiva do cliente, visão que hoje integra a todos os seus projetos tecnológicos: usar a tecnologia para honrar a vida e gerar um impacto que realmente importe.

Como Engenheiro de Software Sênior e especialista em Java para smart cards, sua carreira o levou a palestrar por todo o Brasil e até no Japão. Ao longo de mais de 20 anos, liderou a criação de soluções robustas para diversos setores da indústria. Essa base sólida, que vai desde a homologação de sistemas criptográficos para a Casa Civil até a liderança técnica em projetos de inovação, construiu o alicerce para sua atuação atual.

Hoje, como especialista de IA Agents e evangelista de Inteligência Artificial, Igor está na vanguarda da tecnologia, liderando questões técnicas de projetos e definindo padrões para gigantes atuais dos setores financeiro e de telecomunicações, como Santander, Bradesco, Pernambucanas, TIM e o grupo Telefônica. É nesse cenário de ponta que ele desenvolve e coloca em produção sistemas complexos com agentes de IA. Ele direciona essa expertise para sua grande paixão: o setor da saúde, buscando ativamente criar soluções em neurologia que possam, um dia, reescrever histórias como a sua e de seu pai.

Além de seu trabalho corporativo, Igor é um líder de comunidade nato, que acredita que o conhecimento só tem valor quando é compartilhado. Essa vocação para o humanismo tem raízes profundas: por 14 anos, dedicou-se como voluntário em uma ONG com a missão de resgatar pessoas em situação de rua. Em um marcante contraste com seu trabalho de ponta em Inteligência Artificial, essa experiência solidificou sua crença de que a tecnologia mais avançada deve sempre servir à empatia e à conexão humana. Seja em palestras, artigos ou como mentor, ele se dedica a capacitar outros desenvolvedores, fechando o ciclo de uma jornada extraordinária que transforma gratidão em legado. Este livro é mais um passo nesse caminho.

## **Comunidade e Contato**

A jornada do aprendizado não termina aqui. Na verdade, ela está apenas começando.

* Código Fonte: Todo o código deste livro está disponível para você clonar, modificar e experimentar. Acesse o repositório em:  
  https://github.com/igormedeiros/livros/blob/main/langchain-na-pratica/  
* Comunidade no Telegram: Junte-se a outros desenvolvedores, tire dúvidas, compartilhe seus projetos e continue a conversa em nossa comunidade:  
  https://t.me/igormedeiros\_comunidade  
* Feedback e Contato: Sua opinião é incrivelmente valiosa. Se você gostou deste livro, por favor, considere deixar uma avaliação na Amazon. Isso ajuda outros leitores como você a encontrar este material e me dá o feedback necessário para continuar melhorando. Para outras dúvidas, sugestões ou para saber mais sobre meu trabalho, visite meu site:  
  https://igormedeiros.com.br

Obrigado por me acompanhar nesta jornada. Agora, vá e construa algo incrível!

