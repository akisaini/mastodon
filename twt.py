#%%
import tweepy
# %%
# Twitter Developer keys: 
consumer_key = '3X2sItg0hqlYgiYRI4YdCMFZP'
consumer_key_secret = 'dnf20RgVDMmjOSJyQfPFoMO5esjbOBaTIpMR3yA8WMeusDpL5j'
access_token = '1142488668-YYRzZsk0o5hxodbgyx3bJBNV2PFsEFbPvZnfNtW'
access_token_secret = 'dSUkjQ2l1pGtuICzYo2KHQ6HPqVxZqIZ5dQdJfNuuvCHC'
#%%
auth = tweepy.OAuthhandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# %%
