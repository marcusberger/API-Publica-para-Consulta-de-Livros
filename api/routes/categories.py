from fastapi import APIRouter
from api.services.data_loader import load_books

router = APIRouter()
df = load_books()

@router.get("/categories", response_model=list[str])
def get_categories():
    return sorted(df["category"].unique().tolist())