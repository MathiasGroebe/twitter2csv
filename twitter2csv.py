# -*- coding: utf-8 -*-
___author___ = 'MathiasGroebe'


#---impot libaries---
import json

#---setting variables---

in_file = 'test3.json'
out_file = 'out.csv'
delimiter = ';'

csv_file = open(out_file, 'w', encoding = "utf8")
csv_file.write('id' + delimiter + 'user_id' + delimiter + 'text' + delimiter + 'retweet_count' + delimiter + 'favorite_count' + delimiter + 'created_at' + delimiter + 'user_screen_name' + '\n')

with open(in_file, 'r', encoding = "utf8") as data_file:
    for line in data_file:
        tweet = json.loads(line)
        print(tweet['id'])
        csv_file.write(str(tweet['id']) + delimiter)
        csv_file.write(str(tweet['user']['id']) + delimiter)
        csv_file.write('"' + str(tweet['text']) + '"' + delimiter)
        csv_file.write(str(tweet['retweet_count']) + delimiter)
        csv_file.write(str(tweet['favorite_count']) + delimiter)
        csv_file.write(str(tweet['created_at']) + delimiter)
        csv_file.write(str(tweet['user']['screen_name']) + delimiter)
        csv_file.write('\n')

csv_file.close()
