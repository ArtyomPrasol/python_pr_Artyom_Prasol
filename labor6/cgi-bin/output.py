import cgi
import sqlite3

db = sqlite3.connect("fitness_gym.db")
cur = db.cursor()

def get_r(query):
    cur.execute(query)
    rows = cur.fetchall()
    rows = list(map(make_r, rows))
    return "\n".join(rows)

def make_r(row):
    row = list(map(lambda value: f"<td>{value}</td>", row))
    row = "\n".join(row)
    return "<tr>\n" + row + "\n</tr>"

guests = get_r("SELECT * FROM Client")

print("Content-type: text/html; charset='utf-8'\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print(f"""
            <h3>Гость</h3>
            <table>
            <thead>
                <tr>
                <td>ID</td>
                <td>ФИО</td>
                <td>Адрес</td>
                <td>Номер телефона</td>
                <td>Возраст</td>
                </tr>
            </thead>
            <tbody>
                {guests}
            </tbody>
            </table><br>
        """)

print("<a href='/index.html'> Обратно </a>")

print("""</body>
        </html>""")

db.close()