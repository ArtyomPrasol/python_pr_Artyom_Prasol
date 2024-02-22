import sqlite3
from http.server import HTTPServer, CGIHTTPRequestHandler
import cgitb

cgitb.enable() 

# db = sqlite3.connect("fitness_gym.db")
# cursor = db.cursor()

#Ввод таблиц
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Client(
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                client_name TEXT NOT NULL,
#                adress TEXT NOT NULL,
#                phone_number INTEGER NOT NULL,
#                age INTEGER NOT NULL
# )
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Subscription(
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                name TEXT NOT NULL,
#                price INTEGER NOT NULL,
#                num_days INTEGER
# )
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Saled_subs(
#                id_card INTEGER PRIMARY KEY AUTOINCREMENT,
#                id_client INTEGER,
#                id_sub INTEGER,
#                date_start DATE NOT NULL,
#                date_end DATE NOT NULL,
#                FOREIGN KEY (id_client)  REFERENCES Client (id),
#                FOREIGN KEY (id_sub)  REFERENCES Subscription (id)
# )
# """)

# cursor.execute("ALTER TABLE Client ADD age INTEGER NOT NULL")

#Ввод строк в таблицы
# cursor.execute("INSERT INTO Client (client_name, adress, phone_number, age) VALUES ('Ваня','ул. Пашковская',891834567,23),('Дима','ул. Кировская',12315125612,29),('Саша','ул. Зиповская',89005553535,21)")
# cursor.execute("INSERT INTO Subscription (name, price, num_days) VALUES ('Недельный', 1500, 7), ('Месяц', 4000, 30), ('Годовой', 8000, 365)")
# cursor.execute("INSERT INTO Saled_subs (id_client, id_sub, date_start, date_end) VALUES (1,1,'2024-02-18', '2024-02-25'), (2,1,'2024-02-11', '2024-02-18'), (3,2,'2024-02-05','2024-03-06')")

#db.commit()

#Выбор между 3мя запросами
# var = int(input("Введите 1-3 для выбора запроса: "))
# match(var):
#     case 1:
#         ce = cursor.execute("""
# SELECT Client.id, Client.client_name FROM Client
#                         JOIN Saled_subs on Client.id = Saled_subs.id_client
#                         WHERE Saled_subs.Date_end>=DATE()
# """)
#         print(ce.fetchall())
#     case 2:
#         ce = cursor.execute("""
# SELECT SUM(price) FROM Subscription
#                         JOIN Saled_subs ON Subscription.id = Saled_subs.id_sub
#                         WHERE Saled_subs.Date_end>=DATE()   
# """)
#         print(ce.fetchall()[0][0])
#     case 3:
#         ce = cursor.execute("""
# SELECT id_card, date_end FROM Saled_subs
#                         WHERE Date_end<=DATE()
# """)
#         print(ce.fetchall())
#     case _:
#         print("Запрос не был выбран!")

# db.close()

server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()