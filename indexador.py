from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter


class Indexador:

    def __init__(self, pasta_documentos: str, pasta_banco: str) -> None:
        self.pasta_documentos = Path(pasta_documentos)
        self.pasta_banco = pasta_banco
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text")

    def carregar_documentos(self) -> list:
        loader = DirectoryLoader(
            str(self.pasta_documentos),
            glob="*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"},
        )
        return loader.load()

    def dividir_chunks(self, documentos: list) -> list:
        header_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "titulo"),
                ("##", "secao"),
                ("###", "subsecao"),
            ],
            strip_headers=False,
        )

        char_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
        )

        chunks = []
        for doc in documentos:
            secoes = header_splitter.split_text(doc.page_content)
            for secao in secoes:
                secao.metadata.update(doc.metadata)
            chunks.extend(char_splitter.split_documents(secoes))

        return chunks

    def indexar(self) -> None:
        documentos = self.carregar_documentos()
        chunks = self.dividir_chunks(documentos)
        Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.pasta_banco,
        )