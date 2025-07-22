# **LangChain na Prática: O primeiro passo com Agentes de IA**

**Igor Medeiros**

## **Informações de Copyright**

© 2025 Igor Medeiros. Todos os direitos reservados.

Este livro faz parte da série "IA na Prática".
Lançamento: 20 de Julho de 2025.
ASIN: B0FJ7L9NTM
Link do ebook na Amazon Brasil: https://www.amazon.com.br/dp/B0FJ7L9NTM

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
