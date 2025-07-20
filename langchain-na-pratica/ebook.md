# **LangChain na Prática: O primeiro passo com Agentes de IA**

**Igor Medeiros**

## **Informações de Copyright**

© 2025 Igor Medeiros. Todos os direitos reservados.

Este livro faz parte da série "IA na Prática".
Lançamento: 20 de Julho de 2025.

Nenhuma parte desta publicação pode ser reproduzida, distribuída ou transmitida por qualquer forma ou meio, incluindo fotocópia, gravação ou outros métodos eletrônicos ou mecânicos, sem a permissão prévia por escrito do autor, exceto no caso de breves citações incorporadas em resenhas críticas e outros usos não comerciais permitidos pela lei de direitos autorais.

Contato: igor@igormedeiros.com.br  
Website: https://igormedeiros.com.br

## **Aviso Legal**

Este livro e seu conteúdo são fornecidos "como estão", sem garantias de qualquer tipo, expressas ou implícitas. O autor e o editor não se responsabilizam por quaisquer erros ou omissões, ou por quaisquer danos resultantes do uso das informações contidas neste livro. Os exemplos de código são fornecidos para fins educacionais e podem exigir modificação para uso em produção. A execução dos códigos e a utilização das chaves de API são de inteira responsabilidade do leitor.

## **Prefácio**

[Este prefácio será escrito por Felipe Gagliazzo.]

## **Dedicatória**

Aos meus pais, José Maurício e Genilda, a quem busco honrar todos os dias sendo um ser humano melhor.

À minha filha Melissa, a luz que ilumina minha jornada e me inspira todos os dias a ser melhor.

Ao Dr. Paulo H Pires de Aguiar, o médico e amigo que, com maestria e humanidade, orquestrou o salvamento da minha vida.



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
  * Exercício Prático: Hello, LangChain!  
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

### **Como Aproveitar ao Máximo Este Livro**

Este livro foi desenhado para ser mais do que uma leitura passiva; é um convite à ação. Para extrair o máximo valor desta jornada, sugiro as seguintes abordagens:

1.  **Mão na Massa:** A teoria é importante, mas a prática é onde o aprendizado se solidifica. Execute todos os exemplos de código. Altere-os, quebre-os e conserte-os. A experimentação é a chave para a maestria.
2.  **Não Pule Capítulos:** Os conceitos são construídos de forma progressiva. Cada capítulo se baseia no anterior. Se algo parecer complexo, revise os capítulos anteriores antes de seguir em frente.
3.  **Use o Gêmeo Digital:** Lembre-se do assistente de IA que mencionei na introdução? Ele é seu companheiro de estudo. Use-o para tirar dúvidas, explorar conceitos e até mesmo para debater ideias. Ele foi treinado com o conteúdo deste livro e pode oferecer insights adicionais.
4.  **Participe da Comunidade:** O aprendizado é uma via de mão dupla. Compartilhe suas descobertas, faça perguntas e ajude outros. A comunidade LangChain é vibrante e acolhedora. Juntos, somos mais fortes.
5.  **Adapte e Inove:** Os exemplos fornecidos são pontos de partida. Pense em como você pode adaptar as técnicas e os conceitos para seus próprios projetos e desafios. A inovação começa com a adaptação criativa.

Estou animado para ver o que você vai construir. Vamos começar?

Cada novo conhecimento que você adquirir neste livro não é apenas um conceito teórico; é uma nova ferramenta na sua caixa. Pense em um problema que te incomoda. Um processo manual e repetitivo no seu trabalho? A dificuldade de encontrar informações em uma base de dados interna gigante? A vontade de criar um assistente pessoal que realmente te entenda?

Eu, por exemplo, aprendi sobre visão computacional e frameworks como o YOLO não por um interesse puramente acadêmico, mas porque queria resolver um problema que me toca profundamente. Vendo a luta diária do meu pai com o Alzheimer, comecei a desenvolver um projeto para usar câmeras de segurança internas para monitorar idosos com demência, alertando familiares ou cuidadores sobre quedas ou situações de risco diretamente em seus celulares. O problema real me deu a motivação e o contexto para aprender a ferramenta.

Mantenha essa abordagem em mente enquanto avança pelos capítulos. Tente conectar cada conceito — Chains, Agents, RAG — a uma possível solução para um problema que importa para você. Essa abordagem transforma o aprendizado passivo em uma busca ativa por soluções, tornando a jornada muito mais significativa e eficaz.

No fundo, a programação e a filosofia compartilham um terreno comum: ambas buscam entender e moldar a realidade através da lógica e da abstração. Assim como um filósofo constrói argumentos para desvendar verdades, um programador constrói algoritmos para resolver problemas. A IA, nesse sentido, é a materialização de um pensamento filosófico antigo: a busca por inteligência e autonomia. Ao programar com IA, estamos não apenas escrevendo código, mas participando de um diálogo contínuo com a natureza da inteligência e da criação.


## Capítulo 1: Introdução ao LangChain — Fundamentos e Conceitos Essenciais

**Neste capítulo, você vai aprender:**

* O que é LangChain e como ele surgiu para resolver problemas reais na era da IA.
* Os conceitos fundamentais de Chains, Prompts, Models e Agents.
* Como o LangChain se posiciona no ecossistema de IA, comparado a outros frameworks.
* Seu primeiro código prático com LangChain, usando a sintaxe moderna da LCEL.

Este capítulo serve como a porta de entrada para o universo LangChain. Abordaremos a história e a motivação por trás do framework, seus componentes essenciais e como ele se encaixa no cenário atual da inteligência artificial. Ao final, você terá uma compreensão sólida dos pilares do LangChain e estará pronto para construir suas primeiras aplicações.

### O que é LangChain? Uma Breve História em Meio à Tempestade da IA

Antes de mergulharmos, quero que saiba: é normal se sentir um pouco sobrecarregado no início. O mundo da IA avança a passos largos, e o LangChain, como uma ferramenta poderosa, pode parecer complexo. Mas lembre-se, cada grande jornada começa com um primeiro passo. E você já deu o seu ao abrir este livro. Vamos desmistificar cada conceito, juntos. Respire fundo, e vamos nessa!

Para entender o LangChain, vamos simplificar. Imagine que você tem um supercomputador que sabe conversar, escrever e até criar coisas, mas ele está isolado. Ele não consegue acessar a internet, nem seus documentos, nem interagir com outros programas. O LangChain é como a "ponte" que conecta esse supercomputador (o Modelo de Linguagem, ou LLM) ao mundo real.

Ele surgiu no final de 2022, um pouco antes do ChatGPT "explodir" e mostrar a todos o poder dos LLMs. Naquela época, um engenheiro chamado Harrison Chase percebeu que, para construir aplicações realmente úteis com esses modelos, precisávamos de uma forma fácil de:

* **Conectá-los a informações externas:** Como fazer o LLM "ler" seus e-mails ou documentos?
* **Permitir que eles usem ferramentas:** Como fazer o LLM "clicar" em um botão ou "enviar" uma mensagem?
* **Organizar tarefas complexas:** Como fazer o LLM seguir uma série de passos para resolver um problema grande?

O LangChain foi a resposta para essas perguntas. Ele se tornou incrivelmente popular porque oferecia uma maneira de "orquestrar" os LLMs, transformando-os de meros geradores de texto em "cérebros" capazes de interagir com o mundo. Em pouco tempo, o projeto de código aberto cresceu tanto que se tornou uma empresa, a LangChain AI, atraindo grandes investimentos.

Em resumo, o LangChain é a ferramenta que nos permite construir aplicações de IA que vão muito além de uma simples conversa, conectando os LLMs a dados e ferramentas para resolver problemas do dia a dia.

### O Problema da Conversa Iterativa e o Nascimento das "Chains"

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

### Exercício Prático: Hello, LangChain!

Vamos colocar a mão na massa com o nosso primeiro código. Este será o "Hello, World!" do LangChain. Ele vai demonstrar, da forma mais simples possível, o conceito de chain que acabamos de discutir. Para este e os demais exemplos do livro, usaremos os modelos Gemini do Google, especificamente o gemini-1.5-flash, que é incrivelmente rápido e oferece uma camada gratuita generosa para desenvolvedores.

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


**Comando de Execução (Linux/macOS):**

```sh
# Dê permissão de execução ao script
chmod +x exercicios/capitulo_01/exercicio_1/run.sh

# Execute o exercício
./exercicios/capitulo_01/exercicio_1/run.sh
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

Parabéns! Você acabou de executar sua primeira Chain. Observe a linha chain \= prompt_template | model | output_parser. Essa sintaxe elegante, chamada **LangChain Expression Language (LCEL)**, é a representação visual do encadeamento que discutimos. É a base sobre a qual construiremos aplicações muito mais poderosas.

**Troubleshooting Comum:**

* **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Certifique-se de que você obteve sua `GOOGLE_API_KEY` do Google AI Studio e a adicionou corretamente ao seu arquivo `.env` na raiz do projeto. Lembre-se de que o arquivo `.env` não deve ser versionado no Git.
* **`ModuleNotFoundError`:** Verifique se todas as dependências (`langchain`, `langchain-google-genai`, `python-dotenv`) foram instaladas corretamente usando `uv add` ou `pip install`.
* **Erros de Conexão:** Problemas de rede ou limites de taxa da API podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.

### A Arquitetura Central: Os Componentes Essenciais

Agora que você já viu uma chain em ação, vamos formalizar os blocos de construção fundamentais. Pense neles como peças de Lego que podemos combinar de infinitas maneiras.

**1. Models (LLMs e Chat Models)**

O coração de qualquer aplicação LangChain é um modelo de linguagem. O LangChain fornece uma interface padronizada para interagir com dezenas de modelos diferentes, desde os da OpenAI (GPT-3.5, GPT-4), Google (Gemini), Anthropic (Claude), até modelos de código aberto disponíveis no Hugging Face. Isso significa que você pode trocar o modelo subjacente da sua aplicação com pouquíssimas alterações no código, o que é fantástico para experimentação e otimização de custos.

Existem dois tipos principais de modelos no LangChain:

* **LLMs:** Modelos que recebem uma string como entrada e retornam uma string como saída.
* **Chat Models:** Modelos que recebem uma lista de mensagens ("system", "human", "ai") e retornam uma mensagem. A maioria das aplicações modernas utiliza Chat Models.

**2. Prompts**

Um prompt é a instrução que damos ao modelo de IA. O LangChain facilita a criação de prompts dinâmicos e reutilizáveis com **Prompt Templates**.

**3. Chains**

Uma Chain é uma sequência declarativa de componentes (Runnables) conectados via LCEL (`|`), formando pipelines que processam dados de entrada até a saída final. Use LCEL para compor fluxos simples e eficientes.

**4. Agents (Agentes)**

Agentes são componentes que usam LLMs para decidir dinamicamente quais ações tomar, escolhendo ferramentas e caminhos conforme o contexto e objetivo. Use Agents para tarefas que exigem flexibilidade e tomada de decisão autônoma.

### O Ecossistema LangChain: Mais que uma Biblioteca

O LangChain evoluiu para um ecossistema completo:

* **langchain-core:** Abstrações e interfaces base (Runnable, BaseMessage, etc.).
* **langchain-community:** Integrações mantidas pela comunidade.
* **langchain:** Pacote principal com chains, agents e estratégias de recuperação.
* **LangGraph:** Framework para orquestração de agentes e workflows baseados em grafos, ideal para fluxos complexos e multiagentes.
* **LangSmith:** Plataforma de observabilidade, depuração e avaliação para aplicações LangChain.

### Tabela 1: LangChain vs. Frameworks Concorrentes

Para situar o LangChain no cenário atual, é útil compará-lo com outras ferramentas populares.

| Framework | Foco Principal | Pontos Fortes | Caso de Uso Típico |
| :---- | :---- | :---- | :---- |
| **LangChain** | Orquestração de LLMs e Agentes | Flexibilidade, ecossistema de agentes, vastas integrações, LangGraph | Chatbots complexos, agentes autônomos, assistentes de código |
| **LlamaIndex** | Indexação e Preparação de Dados para RAG | Otimização de dados para RAG, conectores de dados, índices hierárquicos | Aplicações RAG sobre grandes volumes de documentos |
| **CrewAI** | Orquestração de Agentes Colaborativos | Foco em colaboração entre agentes, definição de papéis e tarefas, processos sequenciais | Equipes de agentes autônomos para pesquisa, escrita e análise |
| **Microsoft Autogen** | Framework de Multiagentes Conversacionais | Agentes conversáveis, flexibilidade na definição de padrões de interação | Simulações complexas, resolução de problemas em grupo, jogos |
| **Pydantic AI** | Geração de Saídas Estruturadas (JSON) | Integração com Pydantic, garantia de conformidade com schemas JSON | Extração de dados, saídas de API, integração com sistemas legados |
| **Praison AI** | Orquestração de Multi-Agentes LLM (Low-Code) | Facilidade de uso, customização, integração com outros frameworks, suporte a múltiplos LLMs | Automação de processos, chatbots, pesquisa multi-agente, análise de dados |


É importante notar que, embora o LangChain seja uma ferramenta poderosa e flexível, a escolha do framework ideal depende muito do caso de uso específico. LlamaIndex, por exemplo, brilha em cenários de RAG complexos, enquanto CrewAI e Microsoft Autogen oferecem abordagens mais especializadas para orquestração multiagente. Pydantic AI foca na garantia de saídas estruturadas, crucial para integração com sistemas legados. Praison AI, por sua vez, se destaca pela facilidade de uso e orquestração de multi-agentes com foco em low-code.

O LangChain se posiciona como uma ferramenta modular de propósito geral, permitindo a construção de uma vasta gama de aplicações de IA. A escolha entre esses frameworks envolve um trade-off entre flexibilidade, facilidade de uso e especialização. Enquanto frameworks como CrewAI e AutoGen oferecem soluções mais prontas para orquestração multiagente e colaboração, o LangChain fornece os blocos de construção fundamentais para criar soluções altamente customizadas e complexas, sendo a base para muitos desses outros frameworks. Compreender esses trade-offs é fundamental para escolher a ferramenta certa para o trabalho.



### Pontos Chave

* LangChain simplifica a orquestração de LLMs, permitindo a construção de aplicações complexas.
* O conceito de "Chain" automatiza sequências de chamadas a LLMs, tornando o desenvolvimento mais estruturado.
* Os componentes fundamentais (Models, Prompts, Chains, Agents) são blocos de construção modulares.
* A LCEL (LangChain Expression Language) é a forma moderna e eficiente de construir pipelines no LangChain.

### Resumo do Capítulo

Este capítulo serve como a porta de entrada para o universo LangChain. Abordamos a história, motivação, componentes essenciais e posicionamento do framework. Você está pronto para construir suas primeiras aplicações com LangChain.

### Teste seu Conhecimento

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


4. No exercício "Hello, LangChain!", qual operador foi usado para conectar o prompt, o modelo e o parser?
   a) + (adição)
   b) -> (seta)
   c) | (pipe)
   d) & (e comercial)


5. Qual a principal diferença entre uma Chain e um Agent?
   a) Agents são mais rápidos que Chains.
   b) Chains usam múltiplos modelos, enquanto Agents usam apenas um.
   c) Chains seguem um fluxo predefinido, enquanto Agents usam um LLM para decidir dinamicamente qual ação tomar.
   d) Agents só podem ser usados para chatbots, enquanto Chains são de uso geral.


**Respostas:**
1. c
2. b
3. d
4. c
5. c

### Projeto Hands-on: Construindo um Chatbot Simples

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

**Comando de Execução (Windows):**

```bat
REM Execute o exercício no Windows
exercicios\capitulo_01\exercicio_2\run.bat
```


**Troubleshooting Comum:**

* **`AuthenticationError` ou `GOOGLE_API_KEY` não configurada:** Certifique-se de que você obteve sua `GOOGLE_API_KEY` do Google AI Studio e a adicionou corretamente ao seu arquivo `.env` na raiz do projeto. Lembre-se de que o arquivo `.env` não deve ser versionado no Git.
* **`ModuleNotFoundError`:** Verifique se todas as dependências (`langchain`, `langchain-google-genai`, `python-dotenv`, `langchain-community`) foram instaladas corretamente usando `uv add` ou `pip install`.
* **Erros de Conexão:** Problemas de rede ou limites de taxa da API podem causar erros. Tente novamente após alguns segundos ou verifique sua conexão com a internet.
* **Comportamento Inesperado do Chatbot:** Se o chatbot não estiver mantendo o contexto ou respondendo de forma estranha, revise o `system prompt` e a forma como o `chat_history` está sendo passado para a chain. A clareza das instruções no prompt é fundamental.


## Capítulo 2: Configurando o Ambiente de Desenvolvimento Python para LangChain

**Neste capítulo, você vai aprender:**

* Como configurar um ambiente de desenvolvimento Python robusto e seguro para projetos de IA com LangChain.
* Vantagens do Linux/WSL, pyenv, zsh, Oh My Zsh e chaves SSH para produtividade e segurança.
* Gerenciamento moderno de dependências com uv e pyproject.toml.
* Práticas recomendadas para proteger chaves de API e variáveis de ambiente.
* Considerações sobre hardware para rodar LLMs locais.
* Exercícios práticos para instalar ferramentas essenciais e validar o ambiente.

---

## Vamos começar?

Antes de mergulharmos no mundo do LangChain, é fundamental garantir que nosso ambiente de desenvolvimento esteja pronto para a batalha. Configurar o ambiente certo não é apenas uma questão de conveniência, mas também de eficiência e segurança. Neste capítulo, vamos preparar o terreno para que você possa se concentrar no que realmente importa: construir aplicações incríveis com IA.

Então, antes de começarmos, respire fundo. Pegue um café (ou um chá, no meu caso, já que ironicamente não sou fã de café) e vamos passar por isso juntos, passo a passo. Lembro-me de um colega que passou horas depurando um erro complexo, apenas para descobrir que era um ponto e vírgula faltando. Ou, pior, um espaço a mais na indentação em Python. A máquina é implacável com a sintaxe, mas a satisfação de encontrar o erro é indescritível! A paciência que você exercita aqui será sua maior aliada em toda a jornada com IA. Prometo que, ao final deste capítulo, você terá uma base sólida e organizada para construir todos os projetos incríveis que virão.

### **Por que um bom ambiente de desenvolvimento é crucial?**
Um ambiente de desenvolvimento bem configurado é a fundação sobre a qual você construirá suas aplicações. Ele não apenas facilita o trabalho diário, mas também garante que você possa escalar seus projetos de forma eficiente e segura. 

Basicamente, é importante que você desenvolva em um ambiente que seja o mais próximo possível do ambiente de produção. Isso reduz problemas de compatibilidade e garante que o que funciona no seu computador também funcionará quando você for para o *deploy*.

Aqui estão alguns outros pontos-chave:
* **Consistência:** Um ambiente padronizado reduz problemas de compatibilidade e garante que todos os membros da equipe estejam na mesma página.
* **Eficiência:** Ferramentas como pyenv e Oh My Zsh aceleram o fluxo de trabalho, permitindo que você se concentre no código, não na configuração.
* **Segurança:** Proteger suas chaves de API e variáveis de ambiente é essencial para evitar vazamentos de dados e garantir a integridade do seu projeto.
* **Hardware adequado:** Considerar as especificações do seu computador é crucial, especialmente ao trabalhar com modelos de linguagem grandes (LLMs) que exigem recursos significativos. Embora esse aspecto seja mais relevante quando você for rodar LLMs locais, é importante ter em mente que um ambiente bem configurado pode fazer a diferença entre um projeto que roda suavemente e outro que trava constantemente.

### **Meu Ambiente de Batalha: Por que Linux e Ferramentas de Linha de Comando**

Sei que muitos desenvolvedores, especialmente no mundo corporativo, estão acostumados com o Windows e o PowerShell. E eu entendo perfeitamente, são ferramentas poderosas e familiares. No entanto, para o tipo de desenvolvimento que faremos aqui, e para o desenvolvimento de software em geral, eu recomendo fortemente que você abrace o ambiente Linux.

Para alguns, um terminal de computador é uma tela preta, ainda que colorida, é fria e sem vida. Para mim, quando estou no meu terminal Linux Kali com o shell Zsh todo customizado, me sinto como se estivesse tocando o solo de guitarra de "Hotel California" dos Eagles. Existe uma fluidez, uma arte, um prazer em fazer as ferramentas responderem exatamente como você quer, com o mínimo de esforço. É uma dança entre o homem e a máquina.

**Por que Linux?** A grande maioria das ferramentas de desenvolvimento, servidores de produção, contêineres (Docker) e tecnologias de nuvem rodam nativamente em Linux. Desenvolver em um ambiente semelhante ao de produção economiza uma quantidade enorme de dores de cabeça com compatibilidade, permissões de arquivo e pequenas diferenças que podem quebrar sua aplicação quando você for para o *deploy*.

**"Mas Igor, eu uso Windows!"** Sem problemas! A melhor invenção da Microsoft para desenvolvedores nos últimos anos foi o **Windows Subsystem for Linux (WSL)**. Ele permite que você rode uma distribuição Linux completa diretamente no seu Windows, com integração total. É o melhor dos dois mundos. Pessoalmente, eu uso o Kali Linux, que está disponível gratuitamente na Microsoft Store, por sua robustez e conjunto de ferramentas, mas distribuições como Ubuntu também são excelentes escolhas.

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
* **Comando de Execução:** `setup_python_kali.sh`

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

### Hands-on: Exercício 1 — Instalando pyenv e Python no Kali Linux (WSL)

**Comando de Execução (Linux/macOS):**
```sh
chmod +x setup_python_kali.sh && ./setup_python_kali.sh
```
**Comando de Execução (Windows):**
Execute o script acima dentro do WSL (Ubuntu/Kali).

**Saída Esperada (pode variar):**
```
SUCESSO! Ambiente corrigido e Python 3.12.9 instalado.
python --version
Python 3.12.9
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
* **Comando de Execução:** `setup_zsh.sh`

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

### Hands-on: Exercício 2 — Instalando o Terminal Perfeito (zsh + Oh My Zsh)

**Comando de Execução (Linux/macOS):**
```sh
chmod +x setup_zsh.sh && ./setup_zsh.sh
```
**Comando de Execução (Windows):**
Execute o script acima dentro do WSL.

**Saída Esperada (pode variar):**
```
Instalação e configuração do Zsh e Oh My Zsh concluídas!
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
* **Nome do Arquivo:** `generate_ssh_key.sh`  
* **Dependências:** openssh-client  
* **Comando de Execução:** `generate_ssh_key.sh`

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

### Hands-on: Exercício 3 — Gerando sua Chave SSH para o GitHub

**Comando de Execução (Linux/macOS):**
```sh
chmod +x generate_ssh_key.sh && ./generate_ssh_key.sh
```
**Comando de Execução (Windows):**
Execute o script acima dentro do WSL.

**Saída Esperada (pode variar):**
```
Copie a chave pública abaixo e cole nas configurações do seu GitHub:
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAr...
```

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

### Hands-on: Exercício 4 — Gerenciando Dependências com uv

**Comando de Execução (Linux/macOS/WSL):**
```sh
uv add langchain
```
**Saída Esperada (pode variar):**
```
Added langchain to pyproject.toml
```

### **Gerenciando Segredos: Chaves de API e Variáveis de Ambiente**

Para usar modelos de IA como os do Google Gemini, você precisará de uma **chave de API (API Key)**. É extremamente importante que você **nunca, jamais, em hipótese alguma**, coloque sua chave de API diretamente no seu código-fonte, especialmente se você planeja compartilhar esse código ou versioná-lo com o Git. Isso seria como deixar a chave da sua casa debaixo do tapete da porta.

A prática correta é usar **variáveis de ambiente**. A biblioteca python-dotenv nos ajuda a carregar essas variáveis de um arquivo para o nosso ambiente.

Como obter sua chave de API gratuita do Google Gemini:  
O Google oferece uma camada gratuita muito generosa para desenvolvedores que querem experimentar a API Gemini. A maneira mais fácil de obter uma chave é através do Google AI Studio.

1. Vá para aistudio.google.com/apikey.  
2. Faça login com sua conta do Google.  
3. Clique em "Create API key in new project".  
4. Copie a chave gerada. É isso! Você não precisa configurar um projeto complexo no Google Cloud ou adicionar um cartão de crédito para começar.

**Configurando a chave no seu projeto:**

1. **Crie um arquivo .env:** Na raiz da pasta do seu projeto, crie um arquivo chamado .env.  
2. **Adicione sua chave de API ao arquivo .env:** Abra o arquivo .env e adicione sua chave da seguinte forma:  
   GOOGLE_API_KEY="sua_chave_api_aqui"

3. **Ignore o arquivo .env no Git:** Para garantir que você nunca envie acidentalmente seus segredos para um repositório público, crie um arquivo chamado .gitignore na raiz do seu projeto e adicione a seguinte linha a ele:  
   # Ambiente virtual  
   .venv/

   # Arquivo de segredos  
   .env

   # Cache do Python  
   __pycache__/

É fundamental ir além de apenas esconder as chaves. Adote o **princípio do menor privilégio**: suas chaves de API devem ter apenas as permissões mínimas necessárias para a tarefa que irão executar. 

Por exemplo, se uma chave só precisa ler dados, ela não deve ter permissão para escrever ou deletar. Para ambientes de produção, considere o uso de serviços de gerenciamento de segredos como Azure KeyVault ou AWS Secret Manager. 

É crucial entender que o ambiente de estudos e prototipagem, onde a conveniência é prioridade, difere significativamente de um ambiente de produção, que exige rigorosas práticas de segurança corporativa, como auditorias regulares, controle de acesso baseado em função (RBAC) e monitoramento contínuo. Além disso, a **rotação periódica de chaves** é uma boa prática de segurança. Defina um cronograma para gerar novas chaves e invalidar as antigas, minimizando o risco em caso de vazamento.

### **Considerações sobre Hardware**

Antes de encerrar este capítulo sobre ambiente, é importante tocar em um ponto que muitos desenvolvedores de IA enfrentam: o hardware. Especialmente se você planeja experimentar com modelos de linguagem locais (como os que rodam via Ollama, que abordaremos mais adiante), a capacidade da sua máquina se torna um fator crucial.

Eu, por exemplo, tenho um PC servidor de LLM em casa. É uma máquina modesta, com uma RTX 4060 de 8GB de VRAM. Para muitos, 8GB pode parecer pouco, e de fato, limita o tamanho dos modelos que consigo rodar eficientemente (geralmente até modelos de 8 bilhões de parâmetros). Mas mesmo com essa configuração, consigo gerar respostas a uma taxa de 40+ tokens por segundo, o que é incrivelmente rápido para experimentação e desenvolvimento local. Essa experiência me ensinou que não é preciso ter um supercomputador para começar a explorar o mundo dos LLMs locais, mas entender as limitações do seu hardware é fundamental para gerenciar as expectativas e otimizar seus experimentos.

---

### Hands-on: Exercício — Hello, Ambiente Python!
* **Objetivo:** Validar o ambiente Python e executar o primeiro código com LangChain.
* **Nome do Arquivo:** `exercicios/capitulo_02/main.py`
* **Dependências:** `langchain`, `python-dotenv`
* **Comando de Instalação:**
```sh
uv add langchain python-dotenv
```

```python
# exercicios/capitulo_02/exercicio_1/main.py
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
prompt = ChatPromptTemplate.from_template("Diga olá para o mundo do LangChain!")
print(prompt.format())
```

**Comando de Execução (Linux/macOS):**
```sh
chmod +x exercicios/capitulo_02/exercicio_1/run.sh
./exercicios/capitulo_02/exercicio_1/run.sh
```
**Comando de Execução (Windows):**
```bat
REM Execute o exercício no Windows
exercicios\capitulo_02\exercicio_1\run.bat
```
**Saída Esperada (pode variar):**
```
Diga olá para o mundo do LangChain!
```
**Troubleshooting Comum:**
* `ModuleNotFoundError`: Verifique se todas as dependências foram instaladas corretamente usando `uv add`.
* Problemas de permissão: Use `chmod +x` para scripts `.sh`.
* Variáveis de ambiente não carregadas: Certifique-se de que o arquivo `.env` está na raiz do projeto.

---

### Pontos Chave
* Um ambiente de desenvolvimento bem configurado (Linux/WSL, pyenv, zsh) é crucial para produtividade em IA.
* Gerenciamento de dependências com `uv` e `pyproject.toml` oferece velocidade e consistência.
* A segurança das chaves de API (variáveis de ambiente, `.env`, `.gitignore`) é fundamental para qualquer projeto de IA.
* Compreender as limitações de hardware é importante ao trabalhar com LLMs locais.

---

### Resumo do Capítulo
Neste capítulo, montamos um ambiente de desenvolvimento Python profissional, robusto e seguro, preparando o terreno para construir aplicações de IA de alta qualidade.

* Ambiente Linux: Vantagens de desenvolver em Linux (via WSL) para garantir compatibilidade com ferramentas e servidores de produção.
* Gerenciamento de Versões com pyenv: Instalação e uso do pyenv para múltiplas versões do Python sem conflitos.
* Terminal e Git: Terminal turbinado com zsh e Oh My Zsh, chaves SSH para interagir com o GitHub de forma segura.
* Gerenciamento de Dependências com uv: Evolução do gerenciamento de pacotes em Python, adoção do uv por sua velocidade e simplicidade.
* Gerenciamento de Segredos: Passo a passo para obter e configurar uma chave gratuita do Google AI Studio usando um arquivo .env.

---
### Teste seu Conhecimento

1. Qual é a principal vantagem de usar o WSL (Windows Subsystem for Linux) para desenvolvimento Python?
  a) Permite rodar aplicativos Windows no Linux  
  b) Proporciona um ambiente Linux nativo dentro do Windows, facilitando compatibilidade e produtividade  
  c) Melhora a performance do Windows  
  d) Instala automaticamente todas as dependências Python

2. Para que serve a ferramenta pyenv?
  a) Gerenciar ambientes virtuais  
  b) Atualizar pacotes Python automaticamente  
  c) Instalar e gerenciar múltiplas versões do Python sem conflitos  
  d) Proteger variáveis de ambiente

3. Qual arquivo é o padrão moderno para definir as dependências e metadados de um projeto Python?
  a) requirements.txt  
  b) setup.py  
  c) environment.yml  
  d) pyproject.toml

4. Por que é recomendado usar chaves SSH em vez de HTTPS para interagir com o GitHub?
  a) HTTPS é mais rápido  
  b) Chaves SSH oferecem mais segurança e praticidade, evitando digitação de senhas  
  c) SSH permite editar arquivos diretamente no GitHub  
  d) HTTPS não funciona em ambientes Linux

5. Qual comando você usaria com uv para adicionar uma nova dependência ao projeto?
  a) uv install <pacote>  
  b) pip add <pacote>  
  c) uv add <pacote>  
  d) python -m uv <pacote>

---

**Respostas:**  
1. b  
2. c  
3. d  
4. b  
5. c

---

### Projeto Hands-on: Melhorando o Chatbot Simples

Crie um projeto Python que utilize LangChain para construir um chatbot simples. Use uv para gerenciar dependências, proteja sua chave de API com .env e documente todos os comandos usados. Experimente rodar o projeto em diferentes versões do Python usando pyenv e compartilhe o repositório via SSH no GitHub.

## Capítulo 3: Manipulação de Prompts e Modelos de Linguagem com LangChain

**Neste capítulo, você vai aprender:**

* Os fundamentos da engenharia de prompts e como ela impacta a qualidade das respostas dos LLMs.
* Como criar e utilizar PromptTemplates dinâmicos e reutilizáveis no LangChain.
* Integração de modelos de linguagem (LLMs) com prompts usando a LCEL.
* Exercício prático de tradutor multilíngue com exemplos de código, instruções de execução e troubleshooting.
* Tabelas, fluxogramas, dicas avançadas e teste de conhecimento para consolidar o aprendizado.
* Como criar prompts para diferentes tipos de tarefas: geração, classificação, extração, tradução e sumarização.
* Estratégias para depuração e avaliação de prompts.
* Boas práticas para modularização e reuso de templates em projetos maiores.

---

### A Arte e a Ciência da Engenharia de Prompts

Se os modelos de linguagem são como gênios poderosos, os prompts são os nossos pedidos. A forma como fazemos o pedido — as palavras que usamos, a estrutura que damos, o contexto que fornecemos — determina drasticamente a qualidade da resposta que recebemos. Isso é o que chamamos de **Engenharia de Prompts**: a disciplina de projetar e otimizar as instruções dadas aos modelos de linguagem para obter os resultados desejados.

Não se trata de "adivinhar" as palavras mágicas. É uma disciplina que mistura criatividade, lógica e experimentação. Um bom prompt é claro, conciso e específico. Ele guia o modelo, em vez de deixá-lo vagando. O LangChain nos oferece ferramentas para elevar nossa engenharia de prompts de simples strings para templates dinâmicos e reutilizáveis.

**Dicas Avançadas:**
- Teste diferentes variações de prompts e compare resultados usando LangSmith ou logs.
- Use exemplos (few-shot) dentro do prompt para orientar o modelo em tarefas complexas.
- Adote padrões como Chain-of-Thought para estimular raciocínio passo a passo.
- Documente e versiona seus templates para facilitar manutenção e evolução do projeto.

### Templates de Prompt: Reutilização e Dinamismo

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

**Outros usos de PromptTemplates:**
- Tradução automática entre idiomas.
- Geração de respostas personalizadas para diferentes perfis de usuário.
- Extração de informações estruturadas (ex: dados em JSON).
- Classificação de sentimentos ou tópicos.

A engenharia de prompts é sobre encontrar a combinação de palavras e estrutura que faz o modelo responder de forma precisa e criativa. Um prompt bem construído resulta em respostas melhores e mais úteis.

Neste capítulo, vamos aprender a afinar nossos templates e técnicas para criar prompts que realmente funcionam.

### Integrando Modelos de Linguagem (LLMs)

Um prompt, por si só, é apenas texto. Ele precisa ser enviado a um modelo para ganhar vida. Vamos usar o Gemini do Google.

```python
# Supondo que você já configurou seu ambiente como no Capítulo 2
from langchain_google_genai import ChatGoogleGenerativeAI

# Inicializa o modelo
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
# 'temperature' é um parâmetro que controla a criatividade da resposta.
# 0 é mais determinístico, 1 é mais criativo.
```

Para conectar o prompt_template com o llm, usamos a **LangChain Expression Language (LCEL)**, com o operador pipe (|):

```python
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

O pipeline criado pelo operador | torna o fluxo de dados entre componentes simples e legível.

**Dicas de Integração:**
- Combine PromptTemplates com parsers de saída para garantir respostas no formato desejado.
- Use o operador pipe (|) para criar pipelines flexíveis e testáveis.
- Experimente diferentes modelos (Gemini, Claude, GPT) e compare resultados.
- Adote logs e tracing para depurar e otimizar o fluxo de dados.

---

### Hands-on: Exercício — Tradutor Multilíngue Dinâmico com LangChain

* **Objetivo:** Criar uma chain que usa um ChatPromptTemplate dinâmico para instruir um LLM a realizar traduções.
* **Nome do Arquivo:** `exercicios/capitulo_03/exercicio_1/main.py`
* **Dependências:** `langchain`, `langchain-google-genai`, `python-dotenv`
* **Comando de Instalação:**
```sh
uv add langchain langchain-google-genai python-dotenv
```

**Exemplo de Código: `exercicios/capitulo_03/exercicio_1/main.py`**

```python
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Carrega variáveis de ambiente (.env)
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise EnvironmentError("GOOGLE_API_KEY não encontrada. Adicione ao seu arquivo .env.")

# Inicializa o modelo Gemini
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# Template dinâmico para tradução
template = """Você é um tradutor multilíngue especialista.
Traduza o texto abaixo para {idioma_destino}.
Responda apenas com a tradução.

Texto:
{texto_origem}
"""

prompt = ChatPromptTemplate.from_template(template)
parser = StrOutputParser()

# Pipeline LCEL: prompt -> modelo -> parser
chain = prompt | llm | parser

# Exemplos de uso
exemplos = [
    {"texto_origem": "A inteligência artificial está mudando o mundo.", "idioma_destino": "Francês"},
    {"texto_origem": "Python is a powerful programming language.", "idioma_destino": "Japonês"},
    {"texto_origem": "Hello, world!", "idioma_destino": "Klingon"},
]

for exemplo in exemplos:
    print(f"Traduzindo '{exemplo['texto_origem']}' para {exemplo['idioma_destino']}...")
    resultado = chain.invoke(exemplo)
    print(f"Resultado: {resultado}\n")
```

**Comando de Execução (Linux/macOS):**
```sh
chmod +x exercicios/capitulo_03/exercicio_1/run.sh
./exercicios/capitulo_03/exercicio_1/run.sh
```
**Comando de Execução (Windows):**
```bat
REM Execute o exercício no Windows
exercicios\capulo_03\exercicio_1\run.bat
```

**Saída Esperada (pode variar):**
Traduzindo 'A inteligência artificial está mudando o mundo.' para Francês...
Resultado: L'intelligence artificielle change le monde.

Traduzindo 'Python is a powerful programming language.' para Japonês...
Resultado: パイソンは強力なプログラミング言語です。

Traduzindo 'Hello, world!' para Klingon...
Resultado: nuqneH, yaj!

---

**Troubleshooting Comum:**
* `AuthenticationError` ou `GOOGLE_API_KEY` não configurada: Certifique-se de que você obteve sua chave do Google AI Studio e a adicionou corretamente ao arquivo `.env`.
* Respostas Inesperadas: Use `temperature=0` para traduções literais. Se persistir, revise o template ou o idioma solicitado.
* Erros de Conexão: Verifique sua internet ou limites de uso da API.
* Prompt não retorna o formato esperado: Adicione instruções claras sobre o formato desejado (ex: "Responda apenas com a tradução").
* Traduções para idiomas fictícios: Teste limites do modelo e documente resultados curiosos.

---

### Pontos Chave
* Engenharia de Prompts é crucial para obter respostas de qualidade dos LLMs.
* `PromptTemplates` no LangChain permitem prompts dinâmicos e reutilizáveis.
* LLMs são integrados e orquestrados eficientemente com o LangChain.
* A LCEL simplifica a construção de pipelines, tornando-os mais legíveis e eficientes.
* Exercícios práticos solidificam o aprendizado dos conceitos de prompts e modelos.
* Modularize templates para facilitar reuso e manutenção.
* Use logs, tracing e testes para depurar e evoluir seus prompts.

---

### Resumo do Capítulo
Neste capítulo, mergulhamos na arte e ciência da engenharia de prompts e como o LangChain nos ajuda a dominar essa habilidade.

* Engenharia de Prompts: A qualidade da interação com LLM depende da clareza e estrutura das instruções.
* Templates de Prompt: Modularidade e reutilização com PromptTemplates.
* Integração de LLMs: Inicialização e conexão de modelos ao template.
* LCEL: Pipeline elegante com operador pipe (|).
* Exercício Prático: Tradutor multilíngue usando variáveis dinâmicas em prompts.
* Estratégias para depuração, avaliação e evolução de prompts em projetos reais.

---

### Teste seu Conhecimento
1. Qual é o principal benefício de usar PromptTemplates em vez de strings formatadas (f-strings)?
   a) PromptTemplates são mais rápidos de executar.
   b) Eles permitem criar prompts modulares, reutilizáveis e mais fáceis de manter.
   c) Apenas PromptTemplates podem ser usados com modelos de chat.
   d) Eles usam menos tokens de API.
2. No exemplo do tradutor, qual componente foi responsável por transformar a saída do modelo de um objeto de mensagem para uma string simples?
   a) ChatGoogleGenerativeAI
   b) ChatPromptTemplate
   c) StrOutputParser
   d) load_dotenv
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

**Respostas:**
1. b
2. c
3. c
4. b
5. d

---

### Projeto Hands-on: Melhorando o Chatbot Simples

Coloque em prática os conceitos do capítulo criando um chatbot simples com LangChain, PromptTemplates e LCEL. Implemente funcionalidades como tradução automática, ajuste de tom e número de pontos em respostas. Documente comandos de execução, proteja chaves de API com .env e compartilhe o projeto via GitHub usando SSH.


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

* **Objetivo:** Construir um agente simples que pode usar uma ferramenta de busca para responder a perguntas factuais.
* **Nome do Arquivo:** `exercicios/capitulo_05/exercicio_1/main.py`
* **Dependências:** `langchain`, `langchain-google-genai`, `langchain-tavily`, `python-dotenv`
* **Comando de Instalação:**
```sh
uv add langchain langchain-google-genai langchain-tavily python-dotenv
```
* **Configuração Adicional:** Adicione sua chave de API da Tavily ao arquivo `.env` como `TAVILY_API_KEY`.

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


## Capítulo 6: Ferramentas e Agentes: Capacitando LLMs com Ações

**Neste capítulo, você vai aprender:**

* Como equipar LLMs com ferramentas externas para criar agentes autônomos e interativos.
* Diferenças entre ferramentas (Tools) e agentes (Agents) no LangChain.
* Implementação prática de agentes com ferramentas customizadas, APIs externas e integração via LangGraph.
* Exercícios práticos de análise de vendas e cotação de moedas, com instruções de execução, troubleshooting e dicas de modularização.
* Pontos chave, checklist e projeto hands-on para consolidar o aprendizado sobre agentes e ferramentas.

---

Neste capítulo, exploraremos um dos conceitos mais poderosos do LangChain: a capacidade de equipar Large Language Models (LLMs) com ferramentas externas, transformando-os em agentes autônomos capazes de interagir com o mundo real. Veremos como os agentes podem raciocinar sobre qual ferramenta usar, executar ações e observar os resultados para alcançar seus objetivos. O padrão ReAct é recomendado para raciocínio iterativo e uso eficiente de ferramentas.

### **6.1. O que são Ferramentas (Tools)?**

No contexto do LangChain, uma **Ferramenta (Tool)** é uma função que um agente pode invocar para interagir com o mundo exterior. Isso pode incluir:

*   **APIs externas:** Buscar informações na web, enviar e-mails, acessar bancos de dados, etc.
*   **Funções customizadas:** Realizar cálculos complexos, manipular dados, interagir com sistemas internos.
*   **Outros modelos de IA:** Chamar modelos de visão computacional, processamento de fala, etc.

Ferramentas podem ser funções decoradas com `@tool`, instâncias de classes Tool, ou carregadas via `load_tools` para integrações externas. Descrições detalhadas são essenciais para o LLM decidir o uso correto da ferramenta. Recomenda-se testar ferramentas isoladamente antes de integrá-las ao agente.

### **6.2. Agentes (Agents): O Cérebro por Trás das Ações**

Um **Agente (Agent)** é um sistema que utiliza um LLM como seu "cérebro" para decidir qual ação tomar, observar o resultado dessa ação e repetir o processo até que a tarefa seja concluída. O processo geralmente segue o padrão **ReAct (Reason + Act)**:

1.  **Reason (Raciocinar):** O LLM analisa a entrada do usuário e o estado atual para determinar qual ferramenta (se houver) deve ser usada e com quais argumentos.
2.  **Act (Agir):** A ferramenta selecionada é executada, e o resultado é observado.
3.  **Observe (Observar):** O LLM recebe o resultado da execução da ferramenta e o utiliza para refinar seu raciocínio ou gerar a resposta final.

O LangChain oferece diversas implementações de agentes, mas a abordagem moderna e recomendada é o `create_tool_calling_agent` (LangChain) ou `create_react_agent` (LangGraph), que se beneficiam das capacidades de *tool calling* nativas dos LLMs mais recentes. Prompts podem ser customizados para orientar o agente. Recomenda-se uso de streaming (`agent_executor.stream`) para inspecionar o raciocínio do agente passo a passo.

---

### Hands-on: Exercício 1 — Agente de Análise de Vendas com Ferramenta SQL

* **Objetivo:** Criar um agente que utilize uma ferramenta SQL para consultar dados de vendas e responder a perguntas complexas.
* **Nome do Arquivo:** `exercicios/capitulo_06/exercicio_1/main.py`
* **Dependências:** `langchain`, `langchain-google-genai`, `python-dotenv`
* **Comando de Instalação:**
```sh
uv add langchain langchain-google-genai python-dotenv
```
* **Configuração Adicional:** Certifique-se de que sua chave de API do Google Gemini (`GOOGLE_API_KEY`) está configurada corretamente no seu arquivo `.env`.

```python
# exercicios/capitulo_06/exercicio_1/main.py
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
cd exercicios/capitulo_06/exercicio_1
chmod +x run.sh
./run.sh
```
**Comando de Execução (Windows):**
```bat
cd exercicios\capitulo_06\exercicio_1
call run.bat
```
**Saída Esperada (pode variar):**
```
Agente de Análise de Vendas pronto! Faça sua pergunta.
> Pergunta: Qual a quantidade total de Laptops vendidos?
< Resposta Final: ...
> Pergunta: Qual o produto mais vendido em termos de quantidade?
< Resposta Final: ...
> Pergunta: Qual o valor total de vendas?
< Resposta Final: ...
> Pergunta: Quantos itens foram vendidos em 2024-01-18?
< Resposta Final: ...
> Pergunta: Qual o nome do meu cachorro?
< Resposta Final: Não tenho informações sobre isso.
```
**Troubleshooting Comum:**
* `sqlite3.OperationalError: no such table: vendas`: Verifique se a função `setup_database()` está sendo chamada corretamente.
* `AuthenticationError`: Verifique a chave de API do Gemini no `.env`.
* `ModuleNotFoundError`: Instale todas as dependências com `uv add`.

---

### Hands-on: Exercício 2 — Agente de Cotação de Moedas com Ferramenta de API Externa

* **Objetivo:** Criar um agente que utilize uma ferramenta para consultar taxas de câmbio de moedas via API externa.
* **Nome do Arquivo:** `exercicios/capitulo_06/exercicio_2/main.py`
* **Dependências:** `langchain`, `langchain-google-genai`, `python-dotenv`, `requests`
* **Comando de Instalação:**
```sh
uv add langchain langchain-google-genai python-dotenv requests
```
* **Configuração Adicional:** Se usar uma API que exija chave, adicione ao `.env` (ex: `EXCHANGE_RATE_API_KEY`).

```python
# exercicios/capitulo_06/exercicio_2/main.py
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool
import requests
import os

# Carregar variáveis de ambiente
load_dotenv()

# 1. Definir a ferramenta de cotação de moedas
@tool
def get_exchange_rate(base_currency: str, target_currency: str) -> str:
    """
    Obtém a taxa de câmbio atual entre duas moedas.
    Use esta ferramenta para converter valores entre moedas.
    Exemplo: get_exchange_rate("USD", "BRL")
    """
    try:
        # Usando uma API de cotação de moedas gratuita (ex: ExchangeRate-API)
        # Você pode precisar se registrar para obter uma chave de API real
        # Para fins de demonstração, usaremos um endpoint público ou simulado
        api_key = os.getenv("EXCHANGE_RATE_API_KEY") # Se necessário
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()
        
        if data and data["rates"] and target_currency in data["rates"]:
            rate = data["rates"][target_currency]
            return f"A taxa de câmbio de {base_currency} para {target_currency} é {rate}"
        else:
            return f"Não foi possível obter a taxa de câmbio para {base_currency}/{target_currency}"
    except Exception as e:
        return f"Erro ao obter a taxa de câmbio: {e}"

# 2. Escolher o LLM que será o cérebro do nosso agente
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# 3. Definir as ferramentas que o agente pode usar
tools = [get_exchange_rate]

# 4. Criar o Prompt do Agente
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente especializado em cotação de moedas. Use a ferramenta 'get_exchange_rate' para responder a perguntas sobre taxas de câmbio."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# 5. Criar o Agente
agent = create_tool_calling_agent(llm, tools, prompt)

# 6. Criar o Executor do Agente
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- Execução ---
if __name__ == "__main__":
    print("Agente de Cotação de Moedas pronto! Faça sua pergunta.")

    perguntas = [
        "Qual a taxa de câmbio de USD para BRL?",
        "Quanto é 100 EUR em JPY?",
        "Qual o valor do dólar hoje?",
        "Qual o nome do meu gato?"
    ]

    for pergunta in perguntas:
        print(f"\n> Pergunta: {pergunta}")
        response = agent_executor.invoke({"input": pergunta})
        print(f"\n< Resposta Final: {response['output']}")
```

**Comando de Execução (Linux/macOS):**
```sh
cd exercicios/capitulo_06/exercicio_2
chmod +x run.sh
./run.sh
```
**Comando de Execução (Windows):**
```bat
cd exercicios\capitulo_06\exercicio_2
call run.bat
```
**Saída Esperada (pode variar):**
```
Agente de Cotação de Moedas pronto! Faça sua pergunta.
> Pergunta: Qual a taxa de câmbio de USD para BRL?
< Resposta Final: ...
> Pergunta: Quanto é 100 EUR em JPY?
< Resposta Final: ...
> Pergunta: Qual o valor do dólar hoje?
< Resposta Final: ...
> Pergunta: Qual o nome do meu gato?
< Resposta Final: Não tenho informações sobre isso.
```
**Troubleshooting Comum:**
* `requests.exceptions.ConnectionError`: Verifique sua conexão com a internet.
* `AuthenticationError`: Verifique a chave de API do Gemini no `.env`.
* `ModuleNotFoundError`: Instale todas as dependências com `uv add`.

---

### Troubleshooting Comum
* Debug de ferramentas: teste funções isoladamente e verifique logs detalhados com `verbose=True`.
* Use tracing para inspeção de execuções e identificar gargalos.
* Instale todas as dependências e configure corretamente o `.env`.
* Proteja chaves de API e modularize ferramentas para facilitar manutenção.

---

### Pontos Chave
* Ferramentas permitem que LLMs interajam com sistemas externos e superem limitações.
* Agentes usam LLMs para raciocinar, decidir e executar ações com ferramentas.
* O padrão ReAct (Reason + Act) e prompts customizados são diferenciais para agentes autônomos eficientes.
* Exercícios práticos mostram integração com banco de dados, APIs externas e modularização.

---

### Resumo do Capítulo
Neste capítulo, você aprendeu como equipar LLMs com ferramentas externas, criando agentes autônomos e interativos no LangChain. Viu a diferença entre ferramentas e agentes, implementou agentes com ferramentas customizadas e APIs externas, e consolidou o aprendizado com exercícios práticos, troubleshooting e dicas de boas práticas.

---

### Teste seu Conhecimento
1. No LangChain, o que é uma Ferramenta (Tool)?
   a) Um modelo de linguagem.
   b) Uma função que o agente pode invocar para interagir com sistemas externos.
   c) Um arquivo de configuração.
   d) Um tipo de prompt especial.
2. Qual é o papel do agente em um sistema LangChain?
   a) Executar comandos de sistema.
   b) Raciocinar, decidir qual ferramenta usar e observar resultados.
   c) Gerar apenas texto sem interação externa.
   d) Armazenar dados em banco de dados.
3. O padrão ReAct (Reason + Act) envolve:
   a) Apenas raciocinar sobre a entrada do usuário.
   b) Raciocinar, agir usando ferramentas e observar resultados.
   c) Executar comandos sem raciocínio.
   d) Gerar prompts estáticos.
4. Qual erro pode ocorrer se a tabela 'vendas' não for criada corretamente?
   a) requests.exceptions.ConnectionError
   b) sqlite3.OperationalError: no such table: vendas
   c) ModuleNotFoundError
   d) AuthenticationError
5. Para consultar taxas de câmbio em tempo real, o agente precisa:
   a) Apenas um LLM.
   b) Uma ferramenta que acesse uma API externa.
   c) Um arquivo .env vazio.
   d) Um banco de dados local.
6. Como inspecionar o raciocínio do agente passo a passo?
   a) Usando agent_executor.stream para visualizar cada etapa.
   b) Executando apenas o LLM sem ferramentas.
   c) Ignorando logs.
   d) Usando prompts estáticos.

**Respostas:**
1. b
2. b
3. b
4. b
5. b
6. a

---

### Projeto Hands-on: Orquestrando Ferramentas e Agentes

Coloque em prática os conceitos do capítulo criando um projeto Python que utiliza LangChain para construir um agente capaz de integrar múltiplas ferramentas: uma para análise de dados locais (ex: vendas) e outra para consulta de APIs externas (ex: cotação de moedas). Siga a estrutura sugerida:

- Estrutura de diretórios para agentes e ferramentas.
- Checklist de boas práticas: modularização, logging, versionamento, testes automatizados.
- Fluxograma do fluxo de decisão do agente.
- Dicas para integração de múltiplas ferramentas e fontes de dados.
- Passos para ativar tracing e compartilhar logs via GitHub.
- Experimente rodar o projeto em diferentes versões do Python usando pyenv.


## Capítulo 7: Técnicas Avançadas: Memória, Feedback e Aprendizado Contínuo

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


## Capítulo 10: Projeto Final Integrador — Assistente de Viagem Inteligente

**Neste capítulo, você vai aprender:**

* Como integrar múltiplos conceitos do LangChain em um projeto robusto.
* Construir um agente de viagem inteligente que pesquisa destinos, clima, atrações e gerencia orçamento.
* Utilizar ferramentas externas (Tavily) e customizadas no LangChain.
* Orquestrar interações com LLM, ferramentas e gerenciamento de segredos.
* Documentar comandos, troubleshooting, pontos chave e testar conhecimento.

---

### Hands-on: Exercício — Assistente de Viagem Inteligente

* **Objetivo:** Desenvolver um agente completo que auxilia no planejamento de viagens, combinando pesquisa e gerenciamento de orçamento.
* **Nome do Arquivo:** `exercicios/capitulo_09/exercicio_1/main.py`
* **Dependências:** `langchain`, `langchain-google-genai`, `langchain-tavily`, `python-dotenv`
* **Comando de Instalação:**
```sh
uv add langchain langchain-google-genai langchain-tavily python-dotenv
```
* **Configuração Adicional:** Adicione sua chave de API da Tavily ao arquivo `.env` como `TAVILY_API_KEY`.

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
        return f"Item '{item}' com custo de R${custo:.2f} adicionado ao orçamento. Orçamento atual: {self.orcamento}"

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

**Comando de Execução (Linux/macOS):**
```sh
chmod +x capitulo_09/execucao_exercicio_9_1.sh
./capitulo_09/execucao_exercicio_9_1.sh
```
**Comando de Execução (Windows):**
```bat
REM Execute o exercício no Windows
capitulo_09\execucao_exercicio_9_1.bat
```
**Saída Esperada (pode variar):**
```
Assistente de Viagem pronto! Como posso ajudar a planejar sua próxima aventura?
> Pergunta: Qual o clima em Paris em agosto?
< Resposta Final: ...
> Pergunta: Quais são as principais atrações turísticas em Roma?
< Resposta Final: ...
> Pergunta: Adicione 'Passagem Aérea' com custo de 2500.00 ao orçamento.
< Resposta Final: ...
> Pergunta: Adicione 'Hospedagem' com custo de 1200.00 ao orçamento.
< Resposta Final: ...
> Pergunta: Qual o meu orçamento total até agora?
< Resposta Final: ...
> Pergunta: Preciso de ideias para uma viagem de aventura na América do Sul.
< Resposta Final: ...
> Pergunta: Qual o custo de um jantar em um restaurante médio em Tóquio?
< Resposta Final: ...
> Pergunta: Qual o meu orçamento total?
< Resposta Final: ...
```
**Troubleshooting Comum:**
* `AuthenticationError` ou `TAVILY_API_KEY` não configurada: Verifique se a chave está correta no `.env`.
* `GOOGLE_API_KEY` não configurada: Verifique se está no `.env`.
* `ModuleNotFoundError`: Instale todas as dependências com `uv add`.
* Erros de conexão: Verifique sua internet e limites de API.
* Agente não usando a ferramenta: Revise as descrições das ferramentas.
* Saída inesperada: Ative `verbose=True` para inspecionar o raciocínio do agente.

---

### Pontos Chave
* Projetos integradores consolidam múltiplos conceitos do LangChain.
* Agentes com múltiplas ferramentas resolvem tarefas complexas e reais.
* LCEL facilita a composição de pipelines robustos.
* Segurança no gerenciamento de chaves de API é fundamental.

---

### Resumo do Capítulo
Neste capítulo, você aplicou todos os conceitos aprendidos para construir um Assistente de Viagem Inteligente. O projeto final demonstrou como orquestrar agentes, integrar ferramentas externas e customizadas, aplicar LCEL e gerenciar segredos de forma segura.

---

### Teste seu Conhecimento

1. Qual o principal benefício de usar múltiplas ferramentas em um agente?
   a) Reduz o custo das chamadas de API.
   b) Permite que o agente execute tarefas mais complexas e diversificadas.
   c) Aumenta a velocidade de resposta do LLM.
   d) Elimina a necessidade de um LLM.
2. No Assistente de Viagem, qual ferramenta seria usada para descobrir "Qual o clima em Paris em agosto?"
   a) adicionar_item_orcamento
   b) ver_orcamento_total
   c) search_tool
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

**Respostas:**
1. b
2. c
3. c
4. b
5. c

---

### Projeto Hands-on: Assistente de Viagem Inteligente

Coloque em prática os conceitos do capítulo criando um projeto Python com LangChain para ser um assistente de viagem inteligente. Implemente pesquisa de destinos, clima, atrações, gerenciamento de orçamento e integração de múltiplas ferramentas. Documente todos os comandos usados, proteja suas chaves de API com .env e compartilhe o repositório via SSH no GitHub. Experimente rodar o projeto em diferentes versões do Python usando pyenv.


## Conclusão

Ao longo deste e-book, você percorreu uma jornada completa pelo universo do LangChain, desde a configuração do ambiente até a construção de agentes inteligentes prontos para produção. Explorou conceitos fundamentais de IA, engenharia de contexto, ferramentas, agentes, memória, feedback, testes, debugging, otimização, segurança e integração de múltiplas tecnologias.

Você aprendeu a:
* Montar um ambiente Python robusto e seguro, com Linux/WSL, pyenv, zsh, Oh My Zsh e gerenciamento moderno de dependências.
* Proteger segredos, chaves de API e garantir boas práticas de segurança.
* Construir chains, agentes autônomos, multiagentes e integrar ferramentas externas e customizadas.
* Implementar memória, feedback e aprendizado contínuo para agentes evolutivos.
* Testar, debugar, monitorar e otimizar aplicações LangChain com LangSmith, tracing, logs e CI/CD.
* Orquestrar projetos práticos, como chatbots, assistentes de viagem e sistemas corporativos, aplicando LCEL e boas práticas de produção.

Mais do que aprender técnicas, você desenvolveu a capacidade de criar soluções reais, seguras, escaláveis e inovadoras com IA generativa. O domínio do LangChain abre portas para aplicações que vão desde protótipos até sistemas robustos em produção, com observabilidade, segurança e integração contínua.

Ao aplicar os conhecimentos adquiridos, você está apto a enfrentar desafios do mundo real, seja desenvolvendo assistentes inteligentes para empresas, automatizando processos, ou criando experiências personalizadas para usuários. O LangChain permite que você aproveite o poder dos LLMs para construir aplicações flexíveis, adaptáveis e preparadas para evoluir conforme novas demandas surgem.

Além disso, você aprendeu a importância da colaboração e do compartilhamento de conhecimento. A comunidade LangChain está em constante crescimento, e contribuir com projetos open source, tutoriais e exemplos práticos é uma excelente forma de se manter atualizado e ajudar outros desenvolvedores a avançar na área de IA generativa.

### Visão de Mercado e Oportunidades

O mercado de IA generativa está em rápida expansão, com demanda crescente por profissionais capazes de criar soluções inovadoras e seguras. Empresas de diversos setores buscam especialistas em LangChain para desenvolver assistentes inteligentes, sistemas de automação, análise de dados avançada e integração de LLMs em processos críticos. Dominar LangChain posiciona você como protagonista em projetos de alto impacto, seja em startups, grandes corporações ou iniciativas acadêmicas.

A capacidade de unir conhecimento técnico, criatividade e visão de negócio é um diferencial competitivo. Projetos bem estruturados com LangChain podem transformar a experiência do usuário, otimizar operações e abrir novas fontes de receita. O ecossistema está em constante evolução, com novas ferramentas, APIs e integrações surgindo a cada mês. Manter-se atualizado e contribuir para a comunidade são atitudes essenciais para o crescimento profissional.

### Protagonismo e Colaboração

O protagonismo do leitor é fundamental para o avanço da área. Compartilhe seus aprendizados, publique tutoriais, participe de fóruns e eventos, e colabore com outros desenvolvedores. O trabalho em equipe, a troca de experiências e o engajamento em projetos open source aceleram o desenvolvimento de soluções cada vez mais sofisticadas e seguras.

A colaboração internacional é uma marca do universo LangChain. Aproveite oportunidades de networking, participe de hackathons, contribua com documentação e exemplos práticos. O futuro da IA generativa depende do envolvimento ativo de profissionais comprometidos com a ética, a inovação e o impacto positivo na sociedade.

### Próximos Passos

- Continue explorando novas ferramentas, APIs e integrações.
- Compartilhe seus projetos, contribua com a comunidade e mantenha-se atualizado.
- Experimente diferentes LLMs, arquiteturas e desafios práticos.
- Aplique os conceitos em problemas reais do seu dia a dia ou empresa.
- Participe de fóruns, eventos e grupos de discussão para expandir sua rede de contatos e aprender com outros profissionais.
- Mantenha-se atento às novidades do ecossistema LangChain e IA generativa, acompanhando lançamentos, atualizações e tendências do mercado.
- Busque certificações, cursos avançados e especializações para aprofundar seu conhecimento.
- Desenvolva projetos autorais e compartilhe resultados em plataformas como GitHub, Medium e LinkedIn.

---

#### O próximo passo: Design de agentes e workflows com LangChain

À medida que você avança, é fundamental entender os padrões de design para agentes e workflows em aplicações com LLMs. O artigo da Anthropic sobre agentes eficazes destaca que nem sempre a solução mais sofisticada é a melhor: muitas vezes, workflows simples e bem definidos são suficientes para a maioria dos casos. Frameworks como LangChain e LangGraph facilitam a implementação de sistemas agentic, mas é essencial saber quando utilizar agentes autônomos e quando optar por workflows orquestrados.

**Workflows** são ideais para tarefas previsíveis e bem estruturadas, onde o caminho de execução pode ser definido previamente. Já **agentes** são recomendados para problemas abertos, que exigem flexibilidade, tomada de decisão dinâmica e adaptação ao contexto. A orquestração baseada em grafos, como a proposta pelo LangGraph, permite criar sistemas híbridos, combinando workflows e agentes para maximizar eficiência e controle.

O próximo passo para quem domina LangChain é aprofundar-se nesses padrões, estudando casos de uso, experimentando diferentes arquiteturas e avaliando quando cada abordagem é mais adequada. Recomenda-se começar simples, medir resultados e só adicionar complexidade quando necessário. Transparência, simplicidade e documentação clara das ferramentas são princípios-chave para construir agentes confiáveis e escaláveis.

Para saber mais, consulte o artigo "Building Effective Agents" da Anthropic e explore frameworks como LangChain, LangGraph e Model Context Protocol para criar soluções cada vez mais avançadas e alinhadas às melhores práticas do mercado.

## Agradecimento

Parabéns por chegar até aqui! O futuro da IA está em suas mãos. Que este material seja um guia prático e inspirador para suas próximas conquistas com LangChain e IA generativa.

Lembre-se: o aprendizado é contínuo, e cada projeto é uma oportunidade de inovar, aprimorar suas habilidades e impactar positivamente o mundo ao seu redor. Continue explorando, experimentando e compartilhando suas descobertas.


## **Próximos Passos na sua Jornada**

Parabéns! Você chegou ao final deste livro e, mais importante, deu um passo gigantesco na sua jornada com a Inteligência Artificial e o LangChain. Mas lembre-se, o aprendizado é contínuo. Aqui estão algumas sugestões para seus próximos passos:

1.  **Explore o LangGraph:** Para sistemas multiagentes ainda mais complexos e com estados, o LangGraph é o próximo nível.
2.  **Aprofunde-se em RAG:** Experimente diferentes tipos de `Vector Stores`, `Embeddings` e estratégias de recuperação.
3.  **Construa seus Próprios Projetos:** A melhor forma de aprender é fazendo. Pense em problemas reais que você enfrenta e tente resolvê-los com agentes de IA.
4.  **Contribua para a Comunidade:** Compartilhe seu conhecimento, ajude outros desenvolvedores e contribua para projetos de código aberto.
5.  **Mantenha-se Atualizado:** O campo da IA avança rapidamente. Siga blogs, participe de conferências e continue experimentando.


## **Comunidade e Contato**

A jornada do aprendizado não termina aqui. Na verdade, ela está apenas começando.

* Código Fonte: Todo o código deste livro está disponível para você clonar, modificar e experimentar. Acesse o repositório em:  
  https://github.com/igormedeiros/livros/blob/main/langchain-na-pratica/  
* Comunidade no Telegram: Junte-se a outros desenvolvedores, tire dúvidas, compartilhe seus projetos e continue a conversa em nossa comunidade:  
  https://t.me/igormedeiros_comunidade  
* Feedback e Contato: Sua opinião é incrivelmente valiosa. Se você gostou deste livro, por favor, considere deixar uma avaliação na Amazon. Isso ajuda outros leitores como você a encontrar este material e me dá o feedback necessário para continuar melhorando. Para outras dúvidas, sugestões ou para saber mais sobre meu trabalho, visite meu site:  
  https://igormedeiros.com.br

Obrigado por me acompanhar nesta jornada. Agora, vá e construa algo incrível!


## **Sobre o Autor**

A jornada de Igor Medeiros é movida por um propósito forjado no amor, na dor e na superação. Filho de um herói que, em suas palavras, “samba todo dia na cara do Alzheimer”, e pai da Melissa, “a luz de sua jornada”, ele carrega em sua história a força desses dois pilares. Sua trajetória profissional de mais de duas décadas foi profundamente ressignificada após um grave desafio de saúde em 2012, que incluiu um tumor gigante na cabeça e uma embolia pulmonar no pós-operatório. **A batalha pela vida deixou marcas permanentes: a paralisia facial e a surdez unilateral total, ambas do lado direito do rosto.**

A experiência de quase morte e a reabilitação que se seguiu não foram uma pausa, mas o ponto de ignição para uma nova missão. Nesse período, sua jornada incluiu um corajoso pivô de carreira, no qual atuou como executivo de marketing e vendas. Essa imersão no lado do negócio ensinou-lhe lições valiosas sobre a importância da qualidade da entrega final e a perspectiva do cliente, visão que hoje integra a todos os seus projetos tecnológicos: usar a tecnologia para honrar a vida e gerar um impacto que realmente importe.

Como Engenheiro de Software Sênior e especialista em Java para smart cards, sua carreira o levou a palestrar por todo o Brasil e até no Japão. Ao longo de mais de 20 anos, liderou a criação de soluções robustas para diversos setores da indústria. Essa base sólida, que vai desde a homologação de sistemas criptográficos para a Casa Civil até a liderança técnica em projetos de inovação, construiu o alicerce para sua atuação atual.

Hoje, como especialista de IA Agents e evangelista de Inteligência Artificial, Igor está na vanguarda da tecnologia, liderando questões técnicas de projetos e definindo padrões para gigantes atuais dos setores financeiro e de telecomunicações, como Santander, Bradesco, Pernambucanas, TIM e o grupo Telefônica. É nesse cenário de ponta que ele desenvolve e coloca em produção sistemas complexos com agentes de IA. Ele direciona essa expertise para sua grande paixão: o setor da saúde, buscando ativamente criar soluções em neurologia que possam, um dia, reescrever histórias como a sua e de seu pai.

Além de seu trabalho corporativo, Igor é um líder de comunidade nato, que acredita que o conhecimento só tem valor quando é compartilhado. Essa vocação para o humanismo tem raízes profundas: por 14 anos, dedicou-se como voluntário em uma ONG com a missão de resgatar pessoas em situação de rua. Em um marcante contraste com seu trabalho de ponta em Inteligência Artificial, essa experiência solidificou sua crença de que a tecnologia mais avançada deve sempre servir à empatia e à conexão humana. Seja em palestras, artigos ou como mentor, ele se dedica a capacitar outros desenvolvedores, fechando o ciclo de uma jornada extraordinária que transforma gratidão em legado. Este livro é mais um passo nesse caminho.

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



## **Referências Bibliográficas**

### **Documentação Oficial e Ferramentas**
*   **Documentação Oficial do LangChain:** [https://python.langchain.com/](https://python.langchain.com/)
*   **Documentação do LangGraph:** Framework para orquestração de agentes e workflows baseados em grafos. [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)
*   **Documentação do Model Context Protocol (MCP):** Integração de ferramentas e agentes. [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)
*   **Documentação do Google AI Studio:** [https://aistudio.google.com/](https://aistudio.google.com/)
*   **Documentação da Tavily API:** [https://tavily.com/](https://tavily.com/)
*   **Documentação do Claude (Anthropic):** [https://www.anthropic.com/claude](https://www.anthropic.com/claude)

### **Livros Recomendados**
*   **"Generative AI with LangChain" de Ben Stokes**
*   **"Building LLM Powered Applications" de Josh Star**

### **Artigos e Pesquisas Fundamentais**
*   **"Attention Is All You Need" (Vaswani et al., 2017):** Arquitetura Transformer.
*   **"Language Models are Few-Shot Learners" (Brown et al., 2020):** Few-shot learning.
*   **"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (Wei et al., 2022):** Chain-of-Thought.
*   **"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (Lewis et al., 2020):** Padrão RAG.
*   **"ReAct: Synergizing Reasoning and Acting in Language Models" (Yao et al., 2022):** Padrão ReAct. [https://react-lm.github.io/](https://react-lm.github.io/)
*   **"Building Effective Agents" (Schluntz & Zhang, Anthropic, 2024):** Design patterns, agentes vs workflows, orquestração baseada em grafos. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)