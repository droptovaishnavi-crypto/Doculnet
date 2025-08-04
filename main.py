from fastapi import FastAPI
from pydantic import BaseModel
from utils.query_engine import process_query

app = FastAPI()

class RequestData(BaseModel):
    query: str
    document: str

@app.post("/hackrx/run")
async def run_query(data: RequestData):
    result = process_query(data.query, data.document)
    return {"answer": result}
