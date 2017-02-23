import requests
# from bs4 import BeautifulSoup

payload = {
	"username": "Daik1226",
	"password": "Daik1226",
	"isPersistent": 0
	}

#login_url= "https://connect.just-eat.ca/login?client_id=RappsOrigPartnerCentre&response_type=code&redirect_uri=https:%2F%2Fpartner.just-eat.ca%2Fsignin-jeconnect&state=Vch_AK7_0-moIIZIe84tKXdDhdDJBMd2JKAxNYiS5KA2Ax9s7YhMf7wmeFTPItHRfZIPpecD7YjZIY8N7ZghkHTIFZxttdDhjTR5TDAvtCf32lMGoY4SLlBTMc6qc46wusjX3jKemq2IITRmMBkxzVykaxludg03bUnI2xD1JwwcJqrzOrfRP1yDWQZ40B8gKGIe--gXWiDV-z16IOGvbv0wGO8"
login_url = 'https://connect.just-eat.ca/api/account/login'

s = requests.session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
#r = requests.get(login_url)

result = s.post(login_url, data=payload)
print(result.status_code)
MYCOOKIES = result.cookies

result = s.get('https://partner.just-eat.ca/', cookies=MYCOOKIES)
print(result.status_code)
