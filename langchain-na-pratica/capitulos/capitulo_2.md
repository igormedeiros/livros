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