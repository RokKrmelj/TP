from fastapi import FastAPI

app = FastAPI()

@app.post("/jsonapi")
async def create_item(a: int, b: int):
    return {"a: ":a, "b: ": b, "a + b: ": a + b}