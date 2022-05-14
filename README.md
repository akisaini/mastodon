There are two aspects to this project. 
To get data from:
# mastodon
Working with the Mastodon social network API. 

The above task is currently on hold while the Youtube API is being used to get the required data. 

For the Youtube API to function properly, the prerequesites are mentioned below: 

Requirements:
 Python 2.7 or Python 3.5+
 The pip package management tool
 The Google APIs Client Library for Python
 pip install --upgrade google-api-python-client
 The google-auth-oauthlib and google-auth-httplib2 libraries for user authorization
 pip install --upgrade google-auth-oauthlib google-auth-httplib2

oauth is not needed at the moment since the project is not going live yet. 

1) Once you make sure the above are installed, you will have to create a google developer account to get access to an API key. 
https://console.cloud.google.com/

2) This is the link for the youtube data API which is used to collect all the data: https://developers.google.com/youtube/v3/docs/
This link includes the documentation for the methods used.

3) The file yt2.py is the main file containing all the methods to get the data. 

4) Comments throughout the file yt2.py help  explaining the methods. 

--------------------------------------------------------------------

At present, we are able to fetch all the links from a video in it's description section and store that in a file. 

Next task is to get the links from the comments section of the same video and store it in a seperate column in a dataframe. This way, there will be clear differentiation between links that are from the description section and one's that are from the comments and replies section. 

From trial and error, it has been found that description links are usually way more than links in the comments and replies section. 

--------------------------------------------------------------------

