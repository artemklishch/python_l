import sqlite3

DB_NAME = "sqlite_db.db"

# Create database file
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     print(sqlite_conn)
#     print(sqlite3.version)

#  create new table
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#     );"""
#     sqlite_conn.execute(sql_request)

#  Add records
# courses = [
#     (351, "JavaScript course", 23, 10),
#     (31, "C++ course", 13, 20),
#     (1, "Java course", 3, 12),
# ]
#
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?,?,?,?)"
#     # sqlite_conn.execute(sql_request, (12, "Python course", 100, 30))
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit()

# Read records
with sqlite3.connect(DB_NAME) as sqlite_conn:
    # sql_request = "SELECT * FROM courses"
    # sql_cursor = sqlite_conn.execute(sql_request)
    # # for record in sql_cursor:
    # #     print(record)  # tuple
    #
    # records = sql_cursor.fetchall()
    # print(records)
    sql_request = "SELECT * FROM courses WHERE reviews_qty>=15"
    sql_cursor = sqlite_conn.execute(sql_request)
    records = sql_cursor.fetchall()
    print(records)
