#!/bin/bash

# Se for a primeira execução, cria o ambiente virtual com uv
if [ ! -d ".venv" ]; then
    echo "Criando ambiente virtual..."
    uv venv
else
    echo "Ambiente virtual já existe."
fi

# Executa o script Python
# uv run --active exercicio_1/main.py
# uv run --active exercicio_2/main.py
# uv run --active exercicio_3/main.py
uv run --active exercicio_4/main.py
