import sqlite3


def create_tables():
    connection = sqlite3.connect('management_system.db')
    cursor = connection.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        student_number TEXT,
                        course TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS lecturers (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        employee_id TEXT,
                        department TEXT)''')
    connection.commit()
    connection.close()


# Call create_tables() to create the necessary tables when the application starts
# create_tables()
def read_table():
    connection = sqlite3.connect('management_system.db')

    cursor = connection.execute("SELECT * from lecturers")
    rows = cursor.fetchall()
    for row in rows:
        print(rows)
    connection.close()

# def insert_data(n, sn, c):
#     connection = sqlite3.connect('management_system.db')
#     cursor = connection.cursor()
#
#     cursor.execute("INSERT INTO lecturers VALUES (Null, ?, ?, ?)", (n, sn, c))
#     connection.commit()


def delete_data():
    connection = sqlite3.connect("management_system.db")
    cursor = connection.execute("DELETE FROM lecturers WHERE id=3")
    connection.commit()


def updateTable(n, sn, c, id):
    connection = sqlite3.connect("management_system.db")
    cursor = connection.execute("UPDATE lecturers SET name=?, employee_id=?,"
                                " department=? WHERE id=?", (n, sn, c, id))
    connection.commit()

# insert_data("Armand", "123", "Diploma")
# delete_data()
# updateTable("Piet", "122", "Bachelor", "2")
read_table()
