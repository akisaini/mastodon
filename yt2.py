# %%
# Requirements:
# Python 2.7 or Python 3.5+
# The pip package management tool
# The Google APIs Client Library for Python
# pip install --upgrade google-api-python-client
# The google-auth-oauthlib and google-auth-httplib2 libraries for user authorization
# pip install --upgrade google-auth-oauthlib google-auth-httplib2

from googleapiclient.discovery import build

api_key = "AIzaSyBQEp5c6PevlkRMuC1zLiYd0IPxzyK1YcU"

# creating youtube resource object
youtube = build('youtube', 'v3',
                developerKey=api_key)


request = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    id='GTr28z9tp7s'
)
response = request.execute()

# %%
# Takes in a simple query and number of results the user is looking for.


def video_identification(q, maxResults):
    # # Your request can also use the Boolean NOT (-) and OR (|) operators to exclude videos or to find videos that are associated with one of several search terms. For example, to search for videos matching either "boating" or "sailing", set the q parameter value to boating|sailing. Similarly, to search for videos matching either "boating" or "sailing" but not "fishing", set the q parameter value to boating|sailing -fishing.

    # Uses the search function to fetch VideoId's - present in snippet.
    # We can add location/Location Radius/Region Code here!
    # Video duration: any/long/medium/short

    # to store video id's
    vid_id = []

    response = youtube.search().list(
        part="snippet",
        type='video',
        q=q,
        order='date',
        videoDuration='medium',
        maxResults=maxResults  # 0 to 50 inclusive
    ).execute()

    for item in response['items']:
        videoid = item['id']['videoId']
        vid_id.append(videoid)

    return vid_id  # returns list of video id's

# %%
# fetches video statistics like views since the release, likes,  dislikes and comments.
# Also provides content details like dimension, definition, caption(T/F) and whether content is licensed or not. 
# Pass in videoId and get results:

# In an ideal scenarion, below function should be executed first to gather preliminary information about the video. And then comments and replies should be fetched. 

def get_vid_stats(videoId):
    # This function needs a request call
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=videoId
    )

    response = request.execute()
    for item in response['items']:
        title = item['snippet']['title']
        description = item['snippet']['description']
        statistics = item['statistics']
        contentDetails = item['contentDetails']
        # Thumbnails? do we need them?

        return {
            'Video Title': title,
            'Video Description': description,
            'Video Statistics': statistics,
            'More Content Details': contentDetails
        }
        
# Below function is just for fetching the description section of the video and putting it in a txt file. - To snatch links.         
def get_vid_description(videoId):
    # This function needs a request call
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=videoId
    )

    response = request.execute()
    for item in response['items']:
        description = item['snippet']['description']
      
    # Creates a new file: description_file here'  
    f = open('description_file', 'w')
    f.write(description)
        
    return {
            'Video Description': description
    }        

# %%
# Use regex to fetch links from the file
import os
import re
def get_desc_links(filename):
# Load the file:
    with open(filename) as f:
        contents = f.read()

    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', contents)
    return urls
#%%

'''
Create method for running the vid_identification on loop on the get_vid_description. 
Above should run all maxresults videoIds on the get_vid_description. If mentioned 50(max) should get back
50 queries.(not hard.)Next, it should take all videoId from the output and run it on the get_vid_description.
This will generate a huge video description text file, on which the regex method will be executed to get
links back. 

This all can be executed in one go just by getting the search query(q) and maxresults from the user
in the UI. 
Another option is to just feed in one videoId in the UI and get back the links for that particular vid. 

These are just the description links. 

Along with get_vid_descriptions, another part would be to run get_comments and store the info in another/same
file. 
'''


def video_comments(video_id):
    # empty list for storing reply
    replies = []

    # retrieve youtube video results
    video_response = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id
    ).execute()

    # iterate video response
    while video_response:

        # extracting required info
        # from each result object
        for item in video_response['items']:

            # Extracting comments
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']

            # counting number of reply of comment
            replycount = item['snippet']['totalReplyCount']

            # if reply is there
            if replycount > 0:

                # iterate through all reply
                for reply in item['replies']['comments']:

                    # Extract reply
                    reply = reply['snippet']['textDisplay']

                    # Store reply is list
                    replies.append(reply)

            # print comment with list of reply
            print(comment, replies, end='\n\n')

            # empty reply list
            replies = []

        # Again repeat
        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(
                part='snippet,replies',
                videoId=video_id
            ).execute()
        else:
            break


# Enter video id
video_id = "Enter Video ID"

# Call function
video_comments(video_id)


# %%
response = youtube.commentThreads().list(
    part='id, replies, snippet',
    maxResults=30,
    textFormat='plainText',
    order='time',
    videoId='lSowC-w4aFY'
).execute()
# %%
# stores comment information from a video. VideoID and MaxResults are required parameters. Rest are optional, set already.


def fetch_comments(videoId, maxResults, part='id, replies, snippet',  textFormat='plainText', order='time'):
    # Generate response.
    response = youtube.commentThreads().list(
        part=part,
        maxResults=maxResults,
        textFormat=textFormat,
        order=order,
        videoId=videoId
    ).execute()

# create empty list to store info.
    comments = []
    comment_ids = []
    replies = []
    likes = []
    published_dates = []
    reply_comment = []
    reply_posted = []
    reply_likes = []
# Will continue until API Quota is maxed out or Comments run out. 10,000 units for a day. Each commentThread call is 1 unit.
    while response:

       # Will only get the comments.
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
            comment_id = item['snippet']['topLevelComment']['id']
            comment_ids.append(comment_id)
            reply_count = item['snippet']['totalReplyCount']
            replies.append(reply_count)
            like_count = item['snippet']['topLevelComment']['snippet']['likeCount']
            likes.append(like_count)
            comment_published = item['snippet']['topLevelComment']['snippet']['publishedAt']
            published_dates.append(comment_published)

 # Will get the replies (fetches the reply information from a comment video)
        for item in response['items']:
            if item['snippet']['totalReplyCount'] >= 1:
                for i in range(len(item['replies']['comments'])):
                    comment = item['replies']['comments'][i]['snippet']['textOriginal']
                    reply_comment.append(comment)
                    publish_date = item['replies']['comments'][i]['snippet']['publishedAt']
                    reply_posted.append(publish_date)
                    like_count = item['replies']['comments'][i]['snippet']['likeCount']
                    reply_likes.append(like_count)
            else:
                pass

    # Check if the video comment section has a next page... if it does generate a new response with 'pageToken' value.
        if 'nextPageToken' in response:
            # Regenrate response for the new vid:
            response = youtube.commentThreads().list(
                part=part,
                maxResults=maxResults,
                textFormat=textFormat,
                order=order,
                videoId=videoId,
                pageToken=response['nextPageToken']
            ).execute()
        else:
            break

# Finally, return the data back
    return {
        'Comments': comments,
        'Comment Id': comment_ids,
        'Reply Count': replies,
        'Likes Count': likes,
        'Published Date of Comment': published_dates,
        'Replies': reply_comment,
        'Published Date of Reply': reply_posted,
        'Likes on Reply': reply_likes,
        # below includes comments + replies.
        'Number of Total Comments': len(comment_ids)+len(reply_comment)
    }


# %%
