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

# 3.2: Reescrevemos o arquivo de repositórios para o modo SEGURO, forcando a verificacao com a chave que acabamos de baixar.
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
