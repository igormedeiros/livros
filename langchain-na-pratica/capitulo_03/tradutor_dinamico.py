

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
    modelo = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

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

