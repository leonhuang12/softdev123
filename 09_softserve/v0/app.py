# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # ...

@app.route("/")                # ...
def hello_world():
    print(__name__)            # ... prints "__main__" in terminal
    return "No hablo queso!"   # ... prints the string into website

app.run()                      # ... runs
                
