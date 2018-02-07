from bs4 import BeautifulSoup as BS
import urllib.request
from html.parser import HTMLParser

#playlistUrl = input("gib nem: ")

with urllib.request.urlopen(
        'https://www.youtube.com/playlist?list=PLp2ovQedKSi5VjHDms1hIYqoUByLaBkgK') as response:
  playlist = response.read()
  soup = BS(playlist)
  


html = playlist.decode("utf-8").encode('cp1252','replace').decode('cp1252')
soup = BS(html)
print(soup)

#
#titles = ""
#class MyHTMLParser(HTMLParser):
#    def handle_starttag(self, tag, attrs):
#        for attr in attrs:
#            if attr[0] == "data-title":
#                global titles
#                titles += attr[1] + "\n"
#        
#parser = MyHTMLParser()
#parser.feed(html)
#print(titles)
#
#with open("playListNames2.txt", "a") as f:
#    f.write(titles)
#
#print("yay")
