#Hello
from flask import Flask , render_template , request
#import urllib
#import os
import requests, json
#import http.client

app = Flask(__name__)

@app.route('/' , methods=['GET' , 'POST'])
def index():
    if request.method=='POST':
        city_name = request.form.get('city')
        url = "https://yahoo-weather5.p.rapidapi.com/weather"

        querystring = {"location":city_name,"format":"json","u":"C"}

        headers = {
            "X-RapidAPI-Key": "51b933430bmshd2a213d0a0aea60p1f91d4jsn3060816c96c9",
            "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        my_data = response.json()
        # return response.text
        country =my_data['location']['country']
        return render_template('index.html' , country = country)
    else:
        return render_template('index.html')

if __name__== "__main__":
    app.run(host='0.0.0.0' , port=5000 , debug = True)
