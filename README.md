# Web Scraper Project

##  scrape.py
### This script scrapes restaurant order data from an online platform

#### Usage:
User inputs account username and password followed by the from-date and duration of the query. The script will produce a csv file including
    - item name
    - item amount
    - item category
    - item unit price
    - order number
    - address
    - postal code
    - tip
    - order date
    - order time
    - amount of previous orders

#### About the scraper:
The scraper uses python's BeautifulSoup and Requests libraries to access and scrape pages relevant to user query