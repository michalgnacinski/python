import tweepy

consumer_key = 'nFuAGRjNVY6Pe3ffC9o6rykqo'
consumer_secret = 'AD0x8TNAV0lJVgVwUsCus00Dqk0QMRRRTtcejFrk7JRrAnRIbv'
access_token = '1544345156777902080-9bh9lHPU9ZzOSOmCqSJIHoVL5N7Nz7'
access_token_secret = 'NxENVHMnLD57NpuuP7qinbrjNATqoyOZnrNSnR5hxaqNV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.verify_credentials()
print(user.screen_name)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print("Followed everyone that is following" + user.screen_name)

def mainFunction():
    search = "Nawrocki"
    numberOfTweets = "Number of tweets you wish to interact with"
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.retweet()
            print('Retweeted the tweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    
