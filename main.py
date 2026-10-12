from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return  {"message": "Hola Mundo"}

@app.get("/products")
def get_products(limit: int = 10):
    return {"products": [], "limit": limit}

@app.get("/products/{product_id}")
def get_product(product_id: int, include_desc: bool = False):
    return {"id": product_id, "include_dec": include_desc}