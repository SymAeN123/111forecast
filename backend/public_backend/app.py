import sys
import os
from pathlib import Path
root = Path.cwd().parents[1]
sys.path.append(str(root))
from config import PUBLIC_PORT

#Server imports
from flask import Flask, jsonify, request, Response, send_file
from waitress import serve
import requests

app = Flask(__name__, static_url_path="", static_folder="./public")

@app.route("/", methods=["GET"])
def send_home_page():
    return send_file("./public/index.html")


@app.route("/submit", methods=["GET"])
def send_submit_page():
    return send_file("./public/submit/index.html")

@app.route("/validatekey", methods=["GET"])
def get_key_user():
    input = request.json
    print(input)
    #send request

    #return r.json()
    return "returning json"

@app.route("/submitforecast", methods=["POST"])
def send_forecast_to_db():
    #Validate input
    input = request.json
    print(input)

    #Formulate JSON

    #Send the post request to db API

    #Get request status

    #Return success or failure
    return jsonify(
        {
            "text": "got the post"
        }
    )

@app.route("/getforecastdate", methods=["GET"])
def get_next_forecast_date():
    #Send get request to db API

    #Create UTC Date Dict

    return "dict with utc date or valid=false"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PUBLIC_PORT)
    #serve(app, host='0.0.0.0', port=PUBLIC_PORT, threads=1)