from flask import Flask
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import datetime
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config["DEBUG"] = True


def converter(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.timestamp()


def makeResponse(data):
    response = app.response_class(
        response=json.dumps(data, default=converter),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/unites', methods=['GET'])
def get_unites():
    connection = mysql.connector.connect(host='185.224.137.214',
                                         database='u646551342_devops',
                                         user='u646551342_devops',
                                         password='devops')
    cursor = connection.cursor()
    try:
            sql = "SELECT * FROM `automates`"
            cursor.execute(sql)
            return makeResponse(cursor.fetchall())
    finally:
        if cursor != None:
            cursor.close()
        if connection != None:
            connection.close()

    return makeResponse({})


@app.route('/', methods=['GET'])
def home():
    return "<h1>Automates API</h1><p>You can have access to automates and unites data through this API.</p>"


if __name__ == '__main__':
    app.run()
