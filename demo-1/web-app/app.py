import os
from flask import Flask, request, jsonify, render_template
import logging
import boto3
from botocore.exceptions import ClientError
from upload_to_s3 import upload_file


app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def home():
    return render_template('index_upload.html')

@app.route('/predict',methods=['POST'])
def upload():
    '''
    For rendering results on HTML GUI
    '''
    folder_name = "files" #request.form['upload']
    # this is to verify that folder to upload to exists.
    if os.path.isdir(os.path.join(APP_ROOT, '{}/'.format(folder_name))):
        print("folder exist")
    
    target = os.path.join(APP_ROOT, '{}/'.format(folder_name))
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        ##############################
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        PATH = folder_name + "/" + filename
        upload.save(PATH)
        upload_file(PATH, "lamdademo-1")    
    return render_template('index_upload.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
