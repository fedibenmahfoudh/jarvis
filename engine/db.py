import sqlite3

#crete jarvis.db file jus run the command
conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

""" query = "INSERT INTO sys_command VALUES (null,'brave', 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave')"
cursor.execute(query)
conn.commit() """

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'chat gpt', 'https://chatgpt.com/')"
cursor.execute(query)
conn.commit()


