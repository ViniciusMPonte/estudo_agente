import os
import sys

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

from estudo_agente.buscador import Buscador

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()
API_KEY: str = os.getenv('API_KEY')

llm_model: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=API_KEY
)


class Agente:

    def __init__(self, buscador: Buscador) -> None:
        self.buscador = buscador
        self.llm = llm_model
        self.system_prompt = self._carregar_system_prompt("prompts/system_prompt.txt")

    @staticmethod
    def _carregar_system_prompt(caminho: str) -> str:
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read().strip()

    def criar_ferramentas(self) -> list:

        @tool
        def buscar_documentos(query: str) -> str:
            """Busca informações nos documentos locais. Use SEMPRE que o usuário fizer qualquer pergunta. As informações retornadas são a fonte principal de conhecimento."""
            docs = self.buscador.buscar(query, quantidade=5)
            return "\n\n".join([doc.page_content for doc in docs])

        return [buscar_documentos]

    def executar(self) -> None:
        ferramentas = self.criar_ferramentas()
        agente = create_agent(
            self.llm,
            tools=ferramentas,
            system_prompt=self.system_prompt,
        )

        print("🤖 Agente ProgressoFit — digite sua pergunta (ou 'sair' para encerrar)\n")

        while True:
            try:
                pergunta = input("\nVocê: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nEncerrando.")
                break

            if not pergunta:
                continue

            if pergunta.lower() in ("sair", "exit", "quit"):
                print("Encerrando.")
                break

            resultado = agente.invoke({
                "messages": [{"role": "user", "content": pergunta}]
            })

            resposta = resultado["messages"][-1].content
            print(f"\nAgente: {resposta}")
