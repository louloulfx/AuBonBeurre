from flask import Flask
from flask import request
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import datetime
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config["DEBUG"] = True


def getDate(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.timestamp()


@app.route('/unites/all', methods=['GET'])
def get_all_unites():
    connection = mysql.connector.connect(host='185.224.137.214',
                                         database='u646551342_devops',
                                         user='u646551342_devops',
                                         password='devops')
    cursor = connection.cursor()
    try:
        sql = "SELECT * FROM `automates`"
        cursor.execute(sql)
        return (app.response_class(
            response=json.dumps(cursor.fetchall(), default=getDate),
            status=200,
            mimetype='application/json'
        ))
    finally:
        if cursor != None:
            cursor.close()
        if connection != None:
            connection.close()

    return (app.response_class(
            response=json.dumps({}, default=getDate),
            status=200,
            mimetype='application/json'
            ))


@app.route('/unites', methods=['GET'])
def get_one_unites():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    connection = mysql.connector.connect(host='185.224.137.214',
                                         database='u646551342_devops',
                                         user='u646551342_devops',
                                         password='devops')
    cursor = connection.cursor()

    try:
        query = "SELECT * FROM `automates` WHERE `nb_unite` = %s"
        cursor.execute(query, (id,))
        return (app.response_class(
            response=json.dumps(cursor.fetchall(), default=getDate),
            status=200,
            mimetype='application/json'
        ))
    finally:
        if cursor != None:
            cursor.close()
        if connection != None:
            connection.close()
    return (app.response_class(
        response=json.dumps({}, default=getDate),
        status=200,
        mimetype='application/json'
    ))


@app.route('/', methods=['GET'])
def home():
    return "<h1>Automates API</h1><p>You can have access to automates and unites data through this API.</p>"


if __name__ == '__main__':
    app.run()
