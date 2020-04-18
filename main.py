import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def helloWorld():
    name = "名無し"
    #return name
    return render_template('hello.html', title='hello', name=name)

@app.route('/<name>')
def helloName(name):
    #return name

    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?'
    query_params = {'city': '130010'}
    data = requests.get(url, params=query_params).json()
    weatherJson = data['forecasts']
    weather = '東京の' + weatherJson[0]['dateLabel'] + 'の天気：' + weatherJson[0]['telop']

    return render_template('hello.html', title='hello', name=name, weather=weather)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)