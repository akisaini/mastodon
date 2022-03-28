'''# Register your app! This only needs to be done once. Uncomment the code and substitute in your information.

from mastodon import Mastodon

'''
Mastodon.create_app(
     'pytooterapp',
     api_base_url = 'https://mastodon.social',
     to_file = 'pytooter_clientcred.secret'
)
'''

# Then login. This can be done every time, or use persisted.'''

from mastodon import Mastodon

mastodon = Mastodon(
    client_id = 'F5ThGzIb6ROI4AJ7dYltZvCFi3QASavJXqVc0gt2Tdk',
    api_base_url = 'https://mastodon.social'
)
mastodon.log_in(
    'akshatsaini1@gmail.com',
    'password@@@@',
    to_file = 'pytooter_usercred.secret'
)

# To post, create an actual API instance.

from mastodon import Mastodon

mastodon = Mastodon(
    access_token = 'CTtR4HAzIqDYZF2IyRUY4E22qjRihhypaeHDznB8vwg',
    api_base_url = 'https://mastodon.social'
)
mastodon.toot('Tooting from python using #mastodonpy Yay !') 
