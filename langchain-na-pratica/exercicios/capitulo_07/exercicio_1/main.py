# capitulo_07/exercicio_1/main.py
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage

model = ChatOpenAI(temperature=0)

@tool
def get_user_age(name: str) -> str:
    """Retorna a idade do usuário (exemplo didático)."""
    if "bob" in name.lower():
        return "42 anos"
    return "41 anos"

tools = [get_user_age]
prompt = ChatPromptTemplate.from_messages([
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent = create_tool_calling_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory)

# Primeira interação
print(agent_executor.invoke({"input": "Oi! Meu nome é Bob, qual minha idade?"}))
# Segunda interação (memória)
print(agent_executor.invoke({"input": "Você lembra meu nome?"}))