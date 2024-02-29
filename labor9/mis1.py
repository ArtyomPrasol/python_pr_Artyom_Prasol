import pandas as pd

def time_to_seconds(time_str):
    mas_time = []
    for time in time_str:
        minutes, seconds = map(int, time.replace(' мин.', '').replace(' сек.', '').split())
        mas_time.append(minutes * 60 + seconds)
    
    return pd.Series(mas_time)

data = pd.read_csv("11 - 1.csv")
score = "7,00"
time_task = 540
result = data[(data.get("Оценка/10,00", "") == score)].reset_index()
result = result[time_to_seconds(result.get("Затраченное время",""))>time_task]
print(len(result))
print(result.sort_values(by='Фамилия'))