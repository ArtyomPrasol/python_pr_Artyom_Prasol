import json
import sqlite3

def write_json(data, file_name):
    data = json.dumps(data, ensure_ascii=False)
    data = json.loads(str(data))

    with open(file_name, 'w', encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False, indent=4)

db = sqlite3.connect("fitness_gym.db")
cur = db.cursor()

data = (cur.execute("SELECT * FROM Client")).fetchall()

file_out = "file_out_clients.json"

data_client={"Client":[]}

for user in data:
    user_dist = {}
    user_dist["id"] = user[0]
    user_dist["client_name"] = user[1]
    user_dist["adress"] = user[2]
    user_dist["phone_number"] = user[3]
    user_dist["age"] = user[4]
    data_client["Client"].append(user_dist)

write_json(data_client,file_out)

db.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/index.html">')