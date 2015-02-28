import urllib2
import json

subreddit = "music"
sortby = "hot"
limit = "1"

class rhapsopy(object):

	def get_reddit_data(subreddit,sortby,limit):
		

def main():
	target_file = 'reddit_data_for_music'
	t = open(target_file,'w')
	try: 
		response = urllib2.urlopen("http://reddit.com/r/music/hot.json?limit=3")	
		content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
	except: 
		print("Data not found. :(")
	else:
		content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
		children = content['data']['children']
		heading = 'score,title,title_len,text_len,created_utc'
		for child in children:
			child_data = child['data']
			
							

			score = child_data['score']
			
			title = child_data['title']
			title_len = len(child_data['title'])
			text_len = len(child_data['selftext'])
			created_utc = child_data['created_utc']
			
			new_line = ''
print "score is: ", score 
print "title is: ", title
print " title length is: ", title_len 
print " text length is: " , text_len
print " created_utc is: ", created_utc

