from buscador import Buscador

buscador = Buscador("chroma_db/")
resultados = buscador.banco.similarity_search_with_relevance_scores("O que é o ProgressoFit plataforma web?", k=3)

for i, (doc, score) in enumerate(resultados):
    print(f"=== chunk {i+1} | score: {score:.2f} ===")
    print(doc.page_content[:300])
    print()