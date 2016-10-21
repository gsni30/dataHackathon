from twython import Twython

ACCESS_TOKEN = '2903989381-IJHn1fpnVhnifHSejnLGV4ofP43BVybWfPF0PJb'
ACCESS_SECRET = '3cbuSV5EQmSaE15rThqRYgBEjQvEdRsQyXwKJ0phC82JW'
CONSUMER_KEY = '5OM8YHXtwIVJitYyZRixkI22E'
CONSUMER_SECRET = 'ZCWb4iXEVep5bcBZfQtD4tTFpR3HUVrMJY1viKYlUcDVgJ5ToW'

#payload={'consumer_key':CONSUMER_KEY,'consumer_key,'access_token':ACCESS_TOKEN}
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

r= twitter.search(q='python')

# url= 'https://api.twitter.com/1.1/users/search.json?q=Twitter%20API&page=1&count=3'

# r= requests.get(url,params=payload)
# r= r.json()
# print r