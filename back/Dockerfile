FROM python:3.7

WORKDIR /app
RUN pip install mysql-connector-python
RUN pip install flask
RUN pip install flask_cors

COPY backend.py .

CMD ["python", "backend.py"]