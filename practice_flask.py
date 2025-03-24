from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'anm'
mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/data', methods=['GET'])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM table_name') 
    data = cur.fetchall()
    cur.close()
    result = []
    for row in data:
        result.append({'id': row[0], 'name': row[1], 'age': row[2]})
    return jsonify(result)

@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM table_name WHERE id = %s', (id,))
    data = cur.fetchall()
    cur.close()
    
    if data:
        result = {'id': data[0][0], 'name': data[0][1], 'age': data[0][2]}
        return jsonify(result)
    else:
        return jsonify({'message': 'Data not found'}), 404

@app.route('/data', methods=['POST'])
def add_data():
    try:
        name = request.json['name']
        age = request.json['age']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO table_name (name, age) VALUES (%s, %s)', (name, age))
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'message': 'Data added successfully'}), 201
    except KeyError:
        return jsonify({'message': 'Bad request, missing name or age'}), 400

@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    try:
        name = request.json['name']
        age = request.json['age']
        cur = mysql.connection.cursor()
        cur.execute('UPDATE table_name SET name = %s, age = %s WHERE id = %s', (name, age, id))
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'message': 'Data updated successfully'})
    except KeyError:
        return jsonify({'message': 'Bad request, missing name or age'}), 400

@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM table_name WHERE id = %s', (id,))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Data deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)