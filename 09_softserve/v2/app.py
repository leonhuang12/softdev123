# Cheerio - Leon, Naomi, Tanzeem
# SoftDev
# K09: Putting it Together
# 2024-09-24

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #where will this go? in the terminal
    return "No hablo queso!"

app.run()

