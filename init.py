from flask import Flask, request, render_template, jsonify

from flask_cors import CORS

intergrations = []

import twitch
intergrations.append(twitch)

threads = []

app = Flask(__name__)
app.debug = True
#CORS(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/fetch", methods=["GET"])
def FetchMessages():

	messages = {}
	for intergration in intergrations:
		name = intergration.Name()
		messageArray = intergration.FetchMessages(intergration)
		messages[name] = messageArray
	messageJson = jsonify(messages)

	#messageJson.headers.add("Access-Control-Allow-Origin", "*")
	#messageJson.headers.add("Access-Control-Allow-Headers", "*")
	#messageJson.headers.add("Access-Control-Allow-Methods", "*")
	return messageJson

if __name__ == "__main__":

	for intergration in intergrations:
		thread = intergration.Setup()

		if thread != None:
			threads.append(thread)
			thread.start()

	app.run(host= "0.0.0.0", port="5001")