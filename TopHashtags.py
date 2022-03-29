
import re

def top_hashtags(data):


    hashtags = {}

    for tweet in data:

        tweet_hashtags = re.findall(r"#(\w+)", tweet['renderedContent'])

        for hashtag in tweet_hashtags:

            if hashtag in hashtags:
                hashtags[hashtag] += 1
            else:
                hashtags[hashtag] = 1

    result = sorted(hashtags.items(), key=lambda item: item[1], reverse=True)

    print('--------Top 10 Hashtags With Most Tweets--------')
    for i in range(0, 9):
        print("Hashtag: ", result[i][0], "Tweet Count: ", result[i][1]) 