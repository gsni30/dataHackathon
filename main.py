import facebook
import requests


search_url= 'https://graph.facebook.com/v2.5/search'
college_name= 'igdtuw'
access_token= 'EAACEdEose0cBAO7n6rrtns9pQaMabFOmBdPYeTppIZAtTavdexbLL0Hkf1HvX9kRO7TYOuGkB3ZAUYsbV3wJ95KSFDFQZCirGBoek1Hy7cDM4911VNUl2AX9juDAOC0ZBM5ZA8rqPfGS16C7tn4bCYYvZBzVywYKIj2dY1ZASsz0gZDZD'
payload= {'q':college_name,'type':'page','access_token':access_token}
r= requests.get(search_url,params=payload)
r= r.json()
# file= open('json_data.txt','w')
# file.write(data)
#print r
access_token= 'EAACEdEose0cBAO7n6rrtns9pQaMabFOmBdPYeTppIZAtTavdexbLL0Hkf1HvX9kRO7TYOuGkB3ZAUYsbV3wJ95KSFDFQZCirGBoek1Hy7cDM4911VNUl2AX9juDAOC0ZBM5ZA8rqPfGS16C7tn4bCYYvZBzVywYKIj2dY1ZASsz0gZDZD'

posts_url='https://graph.facebook.com/v2.5/615777508476910'

#pages= r['data']
payload = {'fields':{'posts':{'likes','comments','shares'}},'access_token':access_token}

#payload = {'access_token':access_token}

r2= requests.get(posts_url,params=payload)
	# print r2
	# print '\n'

r2= r2.json()
print r2
# res= r2['posts']
# res= res['data']
	# print res
	# print '\n'
# for sh in res:
	# print sh
	# shares= sh['shares']
	# shares_count= shares['count']
	# print 'shares count :'+shares_count
	# print '\n'
	# print '\n'
	# likes= sh['likes']
	# no_of_likes= len(likes)
	# print no_of_likes
	# print '\n'
	# comments= sh['comments']
	# comments= comments['data']
	# no_of_comments= len(comments)
	# print no_of_comments
	# print '\n'

	
# print r.text

