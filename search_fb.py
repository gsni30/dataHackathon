import facebook
import requests
import MySQLdb
import unirest

# #### db connection ####
db= MySQLdb.connect("localhost","root","ashu","osm")
cursor = db.cursor()
# #######################

clg_name='dtu'
query =('SELECT clg_id FROM fb_clg WHERE clg_name="'+clg_name+'"')
cursor.execute(query)
row = cursor.fetchone()
print row[0]
	
search_url= 'https://graph.facebook.com/v2.5/search?q='+clg_name+'&type=page&fields=name,likes,id'
access_token= 'EAACEdEose0cBAHZCsBGLX2LJFjrhb5JU9ala5jIlcaARh9LmgL2qQbor3BgGJ5kgE26pg1Ndbtk12uazkqUvDDlBWmFgTDpn7FmshmPy3ZAo5quE0HA9nKXNFAOirwMKrA6ZCGfTK5ejAX8PgZCynCmu2YNh7OCf87ZAM4nweFwZDZD'
payload= {'access_token':access_token}
r= requests.get(search_url,params=payload)
r= r.json()
posts_url='https://graph.facebook.com/v2.5/'
count=871
pages= r['data']
payload = {'access_token':access_token}
shares_count=0 
likes=0
no_of_comments=0
chk_var2=0
chk_var=0
comment_id=''
comment_message=''
arr=['153864514811448','231387990211572','914910265264388']
for post_info in pages:

	print '----------------------------------------------------------'
	print 'page info: '
	page_name= post_info['name']
	print page_name.replace("'", "")
	page_name=page_name.replace("'", "")
	page_name=page_name.replace("\"", "")
	page_id= post_info['id']
	if page_id not in arr :
		print page_id
		page_likes= post_info['likes']
		print page_likes
		q1="INSERT INTO fb_page VALUES ('"+page_id+"','"+page_name+"',"+`page_likes`+","+`int(row[0])`+")"
		cursor.execute(q1)
		db.commit()	
		r2= requests.get(posts_url+post_info['id']+'?fields=posts.limit(10){likes,comments,shares,message}',params= payload)
		r2= r2.json()
		# print r2

		if r2.has_key('posts'):
			ngcnt=0
			necnt=0
			pscnt=0
			status='none'
			cmmnt_score=0
			res= r2['posts']
			res= res['data']
			print count
			print ',,,\n'
			for sh in res:
				print 'post info'
				post_id= sh['id']
				file= open('Hackathon/'+clg_name+'_'+post_id+'.txt','w')
				print post_id
				if sh.has_key('message'):
					post_msg= sh['message']
					post_msg=post_msg.translate('"\'')
					file.write("{ \"message\":\"")
					file.write(post_msg.encode("utf-8"))
					file.write("\"\n")
					chk_var=1

				if sh.has_key('shares'):
					shares= sh['shares']
					shares_count= shares['count']
					print 'shares count :'
					print shares_count
				else:
					shares=0

				if sh.has_key('likes'):
					likes= sh['likes']
					likes= likes['data']
					no_of_likes= len(likes)
					print 'no. of likes: '
					print no_of_likes
				else:
					no_of_likes=0
				if sh.has_key('comments'):
					comments= sh['comments']
					comments= comments['data']
					no_of_comments= len(comments)
					print 'comments:'
					print no_of_comments
					score=float(0)
					
					for cm in comments:
						comment_id= cm['id']
						comment_message= cm['message']
						comment_message=comment_message.translate('"\'')
						response = unirest.post("https://twinword-sentiment-analysis.p.mashape.com/analyze/",
						headers={"X-Mashape-Key": "C4sjFq8Rkjmshcc4qpR4TroNZIzup1LQHf2jsnJnnIkE23mKhb","Content-Type": "application/x-www-form-urlencoded","Accept": "application/json"},
						params={"text":"\""+comment_message+"\""}
						)
						score=float(response.body['ratio'])
						if score<0 :
							ngcnt+=1
						if score>0 :
							pscnt+=1
						if score==0 :
							necnt+=1
		
						query= 'insert into fb_comment values ("'+post_id+'",'+`score`+')'
						cursor.execute(query)
						db.commit()
						if chk_var==1:
							file.write(",")
						if chk_var2!=1:
							file.write("\"comment\": [\"")
						else :
							file.write(",[\"")
						chk_var2=1
						file.write(comment_message.encode("utf-8"))
						file.write("\"]")
				else:
					no_of_comments=0
				if chk_var==1 or chk_var2==1 :
							file.write("}")
				if no_of_comments>0:
					if ngcnt > pscnt :
						if ngcnt > necnt :
							status='negative'
							cmmnt_score=(ngcnt/no_of_comments)*100
						else :
							status='neutral'
							cmmnt_score=(necnt/no_of_comments)*100
					else :
						if pscnt > necnt :
							status = 'positive'
							cmmnt_score=(pscnt/no_of_comments)*100
						else :
							status = 'neutral'
							cmmnt_score=(necnt/no_of_comments)*100
					
				file.close()
				query= 'insert into fb_post values ("'+page_id+'",'+`count`+','+`no_of_likes`+','+`shares_count`+','+`necnt`+','+`pscnt`+','+`necnt`+',"'+status+'",'+`cmmnt_score` +')'
				cursor.execute(query)
				count=count+1
				db.commit()		

				#	print cursor.fetchone()
db.close()	