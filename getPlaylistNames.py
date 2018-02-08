from bs4 import BeautifulSoup as BS
import urllib.request
import re

''' TODO
- append new titles to playlist textfile outputs without overwritting original
- allow user authentification for private playlists
'''
playlist_url = input("gib nem: ")

with urllib.request.urlopen(playlist_url) as response:
  playlist = response.read()#.decode('utf-8')
  soup = BS(playlist, "lxml")
  
playlist_name = soup.find('title').contents[0]
  
title_attrs = soup.find_all(attrs={"data-title":re.compile(r".*")})
titles = [tag["data-title"] for tag in title_attrs]

titles_str = '\n'.join(titles)

print(titles_str)
with open(playlist_name + ".txt", "a", encoding="utf-8") as f:
    f.write(titles_str)