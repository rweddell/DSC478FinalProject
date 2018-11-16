
FROM python:3

ENV PYTHONBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV NAME MovieRecommender

CMD ["python", "Main.py"]
