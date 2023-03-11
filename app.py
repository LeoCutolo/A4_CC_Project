from flask import Flask, render_template
import requests
import os
import mysql.connector
import sys

app = Flask(__name__)

db_host="mariadb"
api_key = os.getenv('API_KEY')
db_name = os.getenv('DB_NAME')
db_table = os.getenv('DB_TABLE')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def connect_to_db():
    db = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    return db

def add_to_db(data):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "INSERT INTO " + db_name + "." + db_table + " (city, temperature, date) VALUES (%s, %s, FROM_UNIXTIME(%s))"
    val = (data['name'], data['main']['temp'], data['dt'])
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()

def get_from_db(city):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "SELECT * FROM " + db_name + "." + db_table + " WHERE city = %s AND date >= CURDATE() ORDER BY date DESC"
    val = (city,)
    cursor.execute(sql, val)
    rows = cursor.fetchall()
    result = []
    for row in rows:
        #print(f"Row: {row}", file=sys.stderr)
        result.append(f"{row[1]} : {row[2]}°C at {row[3].strftime('%H:%M')}")
    cursor.close()
    db.close()

    return result

@app.route('/')
def index():
    with open('/app/src/city.txt', 'r') as f:
        city = f.readline().strip()
    weather = get_weather(city)
    temperatures = get_from_db(city)
    print(f"Temperatures: {temperatures}", file=sys.stderr)
    add_to_db(weather)
    return render_template('index.html', weather=weather, temperatures=temperatures)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)