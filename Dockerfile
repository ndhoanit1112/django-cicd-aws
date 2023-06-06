# For more information, please refer to https://aka.ms/vscode-docker-python
FROM --platform=linux/amd64 python:3.8-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt-get update
# RUN sudo apt-get install mysql-server
RUN apt-get install -y libcurl4-openssl-dev libssl-dev
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

EXPOSE 8000

RUN mkdir -p /var/run/gunicorn
VOLUME gunicorn:/var/run/gunicorn

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD gunicorn --bind=unix:/var/run/gunicorn/gunicorn.sock app.wsgi --workers=4
