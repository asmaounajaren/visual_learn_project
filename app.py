from flask import Flask, render_template, request
from mysqlConnection import configure_db
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "visual_learn_project"
mysql = MySQL(app)

# Example route that fetches data from the database
@app.route('/', methods=['GET'])
def index():
    #try:
    #     cur = mysql.connection.cursor()
    #     cur.execute('SELECT image_path FROM session_image')
    #     data = cur.fetchall()
    #     cur.close()
    #     return render_template('index.html', data=data)
    # except Exception as e:
    #     print("An error occurred:", e)
    return render_template("index.html")
@app.route('/test_mysql')
def test_mysql():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT 1')
        result = cur.fetchone()
        cur.close()
        return f"MySQL Connection Test Successful. Result: {result}"
    except Exception as e:
        return f"MySQL Connection Test Failed. Error: {e}"
if __name__ == '__main__':
    app.run(debug=True)
