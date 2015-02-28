import urllib2
import json

class Rhapsopy(object):

	def __init__(self,jsonData):
		self.score = jsonData['score']
#		self.title = jsonData['data']['children']['title']
		self.title_len = len(jsonData['title'])
		self.text_len = len(jsonData['selftext'])
		self.created_utc = jsonData['created_utc']

	# methods that convert json input to output usable for music
	def score_to_music(): 
		return self.score

	def title_len_to_pitch():
		pitch = int(self.title_len % 7)
		return pitch

	def text_len_to_music():
		return self.text_len	

	def time_to_music():
		return self.created_utc


	def to_csv_row():
		row = ""
		row += score_to_music, ","
		row += title_len_to_music, ","
		row += text_len_to_music, ","
		row += time_to_music
	

def main():

	target_file = 'reddit_to_music.csv'
	t = open(target_file,'w')
	# subreddit = "music"
	# sortby = "hot"
	# limit = "1"

	# try: 
	response = urllib2.urlopen("http://reddit.com/r/music/hot.json?limit=3")	
	jsonData = json.loads(response.read())#.decode(response.info().getparam('charset') or 'utf-8')
	# except: 
	# 	print("Data not found. :(")

	children = jsonData['data']['children']

	output_list = ""

	for child_data in children:
		child = Rhapsopy(child_data['data']) 
		output_list += child.to_csv_row + '\n'

	t.write(output_list)

	t.close()
        print( "\nFile created. %d records written. " % (i) )

main()

	# def get_score(self,subreddit,sortby,limit):
		
	# 	else:
	# 		content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
			
	# 		children = content['data']['children']
			
	# 		for child in children:
	# 			child_data = child['data']

	# 	return: child_data['score']
		
	# def get_title(self,subreddit,sortby,limit):
	# 	try: 
	# 		response = urllib2.urlopen("http://reddit.com/r/music/hot.json?limit=3")	
	# 		content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
	# 	except: 
	# 		print("Data not found. :(")
	# 	else:
	# 		content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
			
	# 		children = content['data']['children']
			
	# 		for child in children:
	# 			child_data = child['data']

	# 	return: child_data['title']
	
	# def get_title_len(self,subreddit,sortby,limit):
	# 	try: 
	# 		response = urllib2.urlopen("http://reddit.com/r/music/hot.json?limit=3")	
	# 		content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
	# 	except: 
	# 		print("Data not found. :(")
	# 	else:
	# 		content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
			
	# 		children = content['data']['children']
			
	# 		for child in children:
	# 			child_data = child['data']

	# 	return: len(child_data['title'])

	# def get_text_len(self,subreddit,sortby,limit):
	# 	try: 
	# 		response = urllib2.urlopen("http://reddit.com/r/music/hot.json?limit=3")	
	# 		content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
	# 	except: 
	# 		print("Data not found. :(")
	# 	else:
	# 		content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
			
	# 		children = content['data']['children']
			
	# 		for child in children:
	# 			child_data = child['data']

	# 	return: len(child_data['selftext']

	# def get_created_utc(self,subreddit,sortby,limit):
	# 	try: 
	# 		response = urllib2.urlopen("http://reddit.com/r/music/hot.json?limit=3")	
	# 		content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
	# 	except: 
	# 		print("Data not found. :(")
	# 	else:
	# 		content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
			
	# 		children = content['data']['children']
			
	# 		for child in children:
	# 			child_data = child['data']

	# 	return: child_data['created_utc']

	


