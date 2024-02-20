import sqlite3

db = sqlite3.connect("fitness_gym.db")
cursor = db.cursor()

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

# cursor.execute("""
# INSERT INTO Client (client_name, adress, phone_number, age) VALUES ('Ваня','ул. Пашковская',891834567,23),('Дима','ул. Кировская',12315125612,29),('Саша','ул. Зиповская',89005553535,21)      
# """)
# cursor.execute("""
# INSERT INTO Subscription (name, price, num_days) VALUES ('Недельный', 1500, 7), ('Месяц', 4000, 30), ('Годовой', 8000, 365)     
# """)

em = db.execute("SELECT * FROM Client")
print(em.fetchall())
db.commit()

db.close()