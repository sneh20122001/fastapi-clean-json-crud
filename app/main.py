from fastapi import FastAPI
from app.api.item_router import router

app = FastAPI(title="Item Management API", version="1.0")

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Item Management API!"}