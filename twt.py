#%%
import tweepy
import csv
# %%
# Twitter Developer keys: 
consumer_key = '3X2sItg0hqlYgiYRI4YdCMFZP'
consumer_key_secret = 'dnf20RgVDMmjOSJyQfPFoMO5esjbOBaTIpMR3yA8WMeusDpL5j'
access_token = '1142488668-YYRzZsk0o5hxodbgyx3bJBNV2PFsEFbPvZnfNtW'
access_token_secret = 'dSUkjQ2l1pGtuICzYo2KHQ6HPqVxZqIZ5dQdJfNuuvCHC'
#%%
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# %%
search_words = "Dogs" #enter your words -> This can be hastags, @mentions or simple text
# Below avoids the retweets from the extraction. 
new_search = search_words + " -filter:retweets"
# %%
#csvFile = open('tweets', 'a')
#csvWriter = csv.writer(csvFile)

fetched_tweets = api.search_tweets(new_search, maxResults = 10)
   # parsing tweets one by one
print(fetched_tweets)



#%%

# %%
