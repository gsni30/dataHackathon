import unirest

# These code snippets use an open-source library. http://unirest.io/python
response = unirest.post("https://twinword-sentiment-analysis.p.mashape.com/analyze/",
  headers={
    "X-Mashape-Key": "C4sjFq8Rkjmshcc4qpR4TroNZIzup1LQHf2jsnJnnIkE23mKhb",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  },
  params={
    "text": "He was a bad man, really ugly."
  }
)

#res=response.json()
print response.body
print '\n'
print response.body['ratio']


# query= 'Insert into test ( id) values ('+`count`+')'