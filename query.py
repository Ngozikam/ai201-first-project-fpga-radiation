import os
import chromadb

from groq import Groq
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

# ---------------------------
# Load Groq API Key
# ---------------------------

client_groq = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------------------
# Load Embedding Model
# ---------------------------

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# ---------------------------
# Load ChromaDB
# ---------------------------

client_db = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client_db.get_collection(
    "fpga_radiation_rag"
)


def retrieve_context(question, top_k=5):

    query_embedding = model.encode(
        question
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    context = ""

    sources = []

    for i in range(
        len(results["documents"][0])
    ):

        doc = results["documents"][0][i]

        source = results["metadatas"][0][i]["source"]

        context += f"\nSOURCE: {source}\n"
        context += doc
        context += "\n\n"

        if source not in sources:
            sources.append(source)

    return context, sources


def ask(question):

    context, sources = retrieve_context(
        question
    )

    prompt = f"""
Answer the question using ONLY the FPGA radiation documents below.

If the documents do not contain enough information,
reply exactly:

I do not have enough information in the loaded FPGA-radiation documents to answer that.

Do not use outside knowledge.
Do not guess.

DOCUMENTS:

{context}

QUESTION:

{question}
"""

    response = client_groq.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )

    answer = response.choices[0].message.content

    return {
        "answer": answer,
        "sources": sources
    }


if __name__ == "__main__":

    result = ask(
        "What is a Single Event Upset in an FPGA?"
    )

    print("\n" + "=" * 60)
    print("ANSWER")
    print("=" * 60)

    print(result["answer"])

    print("\n" + "=" * 60)
    print("SOURCES USED")
    print("=" * 60)

    for i, source in enumerate(
        result["sources"],
        start=1
    ):
        print(f"{i}. {source}")