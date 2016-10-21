# tryst - https://developer.similarweb.com/
import requests

r=requests.get('http://api.similarweb.com/Site/cnn.com/v1/visits?gr=daily&start=9-2013&end=5-2014&md=false&Format=JSON&UserKey=#')