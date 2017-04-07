# -*- coding: utf-8 -*-
___author___ = 'MathiasGroebe'


#---impot libaries---
import json
import math
from datetime import datetime

#---setting variables---

in_file = 'test6.json'
out_file = 'out.csv'
delimiter = ';'

csv_file = open(out_file, 'w', encoding = "utf8")
csv_file.write('id' + delimiter + 'user_id' + delimiter + 'text' + delimiter + 'language' + delimiter + 'retweet_count' + delimiter + 'favorite_count' + delimiter + 'created_at' + delimiter + 'user_screen_name' + delimiter + 'lat' + delimiter + 'lng' + delimiter + 'cood_type' + delimiter + 'place_type' + delimiter + 'place_name' + delimiter + '\n')

with open(in_file, 'r', encoding = "utf8") as data_file:
    for line in data_file:
        tweet = json.loads(line)

        #check if tweet or limit
        if 'id' in tweet:

            #print(tweet['id'])
            csv_file.write(str(tweet['id']) + delimiter)
            csv_file.write(str(tweet['user']['id']) + delimiter)
            #remove linebreaks
            text = tweet['text'].replace('\r', '').replace('\n', '')
            csv_file.write('"' + str(text) + '"' + delimiter)
            csv_file.write(str(tweet['lang']) + delimiter)
            csv_file.write(str(tweet['retweet_count']) + delimiter)
            csv_file.write(str(tweet['favorite_count']) + delimiter)
            #convert timestamp (UTC)
            timestamp = datetime.utcfromtimestamp(round(int(tweet['timestamp_ms'])/1000, 0))
            csv_file.write(str(timestamp) + delimiter)
            csv_file.write(str(tweet['user']['screen_name']) + delimiter)

            #calculate geometry, use native coordinates or centroid from polygon
            if(tweet['geo'] == None):
                if(tweet['place']['bounding_box']['type'] == 'Polygon'):
                    x1 = tweet['place']['bounding_box']['coordinates'][0][0][0]
                    x2 = tweet['place']['bounding_box']['coordinates'][0][2][0]
                    y1 = tweet['place']['bounding_box']['coordinates'][0][0][1]
                    y2 = tweet['place']['bounding_box']['coordinates'][0][1][1]

                    #calculate centroid
                    x = -9999
                    y = -9999
                    if(math.fabs(x2) < math.fabs(x1)):
                        x = x2 + ((x1 - x2) / 2)
                    else:
                        x = x1 + ((x2 - x1) / 2)
                    if(math.fabs(y2) < math.fabs(y1)):
                        y = y2 + ((y1 - y2) / 2)
                    else:
                        y = y1 + ((y2 - y1) / 2)

                    csv_file.write(str(x) + delimiter)
                    csv_file.write(str(y) + delimiter)
                    csv_file.write('place' + delimiter)
                    csv_file.write(str(tweet['place']['place_type']) + delimiter)
                    csv_file.write(str(tweet['place']['name']) + delimiter)

                else:
                    print('No Polygon!')
                    csv_file.write(str(-9999) + delimiter)
                    csv_file.write(str(-9999) + delimiter)
                    csv_file.write('none' + delimiter)
                    csv_file.write('none' + delimiter)
            else:
                csv_file.write(str(tweet['geo']['coordinates'][0]) + delimiter)
                csv_file.write(str(tweet['geo']['coordinates'][1]) + delimiter)

                if(tweet['place'] == None):
                    csv_file.write('coord' + delimiter)
                    csv_file.write('none' + delimiter)
                    csv_file.write('none' + delimiter)
                else:
                    csv_file.write('both' + delimiter)
                    csv_file.write(str(tweet['place']['place_type']) + delimiter)
                    csv_file.write(str(tweet['place']['name']) + delimiter)

            csv_file.write('\n')

        # Handle Error / Limit
        else:
            print('Limit/Error')
            csv_file.write(str(-9999) + delimiter)
            csv_file.write(str(-9999) + delimiter)
            csv_file.write('Limit' + delimiter)
            csv_file.write(str(0) + delimiter)
            csv_file.write(str(0) + delimiter)
            csv_file.write(str(0) + delimiter)
            #convert timestamp (UTC)
            timestamp = datetime.utcfromtimestamp(round(int(tweet['limit']['timestamp_ms'])/1000, 0))
            csv_file.write(str(timestamp) + delimiter)
            csv_file.write('Twitter' + delimiter)
            csv_file.write(str(-9999) + delimiter)
            csv_file.write(str(-9999) + delimiter)
            csv_file.write('none' + delimiter)
            csv_file.write('none' + delimiter)
            csv_file.write('none' + delimiter)
            csv_file.write('\n')


csv_file.close()
