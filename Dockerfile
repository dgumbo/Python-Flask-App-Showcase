FROM python:3.7-alpine

WORKDIR /home/app

COPY ./*.py ./
COPY ./requirements.txt ./

RUN apk add --no-cache libressl-dev musl-dev libffi-dev
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev

RUN apk add msodbcsql17 mssql-tools
RUN install msodbcsql17 mssql-tools
RUN apt install msodbcsql17 mssql-tools
RUN apt-get install msodbcsql17 mssql-tools
RUN sudo apt-get install msodbcsql17 mssql-tools

RUN pip install -r requirements.txt
RUN pip install gunicorn

ENV FLASK_APP app.py

EXPOSE 8000
#CMD ["python", "app.py", "--port", "8000"]
CMD ["gunicorn",  "--bind",  "0.0.0.0:8000",  "app:app"]
# docker run -p8000:8000 -e AZTENANTID=9885457a-2026-4e2c-a47e-32ff52ea0b8d -e AZAPPID=03da7a9b-63cd-4e42-9c26-9ffa4b4c65cb <image>