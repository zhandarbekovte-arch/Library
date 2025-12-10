from collections import Counter

class LibraryStatistics:
    """Кітапхана статистикасы"""

    def __init__(self, students):
        self.students = students or []

    def total_borrowed_books(self):
        """Барлық студенттердің кітаптарын санау"""
        return sum(len(s) for s in self.students)

    def most_popular_genre(self):
        """Ең көп алынған жанр"""
        genres = [book.genre for s in self.students for book, _, _ in s.get_borrowed_books()]
        return max(set(genres), key=genres.count) if genres else None

    def daily_trend(self):
        """Күн бойынша кітап алу саны"""
        from datetime import datetime
        dates = []
        for s in self.students:
            for _, borrow_time, _ in s.get_borrowed_books():
                dates.append(borrow_time.date())
        counter = Counter(dates)
        sorted_dates = sorted(counter.items())
        return dict(sorted_dates)

    def summary(self):
        return {
            "total_books": self.total_borrowed_books(),
            "popular_genre": self.most_popular_genre(),
            "daily_trend": self.daily_trend()
        }
