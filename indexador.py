from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

class Indexador:

    def __init__(self, pasta_documentos: str, pasta_banco: str) -> None:
        self.pasta_documentos = Path(pasta_documentos)
        self.pasta_banco = pasta_banco
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text")

    def carregar_documentos(self) -> list:
        loader = DirectoryLoader(
            str(self.pasta_documentos),
            glob="*.txt",
            loader_cls=TextLoader,
        )
        return loader.load()

    def dividir_chunks(self, documentos: list) -> list:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150,
        )
        return splitter.split_documents(documentos)

    def indexar(self) -> None:
        documentos = self.carregar_documentos()
        chunks = self.dividir_chunks(documentos)
        Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.pasta_banco,
        )

