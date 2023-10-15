FROM python:3.10.13

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 5000
EXPOSE 5432

RUN apt-get update && apt-get install -y make && pip install poetry

COPY . .

RUN make install

CMD ["make", "start"]