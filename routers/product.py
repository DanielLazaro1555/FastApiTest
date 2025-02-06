from fastapi import APIRouter, Path, Query
from models.product import Product

router = APIRouter()

# Lista de productos corregida (separados con coma)
products = [
    {
        "id": 1,
        "name": "product 1",
        "price": 20,
        "stock": 10
    },
    {
        "id": 2,
        "name": "product 2",
        "price": 30,
        "stock": 5
    }
]


@router.get("/products")
def get_all_products():
    return products


@router.get("/products/{id}")
def get_product(id: int = Path(gt=0)):
    return list(filter(lambda item: item["id"] == id, products))


@router.get('/products/')
def get_products_by_stock(stock: int, price: float = Query(gt=0)):
    return list(filter(lambda item: item["stock"] == stock and item['price'] == price, products))


@router.post("/products")
def create_product(product: Product):
    products.routerend(product)
    return products


@router.put('/products/{id}')
def update_product(id: int, product: Product):
    for index, item in enumerate(products):
        if item['id'] == id:
            # Convertimos el modelo a diccionario
            products[index] = product.dict()
            return product  # Devolvemos el producto actualizado


@router.delete('/products/{id}')
def delete_product(id: int):
    for item in products:
        if item['id'] == id:
            products.remove(item)
    return products
