
def top_retweeted(data):

    result = sorted(data, key=lambda d: d['retweetCount'], reverse=True)

    print('--------Top 10 Retweeted Tweets--------')
    for i in range(0, 9):
        print("Id: ", result[i]['id'], "Retweet Count: ", result[i]['retweetCount']) 
