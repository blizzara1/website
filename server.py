from flask import Flask, request, render_template
import json
import requests

app = Flask(__name__)

@app.route('/firstrequest', methods=['GET'])
def firstRequest():
    return('You just posted.... ')

@app.route('/secondrequest', methods=['GET'])
def secondRequest():
    userAgent = str(request.headers['User-Agent'])
    return(render_template('start.html', userAgent = userAgent))

@app.route('/fourthrequest', methods=['GET'])
def fourthRequest():
    return(int("HI"))

@app.route('/thirdrequest', methods=['GET', 'POST'])
def thirdRequest():
    reqData = request.form
    return('You just posted.... ' + str(reqData))

@app.route('/weather', methods=['GET'])
def weather():
    response=requests.get('http://api.openweathermap.org/data/2.5/weather?q=Singapore&appid=7953d6c069a2f1865b1534f2e1cb6be3')
    data = response.json()
    weather = data["weather"][0]["description"]
    weather1 = data["weather"][0]["main"]
    return (render_template('index.html', data_to_pass = weather,data_to_pass_1 = weather1))

if __name__ == '__main__':
    app.run(debug=True)
