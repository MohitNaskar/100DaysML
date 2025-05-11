from flask import Flask, render_template, request, redirect, url_for,Response,send_from_directory,jsonify
import pandas as pd
import os,uuid
app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/')

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
# This is a simple Flask application that runs on localhost:5000