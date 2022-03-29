
def top_tweets_days(data):


    days = {}

    for tweet in data:

        date = tweet['date'][0:10]

        if date in days:
            days[date] += 1
        else:
            days[date] = 1

    result = sorted(days.items(), key=lambda item: item[1], reverse=True)

    print('--------Top 10 Days With Most Tweets--------')
    for i in range(0, 9):
        print("Date: ", result[i][0], "Tweet Count: ", result[i][1]) 
