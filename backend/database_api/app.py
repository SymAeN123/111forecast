#System imports
import sys
import os
from pathlib import Path
cwd = Path.cwd()
root = Path.cwd().parents[1]
sys.path.append(str(root))
from config import DB_PORT

#Server imports
from flask import Flask, jsonify, request, Response, send_file
from waitress import serve
import requests

#Import Database things
import sqlite3
from datetime import datetime

#Environment Variables
from dotenv import load_dotenv
load_dotenv()
MESOWEST_API_KEY = os.getenv('MESOWEST_API_KEY')

app = Flask(__name__, static_url_path="")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=DB_PORT)
    #serve(app, host='0.0.0.0', port=DB_PORT, threads=1)