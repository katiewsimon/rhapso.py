import urllib2
import json

class Child(object):

	def __init__(self,jsonData):
		self.score = jsonData['score']
		print self.score
		self.title_len = len(jsonData['title'])
		self.text_len = len(jsonData['selftext'])
		self.created_utc = jsonData['created_utc']

	# methods that convert json input to output usable for music
	def score_to_instrument(self):
		self.instrument = int(self.score % 5)
		return self.instrument

	def title_len_to_pitch(self):
		self.pitch = int(self.title_len % 7)
		return self.pitch

	def text_len_to_duration(self):
		dur = int(self.text_len % 4)
		if dur == 0:
			dur = "whole note"
		elif dur == 1:
			dur = "quarter note"
		elif dur == 2:
			dur = "half note"
		elif dur == 3:
			dur = "dotted half note"
		return dur	

	def time_to_music(self):
		return self.created_utc

	# adds int input to a row in a csv 
	def to_csv_row(self):
		row = ""
		row = row + str(self.score_to_instrument()) + ","
		row = row + str(self.title_len_to_pitch()) + ","
		row = row + str(self.text_len_to_duration()) + ","
		row = row + str(self.time_to_music())
	

def main():

	target_file = 'reddit_to_music.csv'
	t = open(target_file,'w')

	# possible to customize URL in future:
	subreddit = "music"
	sortby = "hot"
	limit = "1"

	# get json data from reddit
	response = urllib2.urlopen("http://reddit.com/r/music/hot.json?limit=3")	
	jsonData = json.loads(response.read())#.decode(response.info().getparam('charset') or 'utf-8')

	# navigate to useful data
	children = jsonData['data']['children']

	output_list = ""
	row = ""

	# write transformed 
	for child_data in children:
		child = Child(child_data['data']) 
		row = str(child.to_csv_row())
		print(row)
		output_list = output_list + row + '\n'

	t.write(output_list)

	t.close()

main()
