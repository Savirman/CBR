FROM python:slim-buster
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN pip3 install flask
RUN pip3 install urllib3
RUN pip3 install datetime
RUN pip3 install psycopg2-binary
COPY . /app
EXPOSE 5000
ENTRYPOINT python wsgi.py runserver 0.0.0.0:5000
