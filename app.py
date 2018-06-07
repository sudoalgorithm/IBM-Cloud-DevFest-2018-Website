from flask import Flask, render_template, jsonify, request, url_for, redirect
import requests
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    fullname = request.form['fullname']
    email = request.form['email']
    docJson = {}
    url = ''
    response = requests.post(url, data=docJson)
    response.text
    return redirect(url_for('fa'))


@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)