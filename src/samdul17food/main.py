from typing import Union
from fastapi import FastAPI
import datetime
import pickle

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "n17"}

@app.get("/food")
def food(name: str):
    # 시간을 구함
    # 음식 이름과 시간을 csv 로 저장 -> /code/data/food.csv

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('/code/data/food.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name, current_time])

    return {"food": name, "time": current_time}
