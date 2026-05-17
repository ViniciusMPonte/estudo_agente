from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

class Buscador:

    def __init__(self, pasta_banco: str) -> None:
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text")
        self.banco = Chroma(
            persist_directory=pasta_banco,
            embedding_function=self.embeddings,
        )

    def buscar(self, pergunta: str, quantidade: int = 3) -> list:
        return self.banco.similarity_search(pergunta, k=quantidade)