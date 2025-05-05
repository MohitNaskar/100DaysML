from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
# This is a simple Flask application that runs on localhost:5000