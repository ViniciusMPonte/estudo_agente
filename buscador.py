from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

class Buscador:

    def __init__(self, pasta_banco: str) -> None:
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text")
        self.banco = Chroma(
            persist_directory=pasta_banco,
            embedding_function=self.embeddings,
        )

    def buscar(self, pergunta: str, quantidade: int = 3, threshold: float = 0.5) -> list:
        resultados = self.banco.similarity_search_with_relevance_scores(pergunta, k=quantidade)
        return [doc for doc, score in resultados if score >= threshold]