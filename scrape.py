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

# # This function logs into the just-eat canada partner site and returns cookie
# # TODO: Prompt User to enter username and password
# # TODO: Terminate if login result is not 200
# def get_site_login_cookie():
#     payload = {
#         "username": "Daik1226",
#         "password": "Daik1226",
#         "isPersistent": 0
#     }
#     login_url = 'https://connect.just-eat.ca/api/account/login'
#     global s
#     s = requests.session()
#     s.headers[
#         'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
#     r = s.post(login_url, data=payload)
#     print('the status of the login is:' + str(r.status_code))
#     return r.cookies


# This function initiates the link for given variables and returns request object
# TODO: Terminate if result is not 200
def initiate_link(date, duration, index_page, MYCOOKIES, s):
    request_date_url = "https://partner.just-eat.ca/Orders/OrdersBetweenDates/" + \
        date + "/" + duration + "?pageIndex=" + index_page
    result = s.get(request_date_url, cookies=MYCOOKIES)
    print("the status of initiate_link is:" + str(result.status_code))
    return result


# This function returns all order links under the class 'odd orderDetailsRow'
# returning a list of links
# for a given page
def find_odd_order_links(soup):
    found_links = []
    for link in soup.find_all(class_='odd orderDetailsRow'):
        found_links.append(link.a['href'])
    return found_links


# This function returns all order links under the class 'even orderDetailsRow'
# returning a list of links
# for a given page
def find_even_order_links(soup):
    found_links = []
    for link in soup.find_all(class_='even orderDetailsRow'):
        found_links.append(link.a['href'])
    return found_links


# # This function returns the last link of the given index page
# # Note: need to make sure index 8 is the last page
# def find_last_link(soup):
#     for link in soup.find_all(id="PageIndexList"):
#         end_link = link.find_all(href=True)[6]
#         print(end_link)
#     return end_link


# This function returns all links found in a list
# Loop the extraction for all the index pages
def find_all_links (date, duration, MYCOOKIES, s):
    output_links = []
    for index_page in range(100):

        print(' ')
        print(index_page)

        request_date_url = "https://partner.just-eat.ca/Orders/OrdersBetweenDates/" + \
            date + "/" + duration + "?pageIndex=" + str(index_page)
        result = s.get(request_date_url, cookies=MYCOOKIES)

        print('index page ' + str(index_page) + ' status:' + str(result.status_code))

        result_soup = BeautifulSoup(result.content, 'html.parser')

        if len(find_odd_order_links(result_soup)) == 0:
            print(' ')
            print('WE ARE GOING TO BREAK! --> at index ' + str(index_page))
            print(' ')
            break

        for links in find_odd_order_links(result_soup):
            output_links.append(links)
        for links in find_even_order_links(result_soup):
            output_links.append(links)

    return output_links

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
duration = "1m"
index_page = "0"
result = initiate_link(date, duration, index_page, MYCOOKIES, s)

# Use bs4 to find all order links
result_soup = BeautifulSoup(result.content, 'html.parser')

# Find all links using the find all links function.
output_links = find_all_links(date, duration, MYCOOKIES, s)

print(' ')
print('output links are:')
print(' ')
print(output_links)
print(' ')
print(str(len(output_links)) + 'have been found.')

output_links = find_odd_order_links(result_soup)
output_links = find_odd_order_links(result_soup)


for link in output_links:
    order_url = "https://partner.just-eat.ca" + link
    result = s.get(order_url, cookies=MYCOOKIES)
    print('status of page: ' + str(link) + "-->" + str(result.status_code))
    result_soup = BeautifulSoup(result.content, 'html.parser')
