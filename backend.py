# backend.pyfrom fastapi import FastAPI
from pydantic import BaseModel
import requests
import PyPDF2
import io
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import openai

# Load embedding model (lightweight SBERT)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Setup FastAPI
app = FastAPI()

# Your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"   # <-- replace

# Request model
class QueryRequest(BaseModel):
    query: str
    document: str   # PDF URL

@app.post("/hackrx/run")
def run_query(req: QueryRequest):
    # Step 1: Download the PDF
    try:
        pdf_response = requests.get(req.document)
        pdf_response.raise_for_status()
    except Exception as e:
        return {"error": f"Failed to download PDF: {e}"}

    # Step 2: Extract text
    pdf_text = ""
    with io.BytesIO(pdf_response.content) as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            pdf_text += page.extract_text() + "\n"

    if not pdf_text.strip():
        return {"error": "Could not extract text from PDF."}

    # Step 3: Chunk text
    chunks = [pdf_text[i:i+500] for i in range(0, len(pdf_text), 500)]

    # Step 4: Embed chunks
    embeddings = embedder.encode(chunks, convert_to_numpy=True)

    # Step 5: Search relevant chunks using FAISS
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    query_embedding = embedder.encode([req.query], convert_to_numpy=True)
    D, I = index.search(query_embedding, k=3)  # top 3 chunks
    context = "\n".join([chunks[i] for i in I[0]])

    # Step 6: Ask LLM with context
    prompt = f"""
    You are an insurance assistant. Answer the question using the following policy text only.

    Policy text:
    {context}

    Question: {req.query}
    """

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = completion.choices[0].message["content"]
    except Exception as e:
        answer = f"Error calling LLM: {e}"

    return {
        "query": req.query,
        "document": req.document,
        "answer": answer.strip()
    }
