from fastapi import FastAPI
from pydantic import BaseModel

var = 0

app = FastAPI()

class Item(BaseModel):
    temp: int

@app.put("/put/")
async def create_item(item: Item):
    global var
    var = item.temp
    return {"Globalna spremenljivka": item.temp,}

@app.get("/save GET/")
async def get():
    global var
    return var

