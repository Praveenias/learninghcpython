import requests

url = 'http://127.0.0.1:8000/api/v1/';

api_key = {'apiKey':'abcde'}
authToken = '6|DYtyvxLFECd40Klw3gBZBeBzncQpxpad6ZVvwSws'

headers = {
        'Authorization': 'Bearer ' + authToken,
        'Content-Type': 'application/json'
}

#res_access_token = requests.get(url+'access-token',api_key)

#print(res_access_token.json()["data"])

res = requests.get(url+'licenses',headers=headers)
print(res.json())



