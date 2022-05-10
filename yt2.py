#%%
from googleapiclient.discovery import build

api_key = "AIzaSyBQEp5c6PevlkRMuC1zLiYd0IPxzyK1YcU"

# creating youtube resource object
youtube = build('youtube', 'v3',
					developerKey= api_key)

# Takes in main query and number of results user is looking for. 
'''def video_identification(q, maxResults): 

    req = youtube.search().list(
        part="id, snippet",
        type='video',
        q=q,
        videoDuration='short',
        videoDefinition='high',
        maxResults=maxResults,
        fields="items(id(videoId), snippet(description))"
    )

#fields param can have all these values about the video:
#fields="items(id(videoId), snippet(publishedAt, channelId, channelTitle, title, description, thumbnails(high)))"

    response = req.execute()
# Print the results

    lt = [] # to store dict values
    vid_id = [] # to store actual vid_id's
    for i in range(len(response['items'])):
        lt.append(response['items'][i]['id'])

    for j in range(len(lt)):
        vid_id.append(lt[j]['videoId'])
        
    return(vid_id) # returns list of video id's

def video_comments(video_id):
	# empty list for storing reply
	replies = []

	# retrieve youtube video results
	video_response=youtube.commentThreads().list(
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
			if replycount>0:
				
				# iterate through all reply
				for reply in item['replies']['comments']:
					
					# Extract reply
					reply = reply['snippet']['textDisplay']
					
					# Store reply is list
					replies.append(reply)

			# print comment with list of reply
			print(comment, replies, end = '\n\n')

			# empty reply list
			replies = []

		# Again repeat
		if 'nextPageToken' in video_response:
			video_response = youtube.commentThreads().list(
					part = 'snippet,replies',
					videoId = video_id
				).execute()
		else:
			break

# Enter video id
video_id = "Enter Video ID"

# Call function
video_comments(video_id)'''

response = youtube.commentThreads().list(
        part='id, replies, snippet',
        maxResults=10,
        textFormat='plainText',
        order='time',
        videoId='QvkQ1B3FBqA'
).execute()
#%%
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

# Will continue until API Quota is maxed out. 10,000 units for a day. Each commentThread call is 1 unit. 
	while response: 
     
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
   
	#Check if the video comment section has a next page... if it does generate a new response with 'pageToken' value. 
		if 'nextPageToken' in response:
			# Regenrate response for the new vid:
			response = youtube.commentThreads().list(
				part=part,
				maxResults=maxResults,
				textFormat=textFormat,
				order=order,
				videoId=videoId,
				pageToken = response['nextPageToken']
			).execute()
		else:
			break

# Finally, return the data back
	return {     
		'Comments': comments,
		'Comment Id':comment_ids,
		'Reply Count': replies,
  		'Likes Count': likes, 
		'Published Date of Comment': published_dates 
		}

	
# %%

# fetches the reply information from a comment video. 

# # To do: 
# Insert below code in the fetch_comment video. As it requires a response to execute for it to work. And since the response is already being executed in fetch_comment, this needs to be a part of that. 

reply_comment = []
reply_posted = []
reply_likes = []
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
print(reply_comment)
print(reply_posted)
print(reply_likes) 
# %%
