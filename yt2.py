from googleapiclient.discovery import build

api_key = "AIzaSyBQEp5c6PevlkRMuC1zLiYd0IPxzyK1YcU"

	# creating youtube resource object
youtube = build('youtube', 'v3',
					developerKey= api_key)

# Takes in main query and number of results user is looking for. 
def video_identification(q, maxResults): 

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
video_comments(video_id)
