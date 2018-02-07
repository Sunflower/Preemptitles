from bs4 import BeautifulSoup as BS
import urllib.request
from html.parser import HTMLParser
import re


playlist_url = input("gib nem: ")

with urllib.request.urlopen(playlist_url) as response:
  playlist = response.read()
  soup = BS(playlist, "lxml")
  
title_attrs = soup.find_all(attrs={"data-title":re.compile(r".*")})
titles = [tag["data-title"] for tag in title_attrs]

titles_str = '\n'.join(titles).encode('cp1252','replace').decode('cp1252')

print(titles_str)
with open("playListNames.txt", "a") as f:
    f.write(titles_str)
