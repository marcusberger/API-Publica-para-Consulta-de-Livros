from fastapi import FastAPI
from api.routes import books, categories

app = FastAPI(title="Book API", version="1.0")

app.include_router(books.router, prefix="/api/v1")
app.include_router(categories.router, prefix="/api/v1")

@app.get("/api/v1/health")
def health_check():
    return {"status": "ok"}