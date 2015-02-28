import urllib2
import json

subreddit = "music"
sortby = "hot"
limit = "1"

response = urllib2.urlopen("http://reddit.com/r/music/hot.json?limit=3")
content = json.loads(response.read()) #.decode(response.info().getparam($

children = content['data']['children']
for child in children:
        child_data = child['data']
        score = child_data['score']
        title = child_data['title']
        title_len = len(child_data['title'])
        text_len = len(child_data['selftext'])
        created_utc = child_data['created_utc']

print "score is: ", score
print "title is: ", title
print " title length is: ", title_len
print " text length is: " , text_len
print " created_utc is: ", created_utc