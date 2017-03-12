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
order_url = 'https://partner.just-eat.ca/Orders/OrderDetail/12907379'
result = s.get(order_url, cookies=MYCOOKIES)
print('status of page: ' + str(result.status_code))
result_soup = BeautifulSoup(result.content, 'html.parser')

# print(result_soup.find_all(id='OrderDetailSection'))
#
# print(result_soup.find_all("td", {'width': '200'}))
# print('')
# print('')
# print(result_soup.find_all("td", {'width': '200', 'valign': 'top'}))
# print('')
# print('')
# print('')


# returns all order items names and the number of order items
def find_OrderNameList(result_soup):
    OrderNameList = (result_soup.find_all("td", {'width': '200', 'valign': 'top'}))
    item_list = []
    n = 0
    for item in OrderNameList:
        # Note: what if list is empty?
        # if item == 'None':
        #     break
        item_list.append(item.find('b').string)
        n += 1
    return item_list, n


# find the number of all order items (ie.pieces) -- return list
def find_OrderPiecesList(result_soup):
    OrderPiecesList = (result_soup.find_all("strong"))
    item_list = []
    for item in OrderPiecesList:
        item_list.append(item.string)
    print('order item numbers: ' + str(item_list))
    print(len(item_list))
    return(item_list)


# find the item category of each order item -- return list
def find_OrderDescriptionList(result_soup):
    OrderDescriptionList = (result_soup.find_all("td", {'width': '185'}))
    item_list = []
    for item in OrderDescriptionList:
        item_list.append(item.find('b').string)
    print('order categories are: ' + str(item_list))
    print(len(item_list))
    return(item_list)


# find the unit price of each order item -- return list
def find_OrderUnitPriceList(result_soup):
    OrderUnitPriceList = (result_soup.find_all("td", {'width': '85'}))
    item_list = []
    for item in OrderUnitPriceList:
        item_list.append(item.find('font').string)
    print('order unit prices are: ' + str(item_list))
    print(len(item_list))
    return(item_list)


# # find the total price of the number of order items -- return list
# OrderTotalPriceList = (result_soup.find_all("td", {'nowrap': 'nowrap', 'align': 'right'}))
# item_list = []
# for item in OrderTotalPriceList:
#     item_list.append(item.find('font'))
# print(item_list)

namelist, numitems = find_OrderNameList(result_soup)
print('name list type: ' + str(type(namelist)))
print(namelist)
print('')
print('numitems type: ' + str(type(numitems)))
print(numitems)
print('')

find_OrderPiecesList(result_soup)
find_OrderDescriptionList(result_soup)
find_OrderUnitPriceList(result_soup)
