# -*- coding: utf-8 -*-
___author___ = 'MathiasGroebe'


#---impot libaries---
import json
import math

#---setting variables---

in_file = 'test5.json'
out_file = 'out.csv'
delimiter = ';'

csv_file = open(out_file, 'w', encoding = "utf8")
csv_file.write('id' + delimiter + 'user_id' + delimiter + 'text' + delimiter + 'retweet_count' + delimiter + 'favorite_count' + delimiter + 'created_at' + delimiter + 'user_screen_name' + delimiter + 'lat' + delimiter + 'lng' + delimiter + 'cood_type' + '\n')

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

            else:
                print('No Polygon!')
                csv_file.write(str(-9999) + delimiter)
                csv_file.write(str(-9999) + delimiter)
                csv_file.write('error' + delimiter)
        else:
            csv_file.write(str(tweet['geo']['coordinates'][0]) + delimiter)
            csv_file.write(str(tweet['geo']['coordinates'][1]) + delimiter)

            if(tweet['place'] == None):
                csv_file.write('coord' + delimiter)
            else:
                csv_file.write('both' + delimiter)

        csv_file.write('\n')

csv_file.close()
