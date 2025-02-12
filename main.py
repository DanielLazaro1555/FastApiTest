from fastapi import FastAPI

from routers.product import router as product_router

app = FastAPI()

app.include_router(product_router)


@app.get("/")
def message():
    return "Hola mundo!"
