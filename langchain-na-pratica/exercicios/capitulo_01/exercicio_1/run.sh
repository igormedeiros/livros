#!/bin/bash

# Se for a primeira execução, cria o ambiente virtual com uv
if [ ! -d ".venv" ]; then
    echo "Criando ambiente virtual..."
    uv create .venv
else
    echo "Ambiente virtual já existe."
fi

# Ativa o ambiente virtual
source .venv/bin/activate

# Instala as dependências do projeto
echo "Instalando dependências..."
uv sync

# Executa o script Python
uv run main.py