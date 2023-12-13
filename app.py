from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# MySQL configurations
app.config['MYSQL_USER'] = 'A'
app.config['MYSQL_PASSWORD'] = 'B'
app.config['MYSQL_DB'] = 'student'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)

@app.route("/add", methods=['POST'])
def add():
    name = request.form.get('name')
    email = request.form.get('email')
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO students(studentName, email) VALUES(%s, %s);', (name, email))
    mysql.connection.commit()
    return jsonify({'result': 'success'})

@app.route("/update/<int:id>", methods=['POST'])
def update(id):
    name = request.form.get('name')
    email = request.form.get('email')
    cur = mysql.connection.cursor()
    cur.execute("UPDATE students SET studentName=%s, email=%s WHERE studentID=%s", (name, email, id))
    mysql.connection.commit()
    return jsonify({'result': 'updated'})

@app.route("/delete/<int:id>", methods=['GET'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE studentID=%s", [id])
    mysql.connection.commit()
    return jsonify({'result': 'deleted'})

@app.route("/read/<int:id>", methods=['GET'])
def read_one(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students WHERE studentID=%s", [id])
    row = cur.fetchone()
    if row:
        result = {'Name': row[0], 'Email': row[1], 'ID': row[2]}
        return json.dumps(result)
    else:
        return jsonify({'message': 'Student not found'})

@app.route("/remove/<int:id>", methods=['GET'])
def remove(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE studentID=%s", [id])
    mysql.connection.commit()
    return jsonify({'result': 'deleted'})

@app.route("/", methods=['GET'])
def read_all():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    rv = cur.fetchall()
    results = [{'Name': row[0], 'Email': row[1], 'ID': row[2]} for row in rv]
    return render_template('index.html', Results=results, count=len(results))

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=8080)
