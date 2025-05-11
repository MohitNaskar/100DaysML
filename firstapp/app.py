from flask import Flask, render_template, request, redirect, url_for,Response,send_from_directory,jsonify
import pandas as pd
import os,uuid
app = Flask(__name__,template_folder='templates')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')

        return "Yo"

@app.route('/file_upload',methods=['POST'])
def file_upload():
    file = request.files['file']
    if file.filename.endswith(('.txt')):
        return file.read().decode()
    elif file.filename.endswith(('.xls','.xlsx')):
        df = pd.read_excel(file)
        return df.to_html()
    else:
        return "Invalid file type"

@app.route('/convert_csv',methods=['POST'])
def convert_csv():
    file = request.files['file']
    if file.filename.endswith(('.xls','.xlsx')):
        df = pd.read_excel(file)
        response = Response(
            df.to_csv(),
            mimetype="text/csv",
            headers={"Content-disposition":'attachment; filename=result.csv'}
        )
        return response

@app.route('/convert_csv2',methods=['POST'])
def convert_csv2():
    file = request.files['file']
    if file.filename.endswith(('.xls','.xlsx')):
        df = pd.read_excel(file)
        
        if not os.path.exists('downloads'):
            os.makedirs('downloads')

        filename = f'{uuid.uuid4()}.csv'

        df.to_csv(os.path.join('downloads',filename))

        return render_template('download.html',filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads',filename,download_name='result.csv')



if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
# This is a simple Flask application that runs on localhost:5000