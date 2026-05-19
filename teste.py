from buscador import Buscador

PERGUNTA = "O que é o ProgressoFit plataforma web?"

buscador = Buscador("chroma_db/")
resultados = buscador.banco.similarity_search_with_relevance_scores(PERGUNTA, k=3)

for i, (doc, score) in enumerate(resultados):
    print(PERGUNTA + "\n\n")
    print(f"=== chunk {i+1} | score: {score:.2f} ===")
    print(doc.page_content[:1000])
    print()