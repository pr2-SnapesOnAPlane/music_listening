from flask import Flask, render_template, url_for, jsonify, send_from_directory
import os
import requests
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def homepage():
  return render_template('index.html')


@app.route('/test.json')
def get_file_content():
  return send_from_directory('js', 'test.json')
  


if __name__ == '__main__':
  app.run(host='127.0.0.1', debug=True)
