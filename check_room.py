import requests

url = ''

headers = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}

payload = {
    
  }


res = requests.post(url,data= payload)
if(res.text):
    print(res.text)
else:
    print('no avialable')

