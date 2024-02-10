from flask import Flask, render_template, request
from mysqlConnection import configure_db
from flask_mysqldb import MySQL
import base64
from backend import create_emotion_pie_chart,analyze_emotions,plot_engagement_percentage,analyze_engagement

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "visual_learn_project"
mysql = MySQL(app)

# Example route that fetches data from the database
@app.route('/', methods=['GET'])
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT image_path FROM session_image")
    image_records  = cur.fetchall()
    cur.close()
    images = [{'image_path': 'data:image/jpeg;base64,' + base64.b64encode(image[0]).decode('utf-8')} for image in image_records]

    chart_data = create_emotion_pie_chart('merged_output.csv')
    csv_file = 'merged_output.csv'
    emotion, recommendations = analyze_emotions(csv_file)
    plot_eng = plot_engagement_percentage(csv_file)
    anlyze_eng = analyze_engagement('merged_output.csv')
    return render_template("index.html", chart_data=chart_data, emotion=emotion, recommendations=recommendations, plot=plot_eng, engagements=anlyze_eng,images=images)
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
