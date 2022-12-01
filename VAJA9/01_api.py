from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/api/")
async def read_item(a: int, b: int):
    return {"a: ":a, "b: ": b, "a + b: ": a + b}
