import facebook
import requests
import MySQLdb


college_name= 'igdtuw'
# search_url= 'https://graph.facebook.com/v2.5/search?q='+college_name+'&type=page&fields=name,likes,id'
# access_token= 'CAACEdEose0cBAFpVzosQ7DrlZAGLM7kVJNT6lfTS7oTs3hBxJFFbpb6BdqUWdqpL4wsrEzJWMh6LZBRPnNkEJ3fWZBZAv8Kqgp4r3ZCxegtnbSWMDNtwGZAtH5ysT7ALDZCcl5UqVTCVSuciTzuUZCTvYyIF1Ql5j2OpZBJ2dGZBpKEUcs0seheJmc59IcZCZA2TZBrAAtFZCgeOEb6QZDZD'
# payload= {'access_token':access_token}
# r= requests.get(search_url,params=payload)
# r= r.json()
# file= open('json_data.txt','w')
# file.write(data)
# print r

db= MySQLdb.connect("localhost","root","ashu","osm")
cursor = db.cursor()
# query= 'insert into test (`id`,`college_name`,`page_id`,`page_name`,`page_likes`,`post_id`,`post_likes`,`post_comment_id`,\
			         # `post_comment_msg`,`post_shares_count`) \
					 # values ('+`count`+',"'+college_name+'","'+page_id+'","'+page_name+'",'+`page_likes`+',"'+post_id+'",'+`likes`+',"'+comment_id+'","'+comment_message+ '",'+`shares_count`+')'
# #			query = "show databases"	
query= "INSERT INTO `osm`.`test` (id) VALUES ('100');"

cursor.execute(query)
db.commit()
#print cursor.fetchone()
# posts_url='https://graph.facebook.com/v2.5/'
# count=100
# pages= r['data']
# payload = {'access_token':access_token}
# shares_count=0 
# likes=0
# no_of_comments=0
# comment_id=''
# comment_message=''

# for post_info in pages:
	# # print posts_url+post_info['id']
	# print 'page info: '
	# page_name= post_info['name']
	# print page_name
	# page_id= post_info['id']
	# print page_id
	# page_likes= post_info['likes']
	# print page_likes
	# r2= requests.get(posts_url+post_info['id']+'?fields=posts.limit(2){likes,comments,shares,message}',params= payload)
	# # print r2
	# # print '\n'
	
	# r2= r2.json()
	# # print r2
	
	# if r2.has_key('posts'):
	    
		# res= r2['posts']
		# res= res['data']
		# # print res
		# # print '\n'
		# for sh in res:
			# print 'post info'
			# post_id= sh['id']
			# print post_id
			# if sh.has_key('message'):
				# post_msg= sh['message']
				# # print post_msg.encode('ascii','ignore')
			# # print post_msg
			# # print sh['shares']
			# if sh.has_key('shares'):
				# shares= sh['shares']
				# shares_count= shares['count']
				# print 'shares count :'
				# print shares_count
			# else:
				# shares=0
				# # print "no value found"
			# #post1= sh['message']
			# #print post1
			# if sh.has_key('likes'):
				# likes= sh['likes']
				# no_of_likes= len(likes)
				# print 'no. of likes: '
				# print no_of_likes
			# else:
				# likes=0
			# if sh.has_key('comments'):
				# comments= sh['comments']
				# comments= comments['data']
				# no_of_comments= len(comments)
				# print 'comments:'
				# print no_of_comments	
				# for cm in comments:
					# comment_id= cm['id']
					# comment_message= cm['message']
			# else:
				# no_of_comments=0
			# query= 'insert into test (`id`,`college_name`,`page_id`,`page_name`,`page_likes`,`post_id`,`post_likes`,`post_comment_id`,\
			         # `post_comment_msg`,`post_shares_count`) \
					 # values ('+`count`+',"'+college_name+'","'+page_id+'","'+page_name+'",'+`page_likes`+',"'+post_id+'",'+`likes`+',"'+comment_id+'","'+comment_message+ '",'+`shares_count`+')'
# #			query = "show databases"	
			# query= 'Insert into test (id) values ('+`count`+')'
			# cursor.execute(query)
		# #	print cursor.fetchone()
db.close()				
