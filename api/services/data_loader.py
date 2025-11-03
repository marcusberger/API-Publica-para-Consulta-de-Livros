import pandas as pd

def load_books():
    df = pd.read_csv("data/books.csv")
    df["id"] = df.index
    return df