"""
Outline:
(1)Login into partner.just-eat.ca website
 -- note: the cookie must be passed to every link
(2)Input date and selection into the partner home page
ex: https://partner.just-eat.ca/Orders/OrdersBetweenDates/17-02-2017/
    1m?pageIndex=3
(3)Index all "href" order links for each index page
ex: https://partner.just-eat.ca/Orders/OrderDetail/12936365
(4)For each order link, scrape the order contents
(5)Export data as a csv
"""

import requests
from bs4 import BeautifulSoup


# ------------------------------FUNCTIONS----------------------------------#


# This function initiates the link for given variables and returns request object
# TODO: Terminate if result is not 200
def initiate_link(date, duration, index_page, MYCOOKIES, s):
    request_date_url = "https://partner.just-eat.ca/Orders/OrdersBetweenDates/" + \
        date + "/" + duration + "?pageIndex=" + index_page
    result = s.get(request_date_url, cookies=MYCOOKIES)
    print("the status of initiate_link is:" + str(result.status_code))
    return result


# This function returns all order links under the classes 'odd orderDetailsRow' and 'even orderDetailsRow'
# returning a list of order details links for a given html page
def find_order_links(soup):
    found_links = []
    for link in soup.find_all(class_='odd orderDetailsRow'):
        found_links.append(link.a['href'])
    for link in soup.find_all(class_='even orderDetailsRow'):
        found_links.append(link.a['href'])
    return found_links


# This function returns all links found in a list
# Loop the extraction for all the index pages
def find_all_links(date, duration, MYCOOKIES, s):
    output_links = []
    for index_page in range(100):

        print(' ')
        print(index_page)

        request_date_url = "https://partner.just-eat.ca/Orders/OrdersBetweenDates/" + \
            date + "/" + duration + "?pageIndex=" + str(index_page)
        result = s.get(request_date_url, cookies=MYCOOKIES)

        print('index page ' + str(index_page) + ' status:' + str(result.status_code))

        result_soup = BeautifulSoup(result.content, 'html.parser')

        if len(find_order_links(result_soup)) == 0:
            print(' ')
            print('WE ARE GOING TO BREAK! --> at index ' + str(index_page))
            print(' ')
            break

        for links in find_order_links(result_soup):
            output_links.append(links)

    return output_links


# returns all (1) order item names (2) number of order items
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
    return(item_list)


# find the item category of each order item -- return list
def find_OrderDescriptionList(result_soup):
    OrderDescriptionList = (result_soup.find_all("td", {'width': '185'}))
    item_list = []
    for item in OrderDescriptionList:
        item_list.append(item.find('b').string)
    return(item_list)


# find the unit price of each order item -- return list
def find_OrderUnitPriceList(result_soup):
    OrderUnitPriceList = (result_soup.find_all("td", {'width': '85'}))
    item_list = []
    for item in OrderUnitPriceList:
        item_list.append(item.find('font').string)
    return(item_list)


# ----------------------------------

# find order number and return order number
def find_OrderNumber(result_soup):
    OrderNumber = result_soup.find_all('td', {'colspan': '2', 'style': 'line-height: 16px;'})
    OrderNumber = OrderNumber[0].find('b').string
    return OrderNumber


# find the street address of the customer
# (note that this is initiated the same way as postal code - room for improvement)
def find_StreetAddress(result_soup):
    StreetAddress = result_soup.find_all("td", {'colspan': '3', 'width': '400', 'valign': 'bottom', 'align': 'left'})
    StreetAddress = StreetAddress[1].find('font').string
    return StreetAddress


# find the postal code of the customer
def find_PostalCode(result_soup):
    PostalCode = result_soup.find_all("td", {'colspan': '3', 'width': '400', 'valign': 'bottom', 'align': 'left'})
    PostalCode = PostalCode[2].string
    return PostalCode


# find the tip of the order by counting back 3 from the list of all prices on the page  (ie. td, align right)
def find_Tip(result_soup):
    Tip = result_soup.find_all("td", {'align': 'right'})
    n = int(len(Tip)) - 3
    Tip = Tip[n].find('font').string
    return Tip


# find the date of the order
def find_Date(result_soup):
    Date = result_soup.find_all("td", {'colspan': '5', 'valign': 'bottom'})
    Date = Date[0].find('font', {'size': '4'}).string
    return Date


# find the Time --> use regex to search?
def find_DateTime(result_soup):
    DateTime = result_soup.find_all("td", {'valign': 'top', 'align': 'center'})
    n = int(len(DateTime)) - 2
    DateTime = DateTime[n].find("font", {'size': '2'}).string
    return DateTime


# find previous orders from customer by using the last of the list
def find_PrevOrder(result_soup):
    PrevOrder = result_soup.find_all("td", {'align': 'center'})
    n = int(len(PrevOrder)) - 2
    PrevOrder = PrevOrder[n].find('font').string
    return PrevOrder


# --------------------------------------------------------------------------#

# Login to Partner Justeat site and return the login cookie
# TODO: Prompt user to enter username and password
# TODO: Terminate if login is unsuccessful
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


# TODO: Prompt user to enter date and duration
# Initiate the link into the 'result' variable
date = "17-02-2017"
duration = "1d"
index_page = "0"
result = initiate_link(date, duration, index_page, MYCOOKIES, s)

# Use bs4 to find all order links
result_soup = BeautifulSoup(result.content, 'html.parser')

# Find all links using the find all links function.
output_links = find_all_links(date, duration, MYCOOKIES, s)

# print all order details links found
print(' ')
print('output links are:')
print(' ')
print(output_links)
print(' ')
print(str(len(output_links)) + 'have been found.')

output_links = find_order_links(result_soup)


print('')
print('')
print('')
print('')
print('')

# iterate over each order details link within the list of links found
for link in output_links:

    # initiate order details link
    order_url = "https://partner.just-eat.ca" + link
    result = s.get(order_url, cookies=MYCOOKIES)
    print('status of page: ' + str(link) + "-->" + str(result.status_code))
    result_soup = BeautifulSoup(result.content, 'html.parser')

    # find and print item names and number of items
    print('item names are:')
    namelist, numitems = find_OrderNameList(result_soup)
    print(namelist)
    print('')

    print('item amounts are:')
    amountlist = find_OrderPiecesList(result_soup)
    print(amountlist)
    print('')

    print('item catagories are:')
    catagorieslist = find_OrderDescriptionList(result_soup)
    print(catagorieslist)
    print('')

    print('item unit prices are:')
    unitpriceslist = find_OrderUnitPriceList(result_soup)
    print(unitpriceslist)
    print('')

    print('-------------------------------------')

# TODO: need to add columns for order number, street address, postal code, tip and date.
# iterate these items 'numitem' times for each list
# might need to create a function that creates lists that repeats a string for
# numitem times
