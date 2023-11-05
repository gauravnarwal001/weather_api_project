from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route("/weatherapp",methods = ['post'])
def get_weatherdata():

    url = "https://api.openweathermap.org/data/2.5/weather"

    parse = {
        'q' : request.form.get('city'),
        'units' : request.form.get('units'),
        'appid' : request.form.get('appid') 
        }

    response = requests.get(url,params = parse)
    data = response.json()

    return data



if __name__ == '__main__':
    app.run(host = '0.0.0.0')