from flask import Flask, jsonify, request
import os
import time
import datetime
from datetime import date



app = Flask(__name__)

@app.route('/data', methods=['POST'])
def savedata():		
	filename = str(request.remote_addr)+"_"+str(datetime.datetime.today().year)+"-"+str(datetime.datetime.today().month)+"-"+str(datetime.datetime.today().day)+".json"
	file = open(filename, "w")
	file.write(request.json)
	file.close()
	return "recibido"


if __name__ == '__main__':
	app.run(debug=True, port=8080)
	file 