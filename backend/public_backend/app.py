#Server imports
from flask import Flask, jsonify, request, Response, send_file
from waitress import serve
import requests

#Environment Variables
from dotenv import load_dotenv
from os import getenv
load_dotenv()
MESOWEST_API_KEY = getenv('MESOWEST_API_KEY')

app = Flask(__name__, static_url_path="", static_folder="./public")

@app.route("/", methods=["GET"])
def send_home_page():
    return send_file("./public/index.html")


@app.route("/submit", methods=["GET"])
def send_current_page():
    return send_file("./public/submit/index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    #serve(app, host='0.0.0.0', port=8080, threads=1)