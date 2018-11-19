
FROM python:3

ENV PYTHONBUFFERED 1

COPY . /app

WORKDIR /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV NAME MovieRecommender

CMD ["python", "./Main2.py"]
