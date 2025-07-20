# capitulo_07/exercicio_5/main.py
from typing_extensions import TypedDict

class KnowledgeTriple(TypedDict):
    subject: str
    predicate: str
    object: str

triples = [
    KnowledgeTriple(subject="João", predicate="gosta de", object="pizza"),
    KnowledgeTriple(subject="Maria", predicate="mora em", object="São Paulo"),
]
for triple in triples:
    print(f"{triple['subject']} {triple['predicate']} {triple['object']}")