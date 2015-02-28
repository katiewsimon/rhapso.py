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
	row = ""

	for child_data in children:
		child = Rhapsopy(child_data['data']) 
		row = str(child.to_csv_row)
		print(row)
		output_list = output_list + row + '\n'

	t.write(output_list)

	t.close()

main()
