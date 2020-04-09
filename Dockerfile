FROM python:3.8-alpine

RUN apk add build-base python3-dev jpeg-dev zlib-dev

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD python bot.py
