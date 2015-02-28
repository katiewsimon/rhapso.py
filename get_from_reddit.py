import urllib2
import json

class Rhapsopy(object):
	
	try: 
		response = urllib2.urlopen("http://reddit.com/r/music/hot.json?limit=3")	
		jsonData = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
	except: 
		print("Data not found. :(")


	def __init__(self,jsonData):
		self.score = jsonData['data']['children']['score']
#		self.title = jsonData['data']['children']['title']
		self.title_len = len(jsonData['data']['children']['title']
		self.text_len = len(jsonData['data']['children']['selftext']
		self.created_utc = jsonData['data']['children']['created_utc']

		#more
		# self.subreddit = 'music'
		# self.sortby = 'hot'
		# limit = 1

	output_list = []


	# methods that convert json input to output usable for music
	def score_to_music: 
		return self.score

	def title_len_to_music:
		return self.title_len

	def text_len_to_music:
		return self.text_len	

	def time_to_music:
		return self.created_utc


	def to_csv_row:
		row = ""
		row += score_to_music, ","
		row +=
	

	def get_score(self,subreddit,sortby,limit):
		
		else:
			content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
			
			children = content['data']['children']
			
			for child in children:
				child_data = child['data']

		return: child_data['score']
		
	def get_title(self,subreddit,sortby,limit):
		try: 
			response = urllib2.urlopen("http://reddit.com/r/music/hot.json?limit=3")	
			content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
		except: 
			print("Data not found. :(")
		else:
			content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
			
			children = content['data']['children']
			
			for child in children:
				child_data = child['data']

		return: child_data['title']
	
	def get_title_len(self,subreddit,sortby,limit):
		try: 
			response = urllib2.urlopen("http://reddit.com/r/music/hot.json?limit=3")	
			content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
		except: 
			print("Data not found. :(")
		else:
			content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
			
			children = content['data']['children']
			
			for child in children:
				child_data = child['data']

		return: len(child_data['title'])

	def get_text_len(self,subreddit,sortby,limit):
		try: 
			response = urllib2.urlopen("http://reddit.com/r/music/hot.json?limit=3")	
			content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
		except: 
			print("Data not found. :(")
		else:
			content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
			
			children = content['data']['children']
			
			for child in children:
				child_data = child['data']

		return: len(child_data['selftext']

	def get_created_utc(self,subreddit,sortby,limit):
		try: 
			response = urllib2.urlopen("http://reddit.com/r/music/hot.json?limit=3")	
			content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
		except: 
			print("Data not found. :(")
		else:
			content = json.loads(response.read()).decode(response.info().getparam('charset') or 'utf-8'
			
			children = content['data']['children']
			
			for child in children:
				child_data = child['data']

		return: child_data['created_utc']

	


