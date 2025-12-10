import random
from datetime import datetime, timedelta

from models import Book, Student


def random_date():
    """Соңғы 30 күн ішіндегі кездейсоқ уақыт."""
    days_ago = random.randint(0, 30)
    random_time = timedelta(
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59),
    )
    return datetime.now() - timedelta(days=days_ago) + random_time


def get_sample_data():
    """Студенттер мен кітаптардың бастапқы дайын тізімі."""
    books = [
        Book("Python негіздері", "Г. Әбілқайыр", "Бағдарламалау"),
        Book("Машина үйрену", "Т. Ермеков", "Жасанды интеллект"),
        Book("Математикалық талдау", "С. Жұмабаев", "Математика"),
        Book("Философия тарихы", "Қ. Әбдірахманов", "Гуманитарлық"),
        Book("Деректер қоры", "А. Сейтқұлов", "Ақпараттық технология"),
        Book("Web технологиялар", "М. Қасым", "Бағдарламалау"),
        Book("Биоинформатика", "Ж. Айсұлу", "Биология"),
        Book("Тіл мәдениеті", "Р. Дәуренбек", "Филология"),
    ]

    students = [
        Student("Айдос Ермек", "Ақпараттық технологиялар", 2),
        Student("Жанар Омар", "Филология", 3),
        Student("Ринат Марат", "Математика", 1),
        Student("Диана Бекзат", "Гуманитарлық ғылымдар", 4),
        Student("Самат Жолдас", "Биология", 2),
        Student("Әлия Серік", "Информатика", 3),
        Student("Мұрат Алмас", "Экономика", 2),
        Student("Аяжан Рүстем", "Философия", 1),
    ]

    for student in students:
        borrowed = random.sample(books, random.randint(2, 5))

        for book in borrowed:
            borrow_time = random_date()
            student.borrow_book(book, borrow_time)

            if random.choice([True, False]):
                return_time = borrow_time + timedelta(
                    days=random.randint(1, 10)
                )
                student.return_book(book, return_time)

    return students
