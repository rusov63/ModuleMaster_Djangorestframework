FROM python:3.11

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
# Python не использовать буферизацию ввода-вывода и не создавать
# скомпилированные файлы для ускорения запуска.

RUN pip install --upgrade pip
# обновляет pip до последней версии.

WORKDIR /app
#старт команды manage.py из директории

COPY ./requirements.txt /app/

EXPOSE 8000

RUN pip install -r /app/requirements.txt

COPY . .