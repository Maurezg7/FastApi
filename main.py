from fastapi import FastAPI, HTTPException
from routers.products import router as products_router
from routers.llm import router as products_router

app = FastAPI()
app.include_router(products_router)

@app.get("/")
def home():
    return  {"message": "Hola Mundo"}

