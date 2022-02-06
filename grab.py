from bs4 import BeautifulSoup
import requests
import csv

# This file collects and cleans the data from the Florida lottery website.

# Initialize lotto list and iterator.
numbers = [None] * 2165
j = 0

# Request the HTML of the specified link.
page = requests.get("https://flalottery.com/site/winningNumberSearch.do?searchTypeIn=range&gameNameIn=LOTTO&singleDateIn=&fromDateIn=01%2F02%2F1999&toDateIn=02%2F29%2F2020&n1In=&n2In=&n3In=&n4In=&n5In=&n6In=&pbIn=&mbIn=&lbIn=&pnIn=&cbIn=&n7In=&n8In=&n9In=&n10In=&n11In=&n12In=&n13In=&n14In=&n15In=&n16In=&n17In=&n18In=&n19In=&n20In=&n21In=&n22In=&n23In=&n24In=&submitForm=Submit")

# Make a beautiful soup object using the HTML content requested.
soup = BeautifulSoup(page.content, 'html.parser')

# Strip all rows of HTML content for only text of ID 'td'.
for i in range(1, 4330, 2):
        numbers[j] = soup.find_all('td')[i].get_text().replace(" - ", " ")
        j = j + 1

print(numbers)
