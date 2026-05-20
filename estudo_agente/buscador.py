from langchain_chroma import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings

class Buscador:

    def __init__(self, pasta_banco: str, prompt_hyde: str) -> None:
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text")
        self.llm = ChatOllama(model="qwen2.5", temperature=0)
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