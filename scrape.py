"""
Outline:
(1)Login into partner.just-eat.ca website
 -- note: the cookie must be passed to every link hereforth.
(2)Input date and selection into the partner home page
ex: https://partner.just-eat.ca/Orders/OrdersBetweenDates/17-02-2017/1m?pageIndex=3
(3)Index all "href" order links for each index page
ex: https://partner.just-eat.ca/Orders/OrderDetail/12936365
(4)For each order link, scrape the order contents
(5)Export data as a csv
"""



import requests
from bs4 import BeautifulSoup

#STEP 1: Login to the site
payload = {
	"username": "Daik1226",
	"password": "Daik1226",
	"isPersistent": 0
	}

login_url = 'https://connect.just-eat.ca/api/account/login'

s = requests.session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

result = s.post(login_url, data=payload)
print(result.status_code)
MYCOOKIES = result.cookies

# result = s.get('https://partner.just-eat.ca/', cookies=MYCOOKIES)
# print(result.status_code)
# print(result.text)

#STEP 2: Go to the correct date selection
#Grab the page for a date or a range of dates
date = "17-02-2017"
request_date_url = "https://partner.just-eat.ca/Orders/OrdersBetweenDates/" + date + "/1m?pageIndex=3"
result = s.get(request_date_url, cookies=MYCOOKIES)
print(result.status_code)

#Function which uses beaufiful soup to find href (order) links and store them into an ____?


#For each index page within a search execute the bs function
