FROM elejke/furniture_bot

RUN apk add 
RUN apk add build-base python3-dev jpeg-dev zlib-dev gcc libffi-dev openssl-dev

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD python bot.py
