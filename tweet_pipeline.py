import pandas as pd
import tweepy
from keys import twitter
import json
from tweet_process import process
import time
import sys


# with much help from:
# http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html
# http://docs.tweepy.org/en/v3.4.0/auth_tutorial.html#auth-tutorial
# http://docs.tweepy.org/en/v3.4.0/getting_started.html

# TODO
# catch 503 overload error from twitter, just continue

data_relative_path = "./"
# tweets_location = data_relative_path + "congress_streamed_tweets/"

log = False
log_location = data_relative_path + "bot_log.txt"

# GET THE USER IDS
df = pd.read_csv(data_relative_path + "current_social_media.csv", dtype=str)
user_ids = df.twitter_id
good_user_ids = []
for uid in user_ids:
    try:
        # THIS IS JUST SO WE IGNORE NANS VALUES
        g = int(uid)
        good_user_ids.append(uid)
    except ValueError:
        pass


# testing
# good_user_ids = ["575930104"]

# SETUP AUTHENTICATION
auth = tweepy.OAuthHandler(twitter['consumer_key'], twitter['consumer_secret'])
auth.set_access_token(twitter['access_token'], twitter['access_token_secret'])

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

	def on_status(self, status):
		sj = status._json
		if sj['user']['id_str'] in good_user_ids:
			# with open(tweets_location + sj['user']['id_str'] + '.json', 'a') as f:
			# 	f.write(json.dumps(sj) + '\n')
			
			# # checking out time delays
			# print("received tweet: " + sj['text'])
			# time.sleep(150)
			# RESULT: APPEARS TO CUE TWEETS THAT FIRED WHILE PROCESSING,
			# BUT DOES NOT DO THE PROCESSING AT THE SAME TIME
			# THAT IS, THE TWO PARTS OF EACH TWEET PRINT FOLLOWING EACHOTHER
			# AND IMMEDIATELY AFTER THE SECOND, THE NEXT CUED ONE PRINTS ITS
			# FIRST PART
			# ASYNC PARAMETER APPEARS NOT TO MATTER 
			# (WHICH MAKES SENSE BECAUSE I THINK IT JUST MEANS
			# IT DOESN'T BLOCK AFTER FILTER CALL)
			
			retweeted = 'retweeted_status' in sj.keys()
			if retweeted:
				text = sj['retweeted_status']['text']
			else:
				text = sj['text']

			success, to_tweet = process(text,sj['user']['id_str'],retweeted)

			if success:
				print(sj['text'] + '\n', to_tweet)
				api.update_status("{} https://twitter.com/{}/status/{}".format(to_tweet,sj['user']['screen_name'],sj["id_str"]))
			else:
				print("uncategorized: ", sj['text'])

			if log:
				with open(log_location,'a') as f:
					f.write('stored tweet ' + sj["id_str"] + ' from ' + sj['user']['screen_name'] + " (" + sj['user']['id_str'] + ")\n")
		# print(json.dumps(s, sort_keys=True, indent=4, separators=(',', ': ')))


MyStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = auth, listener=MyStreamListener)
myStream.filter(follow=good_user_ids, async=False)