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

# print(result_soup.find_all(id='OrderDetailSection'))

# print(result_soup.find_all("td", {'width': '200'}))
print(result_soup.find_all("td", {'width': '200', 'valigh': 'top'}))

OrderNameList = (result_soup.find_all("td", {'width': '200', 'valigh': 'top'}))
for item in OrderNameList:
    if item == 'None':
        break
    item_list = []
    item_list.append(item.find('b').string)
print(item_list)

OrderPiecesList = (result_soup.find_all("strong"))
for item in OrderPiecesList:
    item_list = []
    item_list.append(item.string)
print(item_list)

OrderDescriptionList = (result_soup.find_all("td", {'width': '185'}))
for item in OrderDescriptionList:
    item_list = []
    item_list.append(item.find('b').string)
print(item_list)

OrderUnitPriceList = (result_soup.find_all("td", {'width': '85'}))
for item in OrderUnitPriceList:
    item_list = []
    item_list.append(item.find('font').string)
print(item_list)

OrderTotalPriceList = (result_soup.find_all("td", {'nowrap': 'nowrap'}))
for item in OrderTotalPriceList:
    item_list = []
    item_list.append(item.find('font').string)
print(item_list)
