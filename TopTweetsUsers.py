
def top_tweets_users(data):


    users = {}

    for tweet in data:

        if tweet['user']['id'] in users:
            users[tweet['user']['id']] += 1
        else:
            users[tweet['user']['id']] = 1

    result = sorted(users.items(), key=lambda item: item[1], reverse=True)

    print('--------Top 10 Users With Most Tweets--------')
    for i in range(0, 9):
        print("User Id: ", result[i][0], "Tweet Count: ", result[i][1]) 
