FROM python:3.10-slim

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN apt update; apt install -y git
RUN pip install -r requirements.txt
RUN apt remove -y git

WORKDIR /code
COPY ./app ./app
COPY run.py .

#COPY movies.db .
#COPY README.md .
#ENV NO_RATE_LIMIT="TRUE"
#ENV REDIS_HOST="redis"
#CMD uvicorn --host 0.0.0.0 --port 80 run:app --workers 4
