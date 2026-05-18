from langchain_chroma import Chroma
from langchain_core.tools import tool
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain.agents import create_agent


class Agente:

    def __init__(self, pasta_banco: str) -> None:
        self.llm = ChatOllama(model="llama3.2", temperature=0)
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text")
        self.banco = Chroma(
            persist_directory=pasta_banco,
            embedding_function=self.embeddings,
        )

    def criar_ferramentas(self) -> list:
        retriever = self.banco.as_retriever(search_kwargs={"k": 3})

        @tool
        def buscar_documentos(query: str) -> str:
            """Busca informações nos documentos locais. Use para responder perguntas sobre o conteúdo dos arquivos."""
            docs = retriever.invoke(query)
            return "\n\n".join([doc.page_content for doc in docs])

        return [buscar_documentos]

    def executar(self) -> None:
        ferramentas = self.criar_ferramentas()
        agente = create_agent(
            self.llm,
            tools=ferramentas,
            system_prompt="Você é um assistente útil. Sempre use a ferramenta buscar_documentos antes de responder qualquer pergunta.",
        )

        while True:
            pergunta = input("\nVocê: ").strip()
            if not pergunta:
                continue

            resultado = agente.invoke({
                "messages": [{"role": "user", "content": pergunta}]
            })

            for msg in resultado["messages"]:
                print(f"[{msg.type}]: {msg.content[:200]}")

            # resposta = resultado["messages"][-1].content
            # print(f"\nAgente: {resposta}")