'''
Source:
Author: Raja CSP
'''
from flask import Flask,jsonify, request,\
    render_template

import json

app  = Flask(__name__)
PORT = 3011

@app.route("/", methods = ["GET"])
def api_base():

    # result = {
    #     "One" : "Two"
    # }

    # return jsonify(result)
    #    return "helloworld"  
       return render_template('index.html')

if __name__ == "__main__":
    app.run( debug = True,host="0.0.0.0",port = PORT)