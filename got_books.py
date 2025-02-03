import json
import requests


def get_books_after_year(url: str, year: int):
    response = requests.get(url)
    if response.status_code == 200:
        books_data = json.loads(response.text)
        for book in books_data:
            published_year = int(book['released'][:4])
            if published_year > year:
                print(f"Book: {book['name']}")
                print(f"Published: {book['released']}")
                print("_" * 20)



if __name__ == '__main__':
    year = int(input("Enter a year: "))
    url = "https://anapioficeandfire.com/api/books"
    get_books_after_year(url, year)