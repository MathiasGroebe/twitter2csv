# -*- coding: utf-8 -*-
___author___ = 'MathiasGroebe'


#---impot libaries---
import json

#---setting variables---

file_name = 'test3.json'

with open(file_name, 'r', encoding="utf8") as data_file:
    for line in data_file:
        tweet = json.loads(line)
        print(tweet['id'])
