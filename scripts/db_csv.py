import chromadb
import csv

client = chromadb.PersistentClient(path="chroma_db")
colecao = client.list_collections()[0]
dados = colecao.get(include=["documents", "metadatas"])

with open("chunks.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "texto", "metadados"])
    for id_, doc, meta in zip(dados["ids"], dados["documents"], dados["metadatas"]):
        writer.writerow([id_, doc, meta])