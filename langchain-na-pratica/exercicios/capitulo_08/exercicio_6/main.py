# capitulo_08/exercicio_6/main.py
import pytest
from capitulo_08.exercicio_5.main import chain

def test_filme_desconhecido():
    resposta = chain.invoke({"filme": "FilmeInexistente"})
    assert "Desculpe" in resposta.content or resposta.content == ""