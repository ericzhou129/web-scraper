import requests
from bs4 import BeautifulSoup


payload = {
    "username": "Daik1226",
    "password": "Daik1226",
    "isPersistent": 0
}


login_url = 'https://connect.just-eat.ca/api/account/login'
s = requests.session()
s.headers[
    'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
r = s.post(login_url, data=payload)
print('the status of the login is:' + str(r.status_code))
MYCOOKIES = r.cookies

# initiate link
order_url = 'https://partner.just-eat.ca/Orders/OrderDetail/13101538'
result = s.get(order_url, cookies=MYCOOKIES)
print('status of page: ' + str(result.status_code))
result_soup = BeautifulSoup(result.content, 'html.parser')

# new approach to this problem, scan the tr in each table to fill a row
tables = (result_soup.find_all('table', {'width': '600'})[1])
for item in tables:
    print (item)
    print('')
