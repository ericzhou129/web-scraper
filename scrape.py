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

# STEP 1: Login to the site
payload = {
	"username": "Daik1226",
	"password": "Daik1226",
	"isPersistent": 0
	}

login_url = 'https://connect.just-eat.ca/api/account/login'

s = requests.session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

r = s.post(login_url, data=payload)
print(r.status_code)
MYCOOKIES = r.cookies

# STEP 2: Go to the correct date selection
# Grab the page for a date or a range of dates
date = "17-02-2017"
duration = "1m"
index_page = "3"
request_date_url = "https://partner.just-eat.ca/Orders/OrdersBetweenDates/" + date + "/" + duration + "?pageIndex=" + index_page
result = s.get(request_date_url, cookies=MYCOOKIES)
print(result.status_code)

# STEP 3: using beautifulsoup, compile a list of order links.
# use bs4 to find all order links
result_soup = BeautifulSoup(result.content, 'html.parser')

# Figure out how many index pages there are for a given date range.
# hint: use regular expression to find last index?
# TODO: Check that index 8 is inddeed the last link.
for link in result_soup.find_all(id="PageIndexList"):
    print(link.find_all(href - True)[8])
#loop through all index pages

# on each index page, order links are separated into 'even' and 'odd' links
# loops to find all even and odd order links
# TODO: Turn These into functions
count_even = 0
count_odd = 0
for link in result_soup.find_all(class_= 'odd orderDetailsRow'):
    print(link.a['href'])
    if link.a['href'] != None:
        count_odd+=1

for link in result_soup.find_all(class_= 'even orderDetailsRow'):
    print(link.a['href'])
    if link.a['href'] != None:
        count_even+=1

count = count_odd + count_even
print(count + 'links found in total')
