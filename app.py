from flask import Flask,jsonify
import csv
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.worldometers.info/coronavirus/"
def scrape_data(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find_all('table')[0]
    rows = table.select('tbody > tr')
    data = [ ]
    for row in rows[:]:
        data.append([th.text.rstrip() for th in row.find_all('td')])
    return data

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/countries/cases', methods=['GET'])
def get_cases():
    global url
    response = {}
    data = scrape_data(url)
    for i in data:
        response[i[0]] = int(i[1].replace(',',""))
    return jsonify({'cases': response})

@app.route('/countries/new-cases', methods=['GET'])
def get_new_cases():
    global url
    response = {}
    data = scrape_data(url)
    for i in data:
        value = i[2].replace(',',"") if i[2] else i[2].replace('',"0")
        response[i[0]] = int(value)
    return jsonify({'new-cases': response})


@app.route('/countries/deaths', methods=['GET'])
def get_deaths():
    global url
    response = {}
    data = scrape_data(url)
    for i in data:
        value = i[3].replace(',',"") if i[3] else i[3].replace('',"0")
        response[i[0]] = int(value)
    return jsonify({'deaths': response})

@app.route('/countries/new-deaths', methods=['GET'])
def get_new_deaths():
    global url
    response = {}
    data = scrape_data(url)
    for i in data:
        value = i[4].replace('+',"") if i[4] else i[4].replace('',"0")
        response[i[0]] = int(value)
    return jsonify({'new-deaths': response})

@app.route('/countries/active-cases', methods=['GET'])
def get_active_cases():
    global url
    response = {}
    data = scrape_data(url)
    for i in data:
        value = i[6].replace(',',"") if i[6] else i[6].replace('',"0")
        response[i[0]] = int(value)
    return jsonify({'active-cases': response})

@app.route('/countries/serious-critical', methods=['GET'])
def get_serious_critical():
    global url
    response = {}
    data = scrape_data(url)
    for i in data:
        value = i[7].replace(',',"") if i[7] else i[7].replace('',"0")
        response[i[0]] = int(value)
    return jsonify({'serious-critical': response})

@app.route('/countries/recovered', methods=['GET'])
def get_recovered():
    global url
    response = {}
    data = scrape_data(url)
    for i in data:
        value = i[5].replace(',',"") if i[5] else i[5].replace('',"0")
        response[i[0]] = int(value)
    return jsonify({'recovered': response})

@app.route('/countries/cases/million-population', methods=['GET'])
def get_cases_per_million_population():
    global url
    response = {}
    data = scrape_data(url)
    for i in data:
        value = i[8].replace(',',"") if i[8] else i[8].replace('',"0")
        response[i[0]] = float(value)
    return jsonify({'million-population': response})


if __name__ == '__main__':
    app.run(debug=True)
