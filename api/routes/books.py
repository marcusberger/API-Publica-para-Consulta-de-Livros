from fastapi import APIRouter, Query
from api.models.book import Book
from api.services.data_loader import load_books

router = APIRouter()
df = load_books()

@router.get("/books", response_model=list[Book])
def get_books():
    return df.to_dict(orient="records")

@router.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = df[df["id"] == book_id]
    if book.empty:
        return {"error": "Livro não encontrado"}
    return book.iloc[0].to_dict()

@router.get("/books/search", response_model=list[Book])
def search_books(title: str = Query(None), category: str = Query(None)):
    result = df
    if title:
        result = result[result["title"].str.contains(title, case=False)]
    if category:
        result = result[result["category"].str.contains(category, case=False)]
    return result.to_dict(orient="records")