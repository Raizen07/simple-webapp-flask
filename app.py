import os
from flask import Flask
from flask.ext.mysql import MySQL
app = flask(_name_)

mysql = MYSQL()

mysql_database_host = 'MYSQL_DATABASE_HOST' in os.envron and os.environ['MYSQL_DATABASE_HOST'] or 'localhost'

# MYSQL configurations
app.config['MYSQL_DATABASE_USER'] = 'db_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Password'
app.config['MYSQL_DATABASE_DB'] = 'employee-db'
app.config['MYSQL_DATABASE_HOST'] = mysql_database_host
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()

@app.route("/")
def main():
	return "WELCOME!"
	
@app.route('/how are you')
def hello():
	return' I am good, how about you?'

@app.route('/read from database')
def read():
    cursor.execute("SELECT * FROM employees")
	row = cursor.fetchone()
    result = []
    while row is not None:
		result.append(row[0])
		row = cursor.fetchone()
		
	return ",".join(result)
	
if __name__ == "__main__":
    app.run()
	
