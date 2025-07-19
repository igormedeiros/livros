# LangChain na Prática: O primeiro passo com Agentes de IA
# Autor: Igor Medeiros

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearchResults
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool

# Carregar variáveis de ambiente
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    print("Erro: A variável de ambiente GOOGLE_API_KEY não está definida.")
    print("Por favor, crie um arquivo .env na raiz do projeto com GOOGLE_API_KEY='SUA_CHAVE_AQUI'.")
    exit(1)

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
        return f"Item '{item}' com custo de R${custo:.2f} adicionado ao orçamento. Orçamento atual: {self.orcamento}"

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
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, google_api_key=google_api_key)

# --- Prompt do Agente ---
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente de planejamento de viagens. Use as ferramentas disponíveis para ajudar o usuário a planejar sua viagem, pesquisar informações e gerenciar o orçamento. Seja prestativo e informativo."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# --- Agente e Executor ---
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- Execução ---
if __name__ == "__main__":
    print("Assistente de Viagem pronto! Como posso ajudar a planejar sua próxima aventura?")

    perguntas = [
        "Qual o clima em Paris em agosto?",
        "Quais são as principais atrações turísticas em Roma?",
        "Adicione 'Passagem Aérea' com custo de 2500.00 ao orçamento.",
        "Adicione 'Hospedagem' com custo de 1200.00 ao orçamento.",
        "Qual o meu orçamento total até agora?",
        "Preciso de ideias para uma viagem de aventura na América do Sul.",
        "Qual o custo de um jantar em um restaurante médio em Tóquio?",
        "Qual o meu orçamento total?",
    ]

    for pergunta in perguntas:
        print(f"\n> Pergunta: {pergunta}")
        response = agent_executor.invoke({"input": pergunta})
        print(f"\n< Resposta Final: {response['output']}")
