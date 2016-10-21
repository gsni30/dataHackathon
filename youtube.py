import requests
import MySQLdb
college_name= 'iitd'
url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&q=iiitd%7Ciiit+delhi&fields=items%2Fid'
db= MySQLdb.connect("localhost","root","ashu","osm")
cursor = db.cursor()
payload= {'key':'AIzaSyC9r1X_kPg9He3Y7uGDMrbflYp4BJVAZQY'}
res= requests.get(url,params=payload)
r= res.json()
r= r['items']
video_ids=''
for vi in r:
	id = vi['id']
	if id.has_key('videoId'):
		video_ids= video_ids+','+id['videoId']
		# print id['videoId']
# print video_ids

video_info_url= 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id='+video_ids+'&fields=items(id%2Cstatistics)'
res = requests.get(video_info_url,params=payload)
r= res.json()
r= r['items']

for j in r:
	videoId= j['id']
	j= j['statistics']
	viewCount=0
	likeCount=0
	dislikeCount=0
	favoriteCount=0
	commentCount=0
	if j.has_key('viewCount'):
		viewCount=int(j['viewCount'])
	if j.has_key('likeCount'):
		likeCount= int(j['likeCount'])
	if j.has_key('dislikeCount'):
		dislikeCount= int(j['dislikeCount'])
	if j.has_key('favoriteCount'):
		favoriteCount= int(j['favoriteCount'])
	if j.has_key('commentCount'):
		commentCount= int(j['commentCount'])
	# print (j['dislikeCount'])+'  '+j['favoriteCount'] 
	query = 'insert into youtube_data(clg_id,video_id,viewCount,likeCount,dislikeCount,favoriteCount,commentCount) values ('+`3`+',"'+videoId+'",'+`viewCount`+','+`likeCount`+','+`dislikeCount`+','+`favoriteCount`+','+`commentCount`+')'
	cursor.execute(query)
	db.commit()
#print r
# 9rVAZB-5M5A,f4xPaE5PmUk,bJ_mdpAFRvg
#ACBNflWg25s,TBk4Z4q1fEg,BNw8jDSXFNU
