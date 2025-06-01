"""
MCP Demo: Minimal Model Context Protocol Example (FastAPI Mock Version)
This script demonstrates a simple model server using FastAPI to simulate MCP behavior.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# Define a simple model
class AddInput(BaseModel):
    a: int
    b: int

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the MCP FastAPI demo! Visit /docs for API documentation."}

@app.post("/v1/models/adder/predict")
async def predict(inputs: AddInput):
    result = inputs.a + inputs.b
    return {"sum": result}

if __name__ == "__main__":
    print("Starting FastAPI MCP demo server on http://localhost:8000 ...")
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)

"""
How to use this demo:
1. Install the required packages:
   pip install fastapi uvicorn pydantic
2. Run this script:
   python mcp_demo.py
3. Send a POST request to http://localhost:8000/v1/models/adder/predict with JSON body:
   {"a": 2, "b": 3}
   You should get a response: {"sum": 5}
"""
