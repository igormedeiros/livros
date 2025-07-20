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
