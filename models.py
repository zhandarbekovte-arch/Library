from datetime import datetime
from abc import ABC, abstractmethod


class Person(ABC):
    """Адамдар үшін базалық абстрактілі класс."""

    def __init__(self, name, faculty):
        self._name = name
        self._faculty = faculty

    @abstractmethod
    def info(self):
        """Студент/адам туралы ақпарат."""
        raise NotImplementedError

    def __str__(self):
        return f"{self._name} ({self._faculty})"


class Book:
    """Кітап туралы ақпарат."""

    def __init__(self, title, author, genre):
        self._title = title
        self._author = author
        self._genre = genre

    @property
    def title(self):
        return my._title

    @property
    def author(self):
        return self._author

    @property
    def genre(self):
        return self._genre

    def __str__(self):
        return f"{self._title} ({self._author}, {self._genre})"

    def __eq__(self, other):
        return (
            isinstance(other, Book)
            and self._title == other._title
            and self._author == other._author
        )

    def __hash__(self):
        return hash((self._title, self._author))


class Student(Person):
    """Студент класы."""

    def __init__(self, name, faculty, year):
        super().__init__(name, faculty)
        self._year = year
        self._borrowed_books = []

    def borrow_book(self, book, borrow_time: datetime):
        """Кітап алу."""
        self._borrowed_books.append((book, borrow_time, None))

    def return_book(self, book, return_time):
        """Алынған кітапты қайтару."""
        for index, (b, borrow_time, r_time) in enumerate(
            self._borrowed_books
        ):
            if b == book and r_time is None:
                self._borrowed_books[index] = (
                    b,
                    borrow_time,
                    return_time,
                )
                break

    def get_borrowed_books(self):
        return self._borrowed_books

    @property
    def year(self):
        return self._year

    def info(self):
        return f"{self._name} ({self._faculty}, {self._year}-курс)"

    def __len__(self):
        return len(self._borrowed_books)
