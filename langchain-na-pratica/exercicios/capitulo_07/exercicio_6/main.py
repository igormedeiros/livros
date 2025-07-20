# capitulo_07/exercicio_6/main.py
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

model = ChatOpenAI(temperature=0)

@tool
def registrar_feedback(feedback: str) -> str:
    """Registra feedback do usuário na memória."""
    return f"Feedback registrado: {feedback}"

tools = [registrar_feedback]
prompt = ChatPromptTemplate.from_messages([
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent = create_tool_calling_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory)

print(agent_executor.invoke({"input": "Preciso de ajuda com minha conta."}))
print(agent_executor.invoke({"input": "O atendimento foi ótimo!"}))
print(agent_executor.invoke({"input": "Qual foi meu feedback anterior?"}))