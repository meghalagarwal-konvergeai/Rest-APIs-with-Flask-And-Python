import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table = "CREATE TABLE USERS (id int, username text, password text)"
cursor.execute(create_table)

user = (1, "jose", "asdf")
insert_query = "INSERT INTO USERS VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, "rolf", "asdf"),
    (3, "anne", "xyz")
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM USERS"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()