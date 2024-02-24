import cgi
import html
import sqlite3

form = cgi.FieldStorage()

name = form.getfirst("fio")
num = form.getfirst("number")
adr = form.getfirst("adress")
age = form.getfirst("age")
if num:
    num = int(num)
if age:
    age = int(age)

db = sqlite3.connect("fitness_gym.db")
cur = db.cursor()
if(all((name,num,adr,age))):
    in_data = f"INSERT INTO Client (client_name, adress, phone_number, age) VALUES ('{name}','{adr}','{num}','{age}')"
    cur.execute(in_data)
    db.commit()

db.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/index.html">')