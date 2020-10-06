FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

ADD . /test_zinobe
WORKDIR /test_zinobe

RUN pip install --upgrade pip

COPY requirements.txt /test_zinobe/
RUN pip install -r requirements.txt
COPY . /test_zinobe/