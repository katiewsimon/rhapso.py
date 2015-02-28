# import praw

# r = praw.Reddit(user_agent = 'Hellow world application.')
# sub = r.get_subreddit('music')
# rising = sub.get_rising(limit=5)
# # for post in r.get_subreddit('music'):
# # 	r.get_rising(limit=5)
# print(str(rising))


import urllib2
import json

response = urllib2.urlopen("http://reddit.com/r/music/hot.json?limit=1")
content = json.loads(response.read().decode(response.info().getparam('charset') or 'utf-8'))

for i in content.iteritems():
	p1 = i.iteritems()
	for j in p1.iteritems():
		p2 = j.iteritems()
		for k in p2.iteritems:
			print the_key, " corresponds to ", the_value

	



# items = content.items()

# print items

# [p[0] for p in ]

# for data in content:
# 	for children in data:
# 		for data in children:
# 			print data['author']

# dict_shortcut = data['data']['children']['data']
# kind = data['kind']
# modhash = data['data']['modhash']
# domain = dict_shortcut['domain']
# # subreddit = data['subreddit']
# # title = data['title']

# print domain
# print("kind is ", content.kind, " and name is ",content.data.name)


# def main():

# 	response = urllib2.urlopen("http://reddit.com/api/v1/me/karma.json")
# 	content = json.loads(response)
# 	print "something"
# 	print("kind is ", content.kind, " and name is ",content.data.name)

    # target_file = 'teacherpay_scrubbed_from_url.csv'
    # t = open(target_file,'w')

    # url = 'http://lib.stat.cmu.edu/DASL/Datafiles/teacherpaydat.html'
    # print("Obtaining data from " + 'http://lib.stat.cmu.edu/DASL/Datafiles/teacherpaydat.html')
    
    # y = 0
    
    # try:
    #     response = urllib.request.urlopen(url)
        
    # except:
    #     print("Data not found.")