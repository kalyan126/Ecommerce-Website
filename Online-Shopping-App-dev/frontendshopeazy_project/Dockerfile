FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
COPY ./requirements.txt /app/requirements.txt # we are copying the requirements file
RUN pip install -r requirements.txt
COPY . /app
