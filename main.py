from pathlib import Path

from agente import Agente
from buscador import Buscador
from indexador import Indexador

PASTA_DOCUMENTOS = "documentos/"
PASTA_BANCO = "chroma_db/"


def main() -> None:
    if not Path(PASTA_BANCO).exists():
        print("Indexando documentos...")
        indexador = Indexador(PASTA_DOCUMENTOS, PASTA_BANCO)
        indexador.indexar()
        print("Indexação concluída!")

    buscador = Buscador(pasta_banco=PASTA_BANCO)
    agente = Agente(buscador=buscador)
    agente.executar()


if __name__ == "__main__":
    main()