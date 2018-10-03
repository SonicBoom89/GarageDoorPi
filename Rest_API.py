from flask import Flask, abort, jsonify, request

from Logger import Logger
from GarageDoorController import GarageDoorController
from HardwareController import HardwareController
from time import localtime, strftime
from threading import Thread

app = Flask(__name__)

_log = Logger()
_garageController = GarageDoorController()
_hardwareController = HardwareController()

def startWebApi():
        app.run(debug=True, host="0.0.0.0", threaded=True)

@app.route('/toggle')
def toggle_garage():
    _log.info("Toggle GET Request received: " + str(request))
    cputemp = _hardwareController.getCpuTemp()
    _garageController.toggle()
    return jsonify(result="Toggeling door", CpuTemp=str(cputemp))


startWebApi()