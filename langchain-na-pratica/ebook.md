# **LangChain na Prática: O primeiro passo com Agentes de IA**

**Igor Medeiros**

## **Informações de Copyright**

© 2025 Igor Medeiros. Todos os direitos reservados.

Este livro faz parte da série "IA na Prática".
Lançamento: 19 de Julho de 2025.

Nenhuma parte desta publicação pode ser reproduzida, distribuída ou transmitida por qualquer forma ou meio, incluindo fotocópia, gravação ou outros métodos eletrônicos ou mecânicos, sem a permissão prévia por escrito do autor, exceto no caso de breves citações incorporadas em resenhas críticas e outros usos não comerciais permitidos pela lei de direitos autorais.

ISBN: [A SER DEFINIDO]

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

À **Giselle Arruda**, por segurar minha mão em momentos difíceis, quando precisei de ajuda para me reerguer profissionalmente. Você foi a pessoa que me aparou e me guiou com uma força e uma empatia que jamais esquecerei.

Ao **Fernando Lopes Jr.**, por ser um amigo e um incentivador, sempre me apoiando nos momentos mais difíceis.

Ao **Eduardo Bregaida**, que confiou em mim e me apresentou uma possibilidade de recomeço quando eu mais precisei, enquanto enfrentava uma terrível fase de problemas de saúde mental e buscava um caminho de volta ao mercado de TI. Sua confiança foi um ponto de virada.

À **Marina**, **Adriana** e **Julio**, por confiarem sempre em mim para voltar ao cenário das palestras técnicas pelo Brasil e outros países, ainda que de forma online, no contexto interno corporativo. Sua crença no meu potencial foi fundamental para essa retomada.

À **Cristiane Tokarski**, por ter surgido como um anjo que agiu corrigindo o curso que a vida havia me conduzido, onde eu não me sentia "encaixado" na trilha do meu proposito profissional. Sua orientação foi um farol que me ajudou a reencontrar meu caminho e propósito.

Ao **Marcello Manzan**, um irmão de alma que a faculdade me deu e que hoje é como se fosse da minha família. Sua busca incansável pela excelência profissional é uma inspiração diária, um farol que me guia. Mais do que isso, sou grato pela sua amizade inabalável e pelas risadas que, ao longo dos anos, transformaram desafios em memórias preciosas.

À vasta e vibrante comunidade open source do LangChain e de todas as bibliotecas e ferramentas que tornaram este livro possível. Seu trabalho incansável e colaboração são a verdadeira força motriz por trás da inovação em IA. Reconhecemos e agradecemos a todos os projetos de código aberto e seus contribuidores, cujas licenças e termos de uso foram respeitados na criação deste material.

A cada um de vocês, meu mais profundo e sincero obrigado.

## **Sumário**

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
  * Pontos Chave  
  * Resumo do Capítulo  
* **Capítulo 2: Configurando o Ambiente de Desenvolvimento Python para LangChain**  
  * Meu Ambiente de Batalha: Por que Linux e Ferramentas de Linha de Comando  
  * Gerenciando Versões do Python como um Profissional: pyenv  
  * Um Terminal com Superpoderes: zsh e Oh My Zsh  
  * Segurança e Conveniência com Git: Chaves SSH  
  * Minhas Ferramentas de Batalha: VS Code  
  * Gerenciando Dependências: A Revolução do uv e pyproject.toml  
  * Gerenciando Segredos: Chaves de API e Variáveis de Ambiente  
  * Considerações sobre Hardware  
  * Troubleshooting Comum  
  * Pontos Chave  
  * Resumo do Capítulo  
  * Teste seu Conhecimento  
* **Capítulo 3: Manipulação de Prompts e Modelos de Linguagem com LangChain**  
  * A Arte e a Ciência da Engenharia de Prompts  
  * Templates de Prompt: Reutilização e Dinamismo  
  * Integrando Modelos de Linguagem (LLMs)  
  * Exercício Prático: Um Tradutor Multilíngue Dinâmico  
  * Resumo do Capítulo  
  * Pontos Chave  
  * Teste seu Conhecimento  
* **Capítulo 4: Construção de Pipelines: Da SequentialChain à LCEL**  
  * A Evolução das Chains: Do Imperativo ao Declarativo  
  * O Jeito Clássico: LLMChain e SequentialChain (OBSOLETO)  
  * A Revolução da LCEL: Por que Devemos Usá-la?  
  * LCEL na Prática: Exercícios Essenciais  
  * Checklist de Construção de Pipelines  
  * Pontos Chave  
  * Teste seu Conhecimento  
* **Capítulo 5: Desenvolvimento de Agentes Autônomos e Multiagentes**  
  * O que é um Agente? O LLM como Cérebro  
  * Engenharia de Contexto: A Evolução do Prompt  
  * RAG (Retrieval-Augmented Generation): Ampliando o Conhecimento do LLM  
  * Componentes de um Agente: Ferramentas e o Executor  
  * Exercício Prático: Agente de Pesquisa Simples  
  * Sistemas Multiagentes e a Magia do LangGraph  
  * Pontos Chave  
  * Resumo do Capítulo  
  * Teste seu Conhecimento  
* **Capítulo 6: Ferramentas e Agentes: Capacitando LLMs com Ações**  
  * O que são Ferramentas (Tools)?  
  * Agentes (Agents): O Cérebro por Trás das Ações  
  * Exercício 1: Agente de Análise de Vendas com Ferramenta SQL  
  * Resumo do Capítulo  
  * Pontos Chave  
  * Teste seu Conhecimento  
* **Capítulo 7: Técnicas Avançadas: Memória, Feedback e Aprendizado Contínuo**
* **Capítulo 8: Testes, Debugging e Otimização de Aplicações LangChain**
* **Capítulo 9: LangChain na Produção: Escalabilidade, Observabilidade e Segurança**  
  * Pontos Chave  
  * Resumo do Capítulo  
  * Teste seu Conhecimento    
  * Pontos Chave  
  * Resumo do Capítulo  
  * Teste seu Conhecimento  
* Próximos passos
* Mensagem final
* Sobre o autor
* Referências
* Apêndice: Glossário de Termos


















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

