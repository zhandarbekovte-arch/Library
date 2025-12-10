import random
from datetime import timedelta
import requests

from models import Book
from utils import get_sample_data, random_date


OPEN_LIBRARY_URL = (
    "https://openlibrary.org/subjects/programming.json?limit=20"
)


def fetch_books():
    """
    Open Library API арқылы кітаптарды алу.
    Егер API жұмыс істемесе — фейк деректер қолданылады.
    """
    try:
        response = requests.get(OPEN_LIBRARY_URL, timeout=5)
        response.raise_for_status()

        data = response.json()
        books = []

        for item in data.get("works", []):
            title = item.get("title", "Белгісіз атау")
            authors = item.get("authors", [])
            author_name = authors[0]["name"] if authors else "Белгісіз автор"
            genre = "Бағдарламалау"

            books.append(Book(title, author_name, genre))
        return books

    except Exception as exc:
        print(f"API қате: {exc}. Фейк деректер қолданылады.")

        books_set = set()
        for student in get_sample_data():
            for book, _, _ in student.get_borrowed_books():
                books_set.add(book)

        return list(books_set)


def fetch_students():
    """Студенттерді алу және кездейсоқ Open Library кітаптарын қосу."""
    students = get_sample_data()
    books = fetch_books()

    for student in students:
        extra_books = random.sample(books, random.randint(1, 2))

        for book in extra_books:
            borrow_time = random_date()
            student.borrow_book(book, borrow_time)

            if random.choice([True, False]):
                return_time = borrow_time + timedelta(
                    days=random.randint(1, 10)
                )
                student.return_book(book, return_time)

    return students
