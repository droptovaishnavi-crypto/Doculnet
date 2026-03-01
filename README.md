<div align="center">

# 🚀 DOCULNET  

### Transforming Static Documents into Intelligent Conversations  

</div>



---

## 🧠 The Problem  

Searching inside long PDFs is frustrating.  
Keyword matching fails to understand meaning.  
Context is lost. Time is wasted.  

Documents store information —  
but they don’t understand you.



---

## 💡 The Vision  

Doculnet reimagines how we interact with documents.  

Instead of scrolling and searching,  
you simply **ask**.  

Instead of matching words,  
the system understands **intent**.  

Doculnet turns static documents into dynamic knowledge systems.



---

## ⚙️ Tech Stack  

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)  
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi)  
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-black?style=for-the-badge&logo=openai)  
![Pinecone](https://img.shields.io/badge/Pinecone-VectorDB-purple?style=for-the-badge)  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)  

</div>



---

## 🏗️ Architecture  

1. 📄 Document ingestion  
2. ✂ Intelligent text chunking  
3. 🧬 Embedding generation  
4. 🗄 Vector storage (Pinecone)  
5. 🔎 Semantic retrieval  
6. 🤖 LLM-powered answer generation  

Built using Retrieval-Augmented Generation (RAG).



---

## ✨ Key Highlights  

- 🔍 Context-aware semantic search  
- 🤖 LLM-driven response generation  
- ⚡ FastAPI-based backend architecture  
- 🧩 Modular and scalable design  
- 🚀 Ready for production scaling  



---

## 🎯 Use Cases  

- Insurance Policy Q&A  
- Legal Document Assistance  
- Enterprise Knowledge Retrieval  
- Academic Research Support  
---

## 🏗️ System Architecture  

```
          User Query
               │
               ▼
        FastAPI Backend
               │
               ▼
      Text Chunk Retrieval
               │
               ▼
        Pinecone Vector DB
               │
               ▼
   Relevant Context Retrieved
               │
               ▼
        OpenAI GPT Model
               │
               ▼
          Final Answer
```

Doculnet follows a Retrieval-Augmented Generation (RAG) pipeline,  
where semantic retrieval enhances LLM-based response generation.



---

## 🚀 API Usage  

### 🔹 Start the Server

```bash
uvicorn app:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

### 🔹 Example Query (POST Request)

```bash
curl -X POST "http://127.0.0.1:8000/query" \
-H "Content-Type: application/json" \
-d '{"question": "What are the policy coverage details?"}'
```

---

### 🔹 Example JSON Request

```json
{
  "question": "Explain the claim process in this document."
}
```

---

### 🔹 Example JSON Response

```json
{
  "answer": "The claim process involves submitting required documents, verification by the insurer, and final approval based on policy terms."
}
```

---

## 🔐 Environment Variables  

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
DATABASE_URL=your_postgres_url
```

---
👩‍💻 Built By  

**Vaishnavi Devi R**  
AI & Data Science Student  
Passionate about building intelligent AI systems that solve real-world problems.  

