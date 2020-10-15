
FROM python:3.7-slim-buster
COPY ./webapp /webapp/
RUN pip install -r /webapp/requirements.txt
CMD cd /webapp && gunicorn --bind 0.0.0.0:$PORT wsgi
