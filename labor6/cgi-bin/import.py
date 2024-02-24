import json
import sqlite3

db = sqlite3.connect("fitness_gym.db")
cur = db.cursor()

file_in = "file_in_clients.json"

def read_json(file_name):
    with open(file_name,'r',encoding='utf-8') as file:
        return json.load(file)
    
dir_client = read_json(file_in)

for user in dir_client["Client"]:
    in_data = f"INSERT INTO Client (id,client_name,adress,phone_number,age) VALUES ('{user['id']}','{user['client_name']}','{user['adress']}','{user['phone_number']}','{user['age']}')"
    cur.execute(in_data)

db.commit()
db.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/index.html">')