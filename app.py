from flask import Flask, render_template, request, jsonify, url_for, redirect
from cloudant import Cloudant
import os
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

@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/registration')
def register():
    return render_template('registration_complete.html')

@app.route('/api/register', methods=['POST'])
def put_register():
    fullname = request.json['fullname']
    emailaddress = request.json['emailaddress']
    trackArray = request.json['trackArray']
    language = request.json['language']
    disclaimer = request.json['disclaimer']
    data = {
            'fullname':fullname,
            'emailaddress':emailaddress,
            'trackArray':trackArray,
            'language':language,
            'disclaimer':disclaimer
            }
    if client:
        my_document = db.create_document(data)
        data['_id'] = my_document['_id']
        return jsonify(data)
    else:
        print('No database')
        return jsonify(data)
    return redirect(url_for('register'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)