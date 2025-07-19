import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearchResults
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool

# Carregar variáveis de ambiente
load_dotenv()

# --- Ferramentas ---

# Ferramenta de busca na internet
search_tool = TavilySearchResults(
    max_results=3,
    description="Uma ferramenta de busca para encontrar informações na internet sobre destinos de viagem, clima, atrações, etc."
)

# Ferramenta customizada para gerenciar orçamento de viagem (simulado em memória)
class OrcamentoViagem:
    def __init__(self):
        self.orcamento = {}

    @tool
    def adicionar_item_orcamento(self, item: str, custo: float) -> str:
        """
        Adiciona um item e seu custo ao orçamento de viagem.
        Útil para planejar gastos.
        Exemplo: adicionar_item_orcamento("Passagem Aérea", 1500.00)
        """
        self.orcamento[item] = self.orcamento.get(item, 0.0) + custo
        return f"Item '{item}' com custo de R${costo:.2f} adicionado ao orçamento. Orçamento atual: {self.orcamento}"

    @tool
    def ver_orcamento_total(self) -> str:
        """
        Retorna o total do orçamento de viagem e a lista de itens.
        """
        total = sum(self.orcamento.values())
        if not self.orcamento:
            return "O orçamento de viagem está vazio."
        return f"Orçamento total: R${total:.2f}. Itens: {self.orcamento}"

orcamento_viagem = OrcamentoViagem()

tools = [search_tool, orcamento_viagem.adicionar_item_orcamento, orcamento_viagem.ver_orcamento_total]

# --- LLM ---
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# --- Prompt do Agente ---
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente de viagem inteligente. Use as ferramentas disponíveis para ajudar o usuário a planejar sua viagem e gerenciar o orçamento."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# --- Criar e Executar o Agente ---
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

if __name__ == "__main__":
    print("Assistente de Viagem Inteligente pronto! Como posso ajudar?")

    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            break

        try:
            response = agent_executor.invoke({"input": user_input})
            print(f"Assistente: {response['output']}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    print("Assistente de Viagem encerrado.")