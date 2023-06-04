from flask import Flask, render_template, request, redirect
import requests
from datetime import datetime
import json
import pytz
import os

app = Flask(__name__)

# Enable debug mode
app.debug = True

# A list to store registered users (in a real application, this would be stored in a database)
users = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users.append({'username': username, 'password': password})
        return redirect('/login')
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username and user['password'] == password:
                return render_template('welcome.html', username=username)
        return "Invalid username or password"
    return render_template('login.html')


@app.route('/signout')
def signout():
    # Redirect to the login page after signout
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    # Fetch current weather data from OpenWeatherMap API
    api_key = 'f714fc9075e33b595b1e9ef7ec5682e6'

    city = 'London'  # Replace with the desired city name or latitude/longitude
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},uk&APPID={api_key}'
    # url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    # Extract relevant information
    print(data)
    location = data['name']
    temperature = data['main']['temp']
    celsius_temp = temperature - 273.15
    celsius_temp = format(celsius_temp, ".2f")
    current_date = datetime.now().strftime('%Y-%m-%d')
    est_timezone = pytz.timezone('US/Eastern')
    current_time = datetime.now(est_timezone).strftime('%H:%M:%S')


    # Return the weather data as JSON
    weather_data = {
        'location': location,
        'temperature': celsius_temp,
        'date': current_date,
        'time': current_time
    }
    return weather_data

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
