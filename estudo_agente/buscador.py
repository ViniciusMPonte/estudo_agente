import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import OllamaEmbeddings

load_dotenv()
API_KEY: str = os.getenv('API_KEY')

llm_model: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=API_KEY
)


class Buscador:

    def __init__(self, pasta_banco: str, prompt_hyde: str) -> None:
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text")
        self.llm = llm_model
        self.prompt_hyde = prompt_hyde
        self.banco = Chroma(
            persist_directory=pasta_banco,
            embedding_function=self.embeddings,
        )

    @staticmethod
    def carregar_prompt(caminho: str) -> str:
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read().strip()

    def _gerar_documento_hipotetico(self, pergunta: str) -> str:
        prompt = self.prompt_hyde.format(pergunta=pergunta)
        resposta = self.llm.invoke(prompt)
        return resposta.content

    def buscar(self, pergunta: str, quantidade: int = 3, threshold: float = 0.2) -> list:
        documento_hipotetico = self._gerar_documento_hipotetico(pergunta)
        resultados = self.banco.similarity_search_with_relevance_scores(
            documento_hipotetico,
            k=quantidade,
        )
        return [doc for doc, score in resultados if score >= threshold]
