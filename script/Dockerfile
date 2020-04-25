FROM python:3.7

WORKDIR /app
RUN pip install mysql-connector-python
RUN mkdir /app/jsonFiles
RUN apt-get update \
    && apt-get install -y \
        nmap \
        nano
COPY server.py .
COPY generate.py .

CMD ["python", "./server.py"]