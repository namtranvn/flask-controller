
# FROM python:3.8-alpine
FROM python:3.10-buster
# FROM mcr.microsoft.com/devcontainers/python:3.10-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "controller.py"]
