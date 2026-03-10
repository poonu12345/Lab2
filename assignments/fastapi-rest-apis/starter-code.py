# Starter code for the FastAPI REST APIs assignment

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

items = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app"}

# TODO: Add more endpoints for CRUD operations

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
