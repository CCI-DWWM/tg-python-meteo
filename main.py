from typing import Union

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", description="Point d'API racine")
def read_root():
    """Cette fonction retourne juste un JSON"""
    return {"Hello": "World"}


@app.get("/items/{id}")
def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id, "maList": [
            '555', 'hhh', 'iii']}
    )

@app.get("/items2/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}