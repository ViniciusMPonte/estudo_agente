from estudo_agente.buscador import Buscador


def main():
    buscador = Buscador(
        pasta_banco="chroma_db/",
        prompt_hyde=Buscador.carregar_prompt("prompts/hyde_prompt.txt"),
    )

    print("🔍 Buscador de chunks — digite sua pergunta (ou 'sair' para encerrar)\n")

    while True:
        try:
            pergunta = input("Pergunta: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nEncerrando.")
            break

        if not pergunta:
            continue

        if pergunta.lower() in ("sair", "exit", "quit"):
            print("Encerrando.")
            break

        resultados = buscador.banco.similarity_search_with_relevance_scores(pergunta, k=3)

        if not resultados:
            print("Nenhum resultado encontrado.\n")
            continue

        for i, (doc, score) in enumerate(resultados):
            print(f"=== chunk {i + 1} | score: {score:.2f} ===")
            print(doc.page_content[:1000])
            print()


if __name__ == "__main__":
    main()
