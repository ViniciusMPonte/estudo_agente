from pathlib import Path

from agente import Agente
from indexador import Indexador

PASTA_DOCUMENTOS = "documentos/"
PASTA_BANCO = "chroma_db/"


def main() -> None:
    if not Path(PASTA_BANCO).exists():
        print("Indexando documentos...")
        indexador = Indexador(PASTA_DOCUMENTOS, PASTA_BANCO)
        indexador.indexar()
        print("Indexação concluída!")

    agente = Agente(PASTA_BANCO)
    agente.executar()


if __name__ == "__main__":
    main()