import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Supreme Omni Engine Live on Render Cloud!</h1>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
