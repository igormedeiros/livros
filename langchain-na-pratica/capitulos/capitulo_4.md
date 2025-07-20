## Capítulo 4: Construção de Pipelines: Da SequentialChain à LCEL

### A Evolução das Chains: Do Imperativo ao Declarativo

Nos primeiros dias do LangChain, a forma de construir fluxos de trabalho era através de classes como LLMChain e SequentialChain. Essa abordagem, embora funcional, era o que chamamos de **imperativa**: você instanciava objetos e os conectava de forma mais verbosa, o que tornava o código mais difícil de ler e manter. Era como dar instruções passo a passo para montar um móvel, detalhando cada parafuso.

O time do LangChain percebeu que poderia haver uma maneira melhor, mais intuitiva e mais poderosa. Uma maneira que fosse **declarativa**, onde você simplesmente descreve o fluxo de dados — como um diagrama de montagem — e o framework se encarrega da execução otimizada.

Essa percepção deu origem à **LangChain Expression Language (LCEL)**, lançada em agosto de 2023\. A LCEL é, sem dúvida, uma das inovações mais importantes do framework e é a maneira moderna e recomendada de construir qualquer tipo de pipeline.

Neste capítulo, vamos fazer uma viagem no tempo. Primeiro, vamos construir uma chain "à moda antiga" para entender as dores que a LCEL veio resolver. Depois, vamos mergulhar de cabeça na LCEL e ver como ela torna nossa vida muito mais fácil.

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


### A Revolução da LCEL: Por que Devemos Usá-la?

A LCEL não é apenas uma "sintaxe mais bonita"; ela é uma **linguagem declarativa para compor Runnables**, destravando funcionalidades cruciais de forma quase automática e transformando o LangChain de uma ferramenta de prototipagem para uma ferramenta pronta para produção.

* **Streaming Nativo:** Obtenha respostas do modelo token a token com o método .stream(). Isso melhora drasticamente a experiência do usuário em aplicações de chat, que não precisa mais esperar a resposta completa.  
* **Suporte Assíncrono Garantido:** Qualquer chain LCEL pode ser executada de forma não-bloqueante com .ainvoke(). Isso é essencial para servidores web que precisam lidar com múltiplas requisições simultaneamente.  
* **Execução Paralela Otimizada:** A LCEL pode executar múltiplos componentes ao mesmo tempo para otimizar a latência, simplesmente definindo um dicionário de Runnables.  
* **Integração Total com LangSmith:** Tenha rastreabilidade completa de cada passo do seu pipeline, facilitando o debug e a observabilidade, algo que era muito mais complexo com as chains antigas.  
* **Interface Unificada (Runnable):** Quase tudo no LangChain moderno implementa a interface Runnable. Isso significa que prompts, modelos, parsers e até funções Python podem ser encadeados da mesma forma, usando o operador pipe (|), tornando o código mais limpo, legível e modular.

### LCEL na Prática: Exercícios Essenciais

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
```

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
**Comando de Execução (Windows):**

```bat
REM Execute o exercício no Windows
exercicios\capitulo_04\exercicio_6\run.bat
```

Falando em combinar coisas que parecem não combinar, vou contar uma pequena curiosidade sobre mim: eu adoro o ambiente de cafeterias para trabalhar. Aquele burburinho de fundo, a energia das pessoas ao redor... tudo isso me ajuda a focar de uma maneira que o silêncio do escritório em casa não consegue. A ironia? Eu não sou fã de café. Sou o cara estranho em um canto, com uma xícara de chá de camomila, programando freneticamente.

Essa minha peculiaridade me rendeu o apelido de "cliente diferentão" em algumas cafeterias. Mas, assim como a LCEL nos mostra que a combinação de elementos aparentemente díspares pode gerar resultados poderosos e harmoniosos, minha xícara de chá em meio a um mar de expressos é a prova de que a produtividade pode vir de onde menos se espera.

Às vezes, em LangChain, vamos combinar componentes de maneiras inesperadas, como fizemos com a RunnableParallel. Podemos achar que executar tarefas em paralelo pode criar confusão, mas, na verdade, quando orquestrado corretamente, o resultado é surpreendentemente eficiente e harmonioso. É como a minha produtividade movida a chá em meio a um mar de expressos: funciona, e funciona muito bem.

### Checklist de Construção de Pipelines

* [ ] Definir claramente o objetivo do pipeline e as etapas necessárias para alcançá-lo.  
* [ ] Usar a sintaxe LCEL (|) para compor Runnables (prompts, modelos, parsers, funções).  
* [ ] Garantir a passagem correta de dados entre as etapas, usando dicionários e RunnablePassthrough quando necessário.  
* [ ] Utilizar RunnableParallel para otimizar a latência executando tarefas independentes ao mesmo tempo.  
* [ ] Integrar lógica customizada usando RunnableLambda quando necessário.  
* [ ] Implementar streaming (.stream()) para melhorar a experiência do usuário em aplicações interativas.  
* [ ] Incluir monitoramento e logging (idealmente com LangSmith) para acompanhar a execução e identificar falhas.  
* [ ] Testar o pipeline com diferentes entradas para validar a robustez e a eficiência.  
* [ ] Documentar o fluxo e as dependências para facilitar a manutenção futura.





### Pontos Chave
*   A LCEL é a forma moderna e recomendada de construir pipelines no LangChain, oferecendo streaming, suporte assíncrono e execução paralela nativamente.
*   `RunnablePassthrough`, `RunnableParallel`, e `RunnableLambda` são componentes chave para construir pipelines flexíveis e eficientes.
*   A transição de abordagens imperativas para declarativas (LCEL) simplifica o código e melhora a performance.

### Teste seu Conhecimento

1. Qual era a principal desvantagem da abordagem clássica com SequentialChain?  
   a) Não era possível conectar mais de duas chains.  
   b) Era verbosa e exigia a definição manual de input_variables e output_variables.  
   c) Não funcionava com modelos de chat.  
   d) Era mais rápida que a LCEL.  
2. Qual dos seguintes é um benefício fundamental da LCEL que não estava facilmente disponível nas chains clássicas?  
   a) A capacidade de usar prompts.  
   b) Suporte nativo para streaming, batch e execução assíncrona.  
   c) A capacidade de usar modelos do Google.  
   d) A necessidade de definir output_key.  
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