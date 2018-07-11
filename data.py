import tweepy
import csv

import pandas as pd
consumer_key ='v6A85VtD1yxmJXrGlTgQHLbMh'
consumer_secret ='Y108lSTX1huDuVui8wmqALr6HVY5BkM7pBhqaDhl0npcEeOJn8'
access_token_key ='1016287031973031938-eLhh1f8oBAUJOxC7EvhCIwjBqIpj7U'
access_token_secret ='DQCadF8WTjAnyhcizXDFf7KPDGJ5pgAzrDZoG5LoAWwfA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


csvFile = open('worldCup.csv', 'a')
#Use csv Writer

csvWriter = csv.writer(csvFile)
i=0


#
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-06-29 23:59:59',since='2018-06-29 11:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-06-30 11:59:59',since='2018-06-29 23:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-06-30 23:59:59',since='2018-06-30 11:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-01 11:59:59',since='2018-06-30 23:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-01 23:59:59',since='2018-07-01 11:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-02 11:59:59',since='2018-07-01 23:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-02 23:59:59',since='2018-07-02 11:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-03 11:59:59',since='2018-07-02 23:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-03 23:59:59',since='2018-07-03 11:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-04 11:59:59',since='2018-07-03 23:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-04 23:59:59',since='2018-07-04 11:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-05 11:59:59',since='2018-07-04 23:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-05 23:59:59',since='2018-07-05 11:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-06 11:59:59',since='2018-07-05 23:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-06 23:59:59',since='2018-07-06 11:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-07 11:59:59',since='2018-07-06 23:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-07 23:59:59',since='2018-07-07 11:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-08 11:59:59',since='2018-07-07 23:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
# for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
#                            lang="en",
#                            until='2018-07-08 23:59:59',since='2018-07-08 11:59:59').items(2000):
#     print(i)
#     i += 1
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])





for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
                           lang="en",
                           until='2018-06-30',since='2018-06-29').items(5000):
    print(i)
    i += 1
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
                           lang="en",
                           until='2018-07-01',since='2018-06-30').items(5000):
    print(i)
    i += 1
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

for tweet in tweepy.Cursor(api.search,q="#worldcup",count=100,
                           lang="en",
                           until='2018-07-02' , since='2018-07-01').items(5000):
    print(i)
    i+=1
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
                           lang="en",
                           until='2018-07-03',since='2018-07-02').items(5000):
    print(i)
    i += 1
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
                           lang="en",
                           until='2018-07-04',since='2018-07-03').items(5000):
    print(i)
    i += 1
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
                           lang="en",
                           until='2018-07-05',since='2018-07-04').items(5000):
    print(i)
    i += 1
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
                           lang="en",
                           until='2018-07-06',since='2018-07-05').items(5000):
    print(i)
    i += 1
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
                           lang="en",
                           until='2018-07-07',since='2018-07-06').items(5000):
    print(i)
    i += 1
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

for tweet in tweepy.Cursor(api.search, q="#worldcup", count=100,
                           lang="en",
                           until='2018-07-08',since='2018-07-07').items(5000):
    print(i)
    i += 1
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

















