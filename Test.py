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


# def find_OrderNumber(result_soup):
#     #OrderNumber = result_soup.find_all

# find the street address of the customer 
# (note that this is initiated the same way as postal code - room for improvement)
def find_StreetAddress(result_soup):
    StreetAddress = result_soup.find_all("td", {'colspan': '3', 'width': '400', 'valign': 'bottom', 'align': 'left'})
    StreetAddress = StreetAddress[1].find('font').string
    print (StreetAddress)
    return

# find the postal code of the customer
def find_PostalCode(result_soup):
    PostalCode = result_soup.find_all("td", {'colspan': '3', 'width': '400', 'valign': 'bottom', 'align': 'left'})
    PostalCode = PostalCode[2].string
    print (PostalCode)
    return

#find the tip of the order by counting back 3 from the list of all prices on the page  (ie. td, align right)
def find_Tip(result_soup):
    Tip = result_soup.find_all("td", {'align': 'right'})
    n = int(len(Tip)) - 3
    Tip = Tip[n].find('font').string
    print(Tip)
    return


# find the date of the order
def find_Date(result_soup):
    Date = result_soup.find_all("td", {'colspan': '5', 'valign': 'bottom'})
    Date = Date[0].find('font', {'size': '4'}).string
    print(Date)
    return

# find the Time --> use regex to search?
def find_DateTime(result_soup):


find_StreetAddress(result_soup)
find_PostalCode(result_soup)
find_Date(result_soup)
find_Tip(result_soup)

# Implement: orde rnumber, street address, postal code, tip, date