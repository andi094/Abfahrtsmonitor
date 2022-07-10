from flask import Flask, render_template, jsonify
import requests
from requests.structures import CaseInsensitiveDict
import json


import pandas as pd
import sys
import logging

app = Flask(__name__)

# ensure that we can reload when we change the HTML / JS for debugging
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def data():
    # replace this with the real data
    # Get data (json) from stop"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"


    # diva Am Tabor = 60200051
    respAmTabor = requests.get("https://www.wienerlinien.at/ogd_realtime/monitor?diva=60200051&activateTrafficInfo=stoerungkurz&activateTrafficInfo=stoerunglang&activateTrafficInfo=aufzugsinfo", headers=headers)
    respNordbahnstrasse = requests.get("https://www.wienerlinien.at/ogd_realtime/monitor?diva=60200941&activateTrafficInfo=stoerungkurz&activateTrafficInfo=stoerunglang&activateTrafficInfo=aufzugsinfo", headers=headers)
    print(respAmTabor.text)
    print(respNordbahnstrasse.text)
    dataAmTabor = json.loads(respAmTabor.text)
    dataNordbahnstrasse = json.loads(respNordbahnstrasse.text)

    data = [dataAmTabor, dataNordbahnstrasse]
    print(data)
    return render_template("index.html", data=json.dumps(data))

if __name__ == '__main__':
    app.run(debug=True)

