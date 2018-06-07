from flask import Flask, render_template, jsonify, request, url_for, redirect
import requests
import os
from cloudant import Cloudant
import json

app = Flask(__name__)

db_name = 'devfestregistration'
client = None
db = None

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

'''
@app.route('/register', methods=['GET','POST'])
def register():
    fullname = request.form['fullname']
    email = request.form['email']
    docJson = {}
    url = ''
    response = requests.post(url, data=docJson)
    response.text
    return redirect(url_for('fa'))
'''

@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)