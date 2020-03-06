FROM python:3.7-alpine

WORKDIR /home/app

COPY ./*.py ./
COPY ./requirements.txt ./

RUN apk add --no-cache libressl-dev musl-dev libffi-dev
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev

RUN pip install -r requirements.txt
RUN pip install gunicorn

FROM ubuntu:16.04
# RUN apt-get update \
#         && apt-get install -y --no-install-recommends dialog \
#         && apt-get update \
# 	    && apt-get install -y --no-install-recommends openssh-server \
 
# RUN apt-get install -y msodbcsql17 mssql-tools


# apt-get and system utilities
RUN apt-get update && apt-get install -y \
    curl apt-utils apt-transport-https debconf-utils gcc build-essential g++-5 \
    && rm -rf /var/lib/apt/lists/*

# Install SQL Server drivers and tools
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && ACCEPT_EULA=Y apt-get install -y mssql-tools \
    && apt-get install -y unixodbc-dev libssl1.0.0 \
    && rm -rf /var/lib/apt/lists/*


ENV PATH="/opt/mssql-tools/bin:${PATH}"

ENV FLASK_APP app.py

EXPOSE 8000
#CMD ["python", "app.py", "--port", "8000"]
CMD ["gunicorn",  "--bind",  "0.0.0.0:8000",  "app:app"]
# docker run -p8000:8000 -e AZTENANTID=9885457a-2026-4e2c-a47e-32ff52ea0b8d -e AZAPPID=03da7a9b-63cd-4e42-9c26-9ffa4b4c65cb <image>