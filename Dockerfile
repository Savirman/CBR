FROM python:3.10.6-slim-buster
LABEL "author"="Dmitry Dolgov"
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=wsgi.py
WORKDIR /app
RUN pip3 install flask
RUN pip3 install urllib3
RUN pip3 install datetime
RUN pip3 install psycopg2-binary
COPY . /app
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
