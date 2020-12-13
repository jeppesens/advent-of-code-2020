FROM python:3.8

COPY . /app
WORKDIR /app
COPY pyproject.toml ./

RUN pip install poetry
RUN poetry export -f requirements.txt -o requirements.txt --without-hashes

RUN pip install -r requirements.txt
RUN pip install debugpy

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

WORKDIR /app

CMD python main.py
