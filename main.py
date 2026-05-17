from pathlib import Path

from indexador import Indexador
from buscador import Buscador

PASTA_DOCUMENTOS = "documentos/"
PASTA_BANCO = "chroma_db/"


def main() -> None:
    if not Path(PASTA_BANCO).exists():
        print("Indexando documentos...")
        indexador = Indexador(PASTA_DOCUMENTOS, PASTA_BANCO)
        indexador.indexar()
        print("Indexação concluída!")

    buscador = Buscador(PASTA_BANCO)

    while True:
        pergunta = input("\nVocê: ").strip()
        if not pergunta:
            continue

        resultados = buscador.buscar(pergunta)
        for resultado in resultados:
            print(resultado.page_content)
            print("---")


if __name__ == "__main__":
    main()