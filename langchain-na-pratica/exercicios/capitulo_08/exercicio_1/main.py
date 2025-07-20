# capitulo_08/exercicio_1/main.py
import pytest
from langchain_core.output_parsers import StrOutputParser

def test_str_output_parser():
    parser = StrOutputParser()
    output = parser.invoke({"content": "Olá, mundo!"})
    assert output == "Olá, mundo!"