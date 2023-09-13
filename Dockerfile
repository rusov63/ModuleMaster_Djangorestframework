FROM python:3.11-alpine3.18
#Debian GNU/Linux 10, python без компилятора

WORKDIR /service
#старт команды manage.py из директории

COPY ./requirements.txt /service/

EXPOSE 8080

RUN pip install -r /service/requirements.txt

COPY . .