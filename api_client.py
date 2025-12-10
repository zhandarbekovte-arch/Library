import requests
from datetime import datetime
from models import Book, Student
from utils import get_sample_data
import random

# Open Library API URL (мысалы, бағдарламалау тақырыбы бойынша кітаптар)
OPEN_LIBRARY_URL = "https://openlibrary.org/subjects/programming.json?limit=20"

def fetch_books():
    """
    Open Library API арқылы кітаптарды алу.
    Егер API қол жетімсіз болса, локальды фейк деректер қолданылады.
    """
    try:
        response = requests.get(OPEN_LIBRARY_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        books = []
        for item in data.get('works', []):
            title = item.get('title', "Белгісіз атау")
            authors = item.get('authors', [])
            author_name = authors[0]['name'] if authors else "Белгісіз автор"
            genre = "Бағдарламалау"  # Open Library API нақты жанр бермейді
            books.append(Book(title, author_name, genre))
        return books
    except Exception as e:
        print(f"API қате: {e}. Фейк деректер қолданылады.")
        # Фейк деректер
        sample_students = get_sample_data()
        books = set()
        for s in sample_students:
            for b, _, _ in s.get_borrowed_books():
                books.add(b)
        return list(books)


def fetch_students():
    """
    Студенттерді алу және Open Library кітаптарын кездейсоқ қосу.
    """
    students = get_sample_data()
    books = fetch_books()
    # Әр студентке кездейсоқ 1-2 Open Library кітаптарын қосу
    for student in students:
        extra_books = random.sample(books, random.randint(1, 2))
        for book in extra_books:
            from utils import random_date
            borrow_time = random_date()
            student.borrow_book(book, borrow_time)
            if random.choice([True, False]):
                from datetime import timedelta
                return_time = borrow_time + timedelta(days=random.randint(1, 10))
                student.return_book(book, return_time)
    return students
