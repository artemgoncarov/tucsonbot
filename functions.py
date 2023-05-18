import sqlite3


def read_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('db.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from storage_users"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        for row in records:
            print("user_id:", row[0])
            print("dostup", row[1])
            print("date_of_dostup:", row[2])
            print("rank:", row[3], end="\n\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# read_sqlite_table()

def isInDB(id):
    sqlite_connection = sqlite3.connect('db.db')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from storage_users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    ids = []
    for row in records:
        ids.append(int(row[0]))
    if id in ids:
        return True
    else:
        return False


def find_id(id):
    sqlite_connection = sqlite3.connect('db.db')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from storage_users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    ids = []
    dostups = []
    for row in records:
        ids.append(int(row[0]))
        dostups.append(row[1])
    i = ids.index(id)

    return int(dostups[i])

def load_data(user_id, dostup, date_of_dostup, rank):
    sqlite_connection = sqlite3.connect('db.db')
    cursor = sqlite_connection.cursor()
    # print("Подключен к SQLite")

    sqlite_insert_with_param = """INSERT INTO storage_users
                          (user_id, dostup, date_of_dostup, rank)
                          VALUES
                          (?, ?, ?, ?);"""
    data_tuple = (user_id, dostup, date_of_dostup, rank)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    sqlite_connection.commit()
    # print("Переменные Python успешно вставлены в таблицу sqlitedb_developers")

    cursor.close()
