import streamlit as st
import pandas as pd
from stats import LibraryStatistics
from api_client import fetch_students

st.set_page_config(page_title="📚 Университет кітапханасы", layout="wide")
st.title("📊 Университет кітапханасында студенттердің кітап алу статистикасы")

# Мәліметтерді API арқылы алу (Open Library + фейк студенттер)
students = fetch_students()

# Sidebar фильтр
faculties = sorted({s._faculty for s in students})
selected_faculty = st.sidebar.selectbox("Факультет таңдау", ["Барлығы"] + faculties)

years = sorted({s.year for s in students})
selected_year = st.sidebar.selectbox("Курс таңдау", ["Барлығы"] + years)

# Фильтр қолдану
filtered_students = students
if selected_faculty != "Барлығы":
    filtered_students = [s for s in filtered_students if s._faculty == selected_faculty]
if selected_year != "Барлығы":
    filtered_students = [s for s in filtered_students if s.year == selected_year]

# DataFrame жасау
data = []
for s in filtered_students:
    for book, borrow_time, return_time in s.get_borrowed_books():
        data.append({
            "Студент": s.info(),
            "Кітап": book.title,
            "Автор": book.author,
            "Жанр": book.genre,
            "Алу уақыты": borrow_time.strftime("%Y-%m-%d"),
            "Қайтару уақыты": return_time.strftime("%Y-%m-%d") if return_time else "-"
        })

df = pd.DataFrame(data)

if df.empty:
    st.warning("Мәлімет жоқ")
else:
    st.dataframe(df, use_container_width=True)

# Фильтр қолданылған студенттерге сәйкес статистика
stats = LibraryStatistics(filtered_students)
summary = stats.summary()

st.markdown(f"**Жалпы алынған кітап саны:** {summary['total_books']}")
st.markdown(f"**Ең көп алынған жанр:** {summary['popular_genre'] or 'Мәлімет жоқ'}")

# Визуализация
if not df.empty:
    st.subheader("📈 Жанр бойынша кітап саны")
    st.bar_chart(df['Жанр'].value_counts())

    st.subheader("📊 Студенттер бойынша кітап саны")
    st.bar_chart(df['Студент'].value_counts())

    st.subheader("📅 Күн бойынша кітап алу тренді")
    trend_df = pd.DataFrame(list(summary['daily_trend'].items()), columns=['Күн', 'Кітап саны'])
    trend_df = trend_df.set_index('Күн')
    st.line_chart(trend_df)
