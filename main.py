import sqlite3

import requests
from flask import Flask, json

DB_NAME = 'db.sqlite3'
TABLE_NAME = 'api_post'

app = Flask(__name__)
connection = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = connection.cursor()


@app.route('/')
def index():
    res = requests.get('http://127.0.0.1:8000/posts/')
    # print(type(json.loads(res.content.decode(encoding='utf-8'))))

    statement = f"INSERT INTO {TABLE_NAME}(title,body,owner) values (?,?,?)"
    # cursor.execute(statement, ('sgf', 'eswgw', 'sweg'))
    connection.commit()
    for el in json.loads(res.content.decode(encoding='utf-8')):
        #print(el)
        #statement = f"INSERT INTO {TABLE_NAME}(title,body,owner) values (?,?,?)"
        cursor.execute(statement, (el['title'], el['description'], el['author']))
        connection.commit()

    response = app.response_class(
        response=json.dumps({'STATUS': 'OK'}),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
