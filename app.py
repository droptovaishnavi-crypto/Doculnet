# app.py (Streamlit frontend)
import streamlit as st
import requests

# Backend API URL (FastAPI must be running)
API_URL = "http://127.0.0.1:8000/hackrx/run"

st.set_page_config(page_title="DocuIntel - Insurance Query System", layout="centered")

st.title("🔍 DocuIntel: Intelligent Policy Query System")

# User inputs
query = st.text_area("Enter your query", "Does this policy cover knee surgery?")
document_url = st.text_input(
    "Enter Document URL",
    "https://hackrx.blob.core.windows.net/assets/hackrx_6/policies/ICIHLIP22012V012223.pdf"
)

if st.button("Ask"):
    payload = {"query": query, "document": document_url}

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success("✅ Answer:")
            st.json(result)   # pretty print JSON
        else:
            st.error(f"❌ Error: {response.status_code} - {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("⚠️ Could not connect to backend. Make sure FastAPI is running!")
