## Capítulo 3: Manipulação de Prompts e Modelos de Linguagem com LangChain

### A Arte e a Ciência da Engenharia de Prompts

Se os modelos de linguagem são como gênios poderosos, os prompts são os nossos pedidos. A forma como fazemos o pedido — as palavras que usamos, a estrutura que damos, o contexto que fornecemos — determina drasticamente a qualidade da resposta que recebemos. Isso é o que chamamos de **Engenharia de Prompts**: a disciplina de projetar e otimizar as instruções dadas aos modelos de linguagem para obter os resultados desejados.

Não se trata de "adivinhar" as palavras mágicas. É uma disciplina que mistura criatividade, lógica e experimentação. Um bom prompt é claro, conciso e específico. Ele guia o modelo, em vez de deixá-lo vagando. O LangChain nos oferece ferramentas fantásticas para elevar nossa engenharia de prompts de simples strings para templates dinâmicos e reutilizáveis.

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

**Nota Pessoal:** Para alguns, um terminal de computador é uma tela preta, fria e sem vida. Para mim, quando estou no meu terminal Linux Kali com o shell Zsh todo customizado, me sinto como se estivesse prestes a tocar o solo de guitarra de "Hotel California" dos Eagles. Existe uma fluidez, uma arte, um prazer em fazer as ferramentas responderem exatamente como você quer, com o mínimo de esforço. É uma dança entre o homem e a máquina.

A engenharia de prompts é exatamente assim. Não é apenas sobre a técnica de encaixar variáveis em um template. É sobre encontrar o "feeling" certo, a combinação de palavras e estrutura que faz o modelo "cantar". É sobre a elegância de criar um prompt tão bem construído que a resposta do LLM parece mágica, mas na verdade é o resultado de um design cuidadoso.

Neste capítulo, vamos aprender a ser os guitarristas dos nossos LLMs. Vamos afinar nossos instrumentos (os templates) e aprender as escalas (as técnicas de prompt) para criar solos de informação que sejam precisos, criativos e impactantes.

### Integrando Modelos de Linguagem (LLMs)

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

### Exercício Prático: Um Tradutor Multilíngue Dinâmico

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

### Resumo do Capítulo

Neste capítulo, mergulhamos na arte e ciência da engenharia de prompts e como o LangChain nos ajuda a dominar essa habilidade.

* **Engenharia de Prompts:** Entendemos que a qualidade da nossa interação com um LLM depende diretamente da clareza e estrutura das nossas instruções (prompts).  
* **Templates de Prompt:** Vimos como os PromptTemplates do LangChain nos permitem criar prompts dinâmicos e reutilizáveis, evitando código repetitivo e tornando nossas aplicações mais modulares.  
* **Integração de LLMs:** Aprendemos a inicializar um LLM (especificamente o gemini-1.5-flash do Google) e a conectá-lo a um prompt template.  
* **Primeiro Vislumbre da LCEL:** Tivemos uma prévia da LangChain Expression Language (LCEL) e seu operador pipe (|), que cria um pipeline legível e elegante para conectar os componentes.  
* **Exercício Prático:** Construímos um tradutor multilíngue, solidificando o conhecimento de como usar variáveis dinâmicas em um prompt para criar uma aplicação flexível.



### Pontos Chave

*   A Engenharia de Prompts é crucial para obter respostas de qualidade dos LLMs.
*   `PromptTemplates` no LangChain permitem prompts dinâmicos e reutilizáveis.
*   LLMs são integrados e orquestrados eficientemente com o LangChain.
*   A LCEL simplifica a construção de pipelines, tornando-os mais legíveis e eficientes.
*   A prática com exercícios como o tradutor multilíngue solidifica o aprendizado dos conceitos de prompts e modelos.

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

*(Respostas: 1-b, 2-c, 3-c, 4-b, 5-d)*
