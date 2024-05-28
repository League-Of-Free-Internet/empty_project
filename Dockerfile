FROM python:3.12

WORKDIR /app

COPY requirements/production.txt ./requirements/production.txt

RUN pip3 install --upgrade pip

RUN pip3 install -r ./requirements/production.txt --no-cache-dir

RUN apt-get update && apt-get install -y nano

COPY src .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
