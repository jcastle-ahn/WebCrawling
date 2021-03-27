import requests
from bs4 import BeautifulSoup
 
source = requests.get("https://www.naver.com/").text
soup = BeautifulSoup(source, "html.parser")
hotKeys = soup.select("span.blind")
 
index = 0
for key in hotKeys:
    index += 1
    print(str(index) + ", " + key.text)
#    if index >= 20:
#       break
