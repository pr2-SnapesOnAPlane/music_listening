from flask import Flask, render_template, url_for, jsonify
import os
import requests
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def homepage():
  return render_template('index.html')


@app.route('/test')
def get_file_content(test):
    with open('test.json', 'r') as file:
        return file.read()
  


if __name__ == '__main__':
  app.run(host='127.0.0.1', debug=True)