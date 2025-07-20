# capitulo_07/exercicio_2/main.py
from langchain.experimental.generative_agents import GenerativeAgent, GenerativeAgentMemory
from datetime import datetime, timedelta

memory = GenerativeAgentMemory(reflection_threshold=8)
agent = GenerativeAgent(
    name="Tommie",
    age=25,
    traits="ansioso, gosta de design, comunicativo",
    status="procurando emprego",
    memory=memory,
)

observations = [
    "Tommie lembra do cachorro Bruno de infância",
    "Tommie está cansado após dirigir",
    "Viu a nova casa",
    "Os vizinhos têm um gato",
    "A rua é barulhenta à noite",
    "Tommie está com fome",
    "Tommie tenta descansar."
]
for obs in observations:
    agent.memory.add_memory(obs)

print(agent.get_summary(force_refresh=True))