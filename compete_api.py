import requests
import shutil

r = requests.get('https://apps.compete.com/sites/compete.com/trended/uv/?apikey=e1cec49c4d6a522d74076638866a9aee&latest=6&format=png', stream=True)
print r;
if r.status_code == 200:
    with open('aaaile.png', 'wb') as f:
        #r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)    

# r= requests.get('https://apps.compete.com/sites/compete.com/trended/uv/?apikey=e1cec49c4d6a522d74076638866a9aee&latest=6&format=png')

# print r
#http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
#https://developer.compete.com/available-metrics/
#https://developer.compete.com/documentation/
