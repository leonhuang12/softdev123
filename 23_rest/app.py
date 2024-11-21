from flask import Flask, render_template, request
from urllib.request import urlopen
import json


app = Flask(__name__)

url = "https://api.nasa.gov/planetary/apod?api_key="
keyFile = open("key_nasa.txt")
API = keyFile.read()
link = urlopen(url+API)
data = json.loads(link.read())


@app.route('/')
def display():
    return render_template("main.html", expl = data["explanation"], d8=data["date"], hdu = data["hdurl"], u = data["url"], )


if __name__ == "__main__":
    app.debug = True
    app.run()