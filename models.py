from datetime import datetime
from abc import ABC, abstractmethod

class Person(ABC):
    """Адамдар үшін базалық абстрактілі класс"""
    def __init__(self, name, faculty):
        self._name = name
        self._faculty = faculty

    @abstractmethod
    def info(self):
        pass

    def __str__(self):
        return f"{self._name} ({self._faculty})"


class Book:
    """Кітап туралы ақпарат"""
    def __init__(self, title, author, genre):
        self.__title = title
        self.__author = author
        self.__genre = genre

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def genre(self):
        return self.__genre

    def __str__(self):
        return f"{self.__title} ({self.__author}, {self.__genre})"

    def __eq__(self, other):
        return isinstance(other, Book) and self.__title == other.__title and self.__author == other.__author

    def __hash__(self):
        return hash((self.__title, self.__author))


class Student(Person):
    """Студент классы (Person-нан мұрагерлік алған)"""
    def __init__(self, name, faculty, year):
        super().__init__(name, faculty)
        self.__year = year
        self.__borrowed_books = []  # (Book, borrow_time, return_time)

    def borrow_book(self, book: Book, borrow_time: datetime):
        """Кітап алу"""
        self.__borrowed_books.append((book, borrow_time, None))

    def return_book(self, book: Book, return_time: datetime):
        """Кітап қайтару"""
        for i, (b, borrow_time, r_time) in enumerate(self.__borrowed_books):
            if b == book and r_time is None:
                self.__borrowed_books[i] = (b, borrow_time, return_time)
                break

    def get_borrowed_books(self):
        return self.__borrowed_books

    @property
    def year(self):
        return self.__year

    def info(self):
        return f"{self._name} ({self._faculty}, {self.__year}-курс)"

    def __len__(self):
        """Студенттің алған кітаптарының санын қайтарады"""
        return len(self.__borrowed_books)
