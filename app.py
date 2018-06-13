from flask import Flask, render_template, request, jsonify, url_for, redirect
from cloudant import Cloudant
from flask_mail import Mail, Message
import os
import json
import atexit

app = Flask(__name__)

# Load configuration from file
app.config.from_pyfile('config.cfg')

# instantiate mail part
mail = Mail(app)

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
    mobilenumber = request.json['mobilenumber']
    disclaimer = request.json['disclaimer']
    data = {
            'fullname':fullname,
            'emailaddress':emailaddress,
            'trackArray':trackArray,
            'language':language,
            'mobilenumber':mobilenumber,
            'disclaimer':disclaimer
            }
    if client:
        # store data
        my_document = db.create_document(data)
        data['_id'] = my_document['_id']
        # Send email and calendar invite
        msg = Message('See you at: DevFest 2018', sender='devfest2018.ml@gmail.com', recipients=[emailaddress])
        msg.body=render_template('mailtext.txt')
        msg.html=render_template('mailtext.html')
        with app.open_resource("DevFest2018.ics") as fp:
            msg.attach("DevFest2018.ics", "text/calendar", fp.read())
        mail.send(msg)
        return jsonify(data)
    else:
        print('No database')
        return jsonify(data)
    return "Registration Failed"

@atexit.register
def shutdown():
    if client:
        client.disconnect()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
