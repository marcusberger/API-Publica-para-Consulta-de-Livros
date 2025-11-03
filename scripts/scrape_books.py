import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://books.toscrape.com/"
BOOKS = []

def get_rating(text):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(text, 0)

def scrape_book_data(book, category):
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text.strip().lstrip("£")
    availability = book.select_one(".availability").text.strip()
    rating = get_rating(book.p["class"][-1])
    image_url = BASE_URL + book.img["src"].replace("../", "")
    return {
        "title": title,
        "price": float(price),
        "availability": availability,
        "rating": rating,
        "category": category,
        "image_url": image_url
    }

def scrape_category(category_url, category_name):
    page_url = category_url
    while True:
        res = requests.get(page_url)
        soup = BeautifulSoup(res.content, "html.parser")
        books = soup.select("article.product_pod")
        for book in books:
            BOOKS.append(scrape_book_data(book, category_name))
        next_btn = soup.select_one("li.next > a")
        if next_btn:
            page_url = category_url.replace("index.html", "") + next_btn["href"]
        else:
            break

def scrape_all_books():
    print("Iniciando scraping...")
    res = requests.get(BASE_URL + "index.html")
    soup = BeautifulSoup(res.content, "html.parser")
    categories = soup.select(".side_categories ul li ul li a")
    for cat in categories:
        category_name = cat.text.strip()
        category_url = BASE_URL + cat["href"]
        print(f"Scraping categoria: {category_name}")
        scrape_category(category_url, category_name)
        time.sleep(1)  # evita sobrecarga no servidor

    df = pd.DataFrame(BOOKS)
    df.to_csv("data/books.csv", index=False)
    print(f"Scraping finalizado. {len(BOOKS)} livros salvos em data/books.csv")

if __name__ == "__main__":
    scrape_all_books()
