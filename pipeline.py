import os
from pypdf import PdfReader

DOCS_DIR = "docs"
RAW_TEXT_DIR = "raw_text"

os.makedirs(RAW_TEXT_DIR, exist_ok=True)


def extract_pdf_text(pdf_path):
    text = ""

    reader = PdfReader(pdf_path)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def process_documents():

    pdf_files = [
        f for f in os.listdir(DOCS_DIR)
        if f.lower().endswith(".pdf")
    ]

    print(f"\nFound {len(pdf_files)} PDF documents\n")

    for pdf_file in pdf_files:

        pdf_path = os.path.join(DOCS_DIR, pdf_file)

        text = extract_pdf_text(pdf_path)

        txt_filename = os.path.splitext(pdf_file)[0] + ".txt"

        txt_path = os.path.join(RAW_TEXT_DIR, txt_filename)

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Saved: {txt_filename}")
#.....
    

def chunk_text(text, chunk_size=800, overlap=150):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]

        if len(chunk.strip()) > 0:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks

#....
def create_chunks():

    os.makedirs("chunks", exist_ok=True)

    total_chunks = 0

    txt_files = [
        f for f in os.listdir("raw_text")
        if f.endswith(".txt")
    ]

    for txt_file in txt_files:

        txt_path = os.path.join("raw_text", txt_file)

        with open(txt_path, "r", encoding="utf-8") as f:
            text = f.read()

        chunks = chunk_text(text)

        output_file = os.path.join(
            "chunks",
            txt_file.replace(".txt", "_chunks.txt")
        )

        with open(output_file, "w", encoding="utf-8") as out:

            for i, chunk in enumerate(chunks):

                out.write(f"\n=== CHUNK {i+1} ===\n")
                out.write(chunk)
                out.write("\n")

        print(f"{txt_file}: {len(chunks)} chunks")

        total_chunks += len(chunks)

    print(f"\nTotal chunks created: {total_chunks}")

if __name__ == "__main__":
    process_documents()
    create_chunks()
    