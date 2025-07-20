# capitulo_08/exercicio_3/main.py
import os, getpass
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Digite sua LangSmith API key: ")