# Leon Huang
# Cheerio - Naomi, Leon, Tanzeem
# SoftDev
# K09: Putting it Together
# 2024-09-24
# time spent: 1

'''
DISCO:
access value in key: dict[key] -> values

'''

import csv
import random
from flask import Flask

def read_csv(csvfile):
    with open(csvfile, newline='') as csv_file:
        header = next(csv_file)
        percent = 0.0
        content = csv.reader(csv_file)
        dic = {}
        for row in content:
            percent += float(row[1])
            percent = round(percent, 1)
            dic[percent] = row[0]

        dic.popitem()
        #print(dic) key: value --> percentage: occupation
        return dic
    
def choose_random(csvfile):
    data = read_csv(csvfile)
    keys = [key for key in data.keys()]
    random_num = random.random() * 99.8 #random_num is the chance
    for i in range(len(keys)):
        if keys[i] > random_num:
            return data[keys[i-1]] 
            #when percentage is greater than random_num, it is the right occupation

# keep function definitions above @app.route("/")

def heading():
    return "<h4> team name: Naomi, Tanzeem, Leon</h4>"

def occ_list():
    occ_dict = read_csv('occupations.csv')
    st = '<br>'
    for key in occ_dict:
        st = st + '<br>' + occ_dict[key]
        #print(occ_dict[key])
    return st

app = Flask(__name__)
@app.route("/")

def occupation_chooser():
    st = ''
    st += heading()
    st = st + "random occupation: " + choose_random('occupations.csv') 
    st += occ_list()
    return st

# to do-- display list of occupations, display TPNG+roster(???)

app.run(port=5001)