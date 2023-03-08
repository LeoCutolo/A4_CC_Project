FROM python:3.7-alpine

RUN apk --no-cache add --virtual .builddeps gcc gfortran musl-dev

WORKDIR /app

COPY requirements.txt .
COPY app.py ./src/
COPY templates/index.html ./src/templates/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "src/app.py"]