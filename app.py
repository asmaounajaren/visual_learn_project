from flask import Flask, render_template, request , jsonify
from mysqlConnection import configure_db
from flask_mysqldb import MySQL
import base64
from backend import create_emotion_pie_chart,analyze_emotions,plot_engagement_percentage,analyze_engagement,create_emotion_chart_for_person
from datetime import datetime
app = Flask(__name__)

mysql=configure_db(app)

# Example route that fetches data from the database
@app.route('/', methods=['GET'])
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT image_path FROM session_image")
    image_records  = cur.fetchall()
    images = [{'image_path': 'data:image/jpeg;base64,' + base64.b64encode(image[0]).decode('utf-8')} for image in image_records]
    cur.execute("SELECT * FROM student")
    students = cur.fetchall()
    chart_data = create_emotion_pie_chart('merged_output.csv')
    csv_file = 'merged_output.csv'
    emotion, recommendations = analyze_emotions(csv_file)
    plot_eng = plot_engagement_percentage(csv_file)
    anlyze_eng = analyze_engagement('merged_output.csv')

    cur.execute("SELECT course_name, session_date, classroom FROM course_session")
    session_details = cur.fetchone()
    course_name = session_details[0]  # Index 0 corresponds to the first column 'course_name'
    session_date = session_details[1]  # Index 1 corresponds to the second column 'session_date'
    classroom = session_details[2]  # Index 2 corresponds to the third column 'classroom'
    session_datetime = session_date  # If session_date is already a datetime object, no need to convert

    session_date_formatted = session_datetime.strftime('%Y-%m-%d')  # Format as YYYY-MM-DD
    session_time = session_datetime.strftime('%H:%M:%S')

    cur.close()

    return render_template("index.html", chart_data=chart_data, emotion=emotion, recommendations=recommendations, plot=plot_eng, engagements=anlyze_eng,images=images,students=students,course_name=course_name, hour=session_time, session_date_formatted=session_date_formatted , classroom=classroom)
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
    
@app.route('/show_statistic', methods=['POST'])
def show_statistic():
    person = int(request.form.get('person'))
    image_base64 = create_emotion_chart_for_person('merged_output.csv',person)

    if image_base64:
        return jsonify({'image_base64': image_base64})
    else:
        return jsonify({'error': 'No data found for the specified person'}), 404
if __name__ == '__main__':
    app.run(debug=True)
