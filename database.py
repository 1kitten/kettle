import datetime
import sqlite3 as sq


def log_into_data_base(date: datetime.datetime, message: str):
    """
    Функция для создания базы данных.
    Выполняет SQL запрос по добавлению нового
    сообщения в таблицу logs.
    :param date: (datetime) дата добавления сообщения в таблицу
    :param message: (str) сообщение.
    """
    with sq.connect('kettle.db') as conn:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS logs (
            date TEXT,
            message TEXT
            )
            """
        )

        cur.execute("""
        INSERT INTO logs (date, message)
        VALUES (?, ?);
        """, (date, message))
