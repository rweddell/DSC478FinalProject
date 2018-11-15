
FROM python:3

ENV PYTHONBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV NAME MovieRecommender

ENV DISPLAY 0.0

CMD ["python", "Main.py"]
