from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime
import pickle

app = FastAPI()

# CORS 설정 추가
origins = [
    "https://samdul17food.web.app"  # 허용할 출처 (Firebase 호스팅 URL)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "n17"}

@app.get("/food")
def food(name: str):
    # 시간을 구함
    # 음식 이름과 시간을 csv 로 저장 -> /code/data/food.csv

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {"food": name, "time": current_time}
