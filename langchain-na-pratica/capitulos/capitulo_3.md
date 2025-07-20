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

**Desafio Extra:**
- Adicione suporte para múltiplos idiomas e permita que o usuário escolha o idioma de resposta.
- Implemente um comando para o usuário alterar o tom das respostas (ex: formal, informal, humorístico).
- Permita que o usuário solicite resumos de textos, ajustando o número de pontos principais via prompt dinâmico.
- Salve o histórico de conversas em um arquivo local para análise posterior.
- Adicione validação para garantir que o idioma solicitado seja suportado e forneça feedback amigável em caso de erro.
- Implemente testes automatizados para as principais funções do chatbot, garantindo robustez e facilidade de manutenção.
- Crie um fluxograma simples do fluxo de interação do chatbot para facilitar o entendimento do projeto.
- Documente exemplos de uso, comandos disponíveis e dicas de troubleshooting no README do projeto.
- Explore a integração com APIs externas (ex: busca de notícias, previsão do tempo) usando ferramentas do LangChain.
- Adote boas práticas de segurança: nunca exiba a chave de API no console, use variáveis de ambiente e .env, e adicione .env ao .gitignore.
- Implemente logs e tracing para monitorar o uso e performance do chatbot.
- Adote versionamento para templates e configurações do projeto.

**Sugestão de Estrutura de Código:**
- `main.py`: lógica principal do chatbot.
- `utils.py`: funções auxiliares (validação de idioma, manipulação de histórico, etc).
- `config.py`: carregamento de variáveis de ambiente e configuração do modelo.
- `README.md`: instruções detalhadas de instalação, execução, exemplos e troubleshooting.
- `tests/`: testes automatizados para funções críticas.
- `prompts/`: pasta para templates reutilizáveis e versionados.
- `logs/`: pasta para armazenar logs e histórico de conversas.

**Exemplo de Fluxograma:**

```
[Usuário] --> [Chatbot]
    |           |
    |           |---> [Recebe comando ou pergunta]
    |           |---> [Identifica intenção: tradução, resumo, ajuste de tom]
    |           |---> [Formata prompt dinâmico]
    |           |---> [Invoca LLM via LCEL]
    |           |---> [Retorna resposta ao usuário]
    |           |---> [Salva histórico]
    |           |---> [Registra logs]
```

**Checklist para Entrega:**
- [ ] Chatbot funcional com LangChain, PromptTemplates e LCEL
- [ ] Tradução automática e ajuste de tom
- [ ] Resumo de textos com número de pontos configurável
- [ ] Histórico de conversas salvo localmente
- [ ] Comandos de execução documentados
- [ ] Chave de API protegida com .env
- [ ] Projeto compartilhado via GitHub (SSH)
- [ ] README completo com exemplos e troubleshooting
- [ ] Testes automatizados implementados
- [ ] Fluxograma do fluxo de interação
- [ ] Templates versionados e reutilizáveis
- [ ] Logs/tracing implementados

---
