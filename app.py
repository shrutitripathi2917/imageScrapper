from flask import Flask, request, jsonify, render_template
from flask_cors import CORS , cross_origin
import pickle

app=Flask(__name__)

@app.route('/')
@cross_origin()
def home_page():
    return render_template("index.html")

@app.route('/searchImages' , methods=['GET','POST'])
@cross_origin()
def serachImages():
    if request.method=='POST':
        print("enternd post")
        keyWord=request.form('keyword')
    else:
        print("did not enter post")
        print("printing  " + keyWord)


if __name__=='__main__':
    app.run(debug=True)