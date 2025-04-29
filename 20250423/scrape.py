import requests
from bs4 import BeautifulSoup
import lxml

url = "https://codepro.com.pk"
response = requests.get(url)

# print("Status Code:", response.status_code)
# print("Content Preview:", response.text[:500])  # Print first 500 characters



soup = BeautifulSoup(response.text, "lxml")

# title = soup.title.text
headlines = soup.find_all('h3')
print("Page Title:", headlines)




