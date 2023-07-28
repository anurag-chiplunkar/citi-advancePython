import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.google.com/")
if response.status_code != 200:
	print("Error fetching page")
	exit()
else:
    # Parsing the HTML with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
print(soup.title.string)
nb_links = len(soup.find_all('a'))
print(f"There are {nb_links} links in this page")

# Targeting DOM elements
first_link = soup.a
print(first_link)
print(first_link.text)
print(first_link.get('href')

pagespace = soup.find(id="pagespace")
print(pagespace)
athing = soup.find(class_="athing")
print(athing)