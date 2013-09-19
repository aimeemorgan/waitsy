#!/usr/bin/python
from chains import build_song
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
	song = build_song()
	return render_template('index.html', verse1=song[0],
										 verse2=song[1],
										 verse3=song[2],
										 chorus=song[3],
										 title=song[3][0])

if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=0000)

