from pathlib import Path

from estudo_agente.agente import Agente
from estudo_agente.buscador import Buscador
from estudo_agente.indexador import Indexador

PASTA_DOCUMENTOS = "documentos/"
PASTA_BANCO = "chroma_db/"


def main() -> None:
    if not Path(PASTA_BANCO).exists():
        print("Indexando documentos...")
        indexador = Indexador(PASTA_DOCUMENTOS, PASTA_BANCO)
        indexador.indexar()
        print("Indexação concluída!")

    buscador = Buscador(
        pasta_banco=PASTA_BANCO,
        prompt_hyde=Buscador.carregar_prompt("prompts/hyde_prompt.txt"),
    )
    agente = Agente(buscador=buscador)
    agente.executar()


if __name__ == "__main__":
    main()