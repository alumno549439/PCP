from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

lista_items = []

class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default = None, examples=["A ver si funciona"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])


@app.get("/stock")
def mostrar_items():
    return {"Listado Objetos: " + lista_items}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    lista_items.append({"item_id: ": item_id, "item: ": item})
    return item

@app.delete("/delete/{item_id}")
def eliminar_items():
    return {}

# @app.get("/categoria/{cat}")
# def articulos_por_categoria(cat:str = "General"):
#     return

# @app.put("/libro")
# def crear_libro(Libro:Book):
#     libro_nuevo = Libro.model_dump()
#     libro_nuevo["id"] = max(lib['id'] for lib in inventario) + 1 if inventario else 1   # Comprensión en Python.
#     inventario.append(libro_nuevo)
#     return {"Añadido el libro: ": libro_nuevo}

# @app.post("/almacen/{id_libro}")