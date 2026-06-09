import os
import chromadb
from sentence_transformers import SentenceTransformer

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Creating ChromaDB client...")
client = chromadb.PersistentClient(path="chroma_db")

# Clear old collection so duplicate IDs do not cause problems when rerunning
try:
    client.delete_collection(name="fpga_radiation_rag")
except Exception:
    pass

collection = client.get_or_create_collection(
    name="fpga_radiation_rag"
)

chunk_count = 0

for chunk_file in os.listdir("chunks"):
    if not chunk_file.endswith(".txt"):
        continue

    source_name = chunk_file.replace("_chunks.txt", "")
    file_path = os.path.join("chunks", chunk_file)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    chunks = content.split("=== CHUNK")

    for i, chunk in enumerate(chunks):
        chunk = chunk.strip()

        if len(chunk) < 50:
            continue

        embedding = model.encode(chunk).tolist()

        collection.add(
            ids=[f"{source_name}_{i}"],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[
                {
                    "source": source_name,
                    "chunk_id": i
                }
            ]
        )

        chunk_count += 1

print(f"\nStored {chunk_count} chunks in ChromaDB")


def retrieve_chunks(query, top_k=5):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    print("\nQUERY:")
    print(query)

    print("\nTOP RESULTS:\n")

    for i in range(len(results["documents"][0])):
        doc = results["documents"][0][i]
        source = results["metadatas"][0][i]["source"]
        distance = results["distances"][0][i]

        print(f"Result {i+1}")
        print(f"Source: {source}")
        print(f"Distance: {distance:.4f}")
        print(doc[:500])
        print("\n" + "=" * 60 + "\n")


retrieve_chunks(
    "What is a Single Event Upset in an FPGA?"
)

retrieve_chunks(
    "What is Triple Modular Redundancy and how does it improve reliability?"
)

retrieve_chunks(
    "What is the function of the Xilinx Soft Error Mitigation core?"
)