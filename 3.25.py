
from bs4 import BeautifulSoup
from urllib.request import urlopen

htmlString = '''<html>
<head><title>My Document</title></head>
<body>Main text.</body></html>
'''

soup = BeautifulSoup(urlopen("http://www.networksciencelab.com/"))


href = soup.find(href = "v2.jpg")
print(href)
##