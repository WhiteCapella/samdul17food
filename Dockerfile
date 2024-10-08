FROM python:3.11

WORKDIR /code

COPY src/samdul17food/main.py /code/

RUN pip install --no-cache-dir --upgrade git+https://github.com/WhiteCapella/samdul17food.git@0.1.4

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
