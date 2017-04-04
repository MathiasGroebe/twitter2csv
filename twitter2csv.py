# -*- coding: utf-8 -*-
___author___ = 'MathiasGroebe'


#---impot libaries---
import json
import csv

#---setting variables---

file_name = 'test3.json'

with open(file_name, 'r') as data_file:
    line = data_file.readline()
    tweet = json.loads(line)
    print(json.dumps(tweet, indent = 4))
