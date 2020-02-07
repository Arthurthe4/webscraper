"""
### Python 3,6 / UTF-8 ###
--------------------------
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "URL"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="lxml")

# kill all script and style elements you don't need
for script in soup(["script", "style", "footer", "nav"]):
    script.extract()    # rips out script, style, footer, class="header2", nav

allText = soup.body.get_text()  # get_text() removes all <tags>

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in allText.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split('.'))
# drop blank lines
allText = '\n'.join(chunk for chunk in chunks if chunk)

# Creates a txt. file with pure text
text_file = open("Test.txt", "w")
n = text_file.write(allText)
text_file.close()
