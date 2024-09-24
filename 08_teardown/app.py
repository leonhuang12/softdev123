# your heading here

'''
DISCO:
<note any discoveries you made here... no matter how small!>
. /path/bin/activate 

QCC:
0. This is similar to java when you initialize an object
1. Root directory in terminal
2. Will print in the terminal
3. "__main__"
4. In a website that is linked when the program is run in the terminal
5. Call to a function 
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
 Created an venv, installed flask, then ran app.py
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?