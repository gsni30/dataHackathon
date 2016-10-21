from twython import Twython
import MySQLdb

ACCESS_TOKEN = '2903989381-IJHn1fpnVhnifHSejnLGV4ofP43BVybWfPF0PJb'
ACCESS_SECRET = '3cbuSV5EQmSaE15rThqRYgBEjQvEdRsQyXwKJ0phC82JW'
CONSUMER_KEY = '5OM8YHXtwIVJitYyZRixkI22E'
CONSUMER_SECRET = 'ZCWb4iXEVep5bcBZfQtD4tTFpR3HUVrMJY1viKYlUcDVgJ5ToW'

db= MySQLdb.connect("localhost","root","ashu","osm")
cursor = db.cursor()
count=1
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
arr=['igdtuw','iiitd','iitd','dtu','nsit','igit','dce']
for clg in arr:
	try:
		search_results = twitter.search(q=clg,lang='en' ,count=100)
	except TwythonError as e:
		print e
	#print search_results
	for tweet in search_results['statuses']:
		fav= tweet['favorited']
		t=tweet['entities']
		hashtag=''
		for tags in t['hashtags']:
			h= tweet['text']
			
			for i in h:
				if ord(i)>128:
					
					h= h.replace(i,'')
			hashtag+=(h)

		
		comp_tweet=(tweet['text'])
	
		for i in comp_tweet:
				if ord(i)>128:
					comp_tweet= comp_tweet.replace(i,'')
				
		comp_tweet=comp_tweet.replace("'","")
		comp_tweet=comp_tweet.replace('\"',"")
		comp_tweet=comp_tweet.replace('"',"")
		rt_cnt=tweet['retweet_count']
		is_rtd=tweet['retweeted']
		#user details
		user_arr=tweet['user']
		user_id=user_arr['id_str']
		user_foll=user_arr['followers_count']
		user_friend=user_arr['friends_count']
		user_handle= user_arr['screen_name']
		
		for i in user_handle:
			if ord(i)>128:
				user_handle= user_handle.replace(i,'')
			
			#query= 
		try:
			cursor.execute('insert into twitter_tweet values ('+`count`+',"'+comp_tweet+'",'+`rt_cnt`+','+`is_rtd`+',"'+user_id+'","'+hashtag+'")')
			db.commit()
			query= 'Insert into tweet_user values ("'+user_id+'","'+user_handle+'",'+`user_foll`+','+`user_friend`+')'
			cursor.execute(query)
			db.commit()
			count=count+1
		except:
			pass
		
	# print 'Tweet from @%s Date: %s %s' % (tweet['user']['screen_name'].encode('utf-8'),tweet['created_at'],tweet['retweet_count'])
    # print tweet['text'].encode('utf-8'), '\n'