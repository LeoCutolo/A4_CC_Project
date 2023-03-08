from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

api_key = os.getenv('API_KEY')

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/')
def index():
    with open('city.txt', 'r') as f:
        city = f.readline().strip()
    weather = get_weather(city)
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)