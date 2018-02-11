from bs4 import BeautifulSoup as BS
import urllib.request
import re
import requests

''' TODO
- append new titles to playlist textfile outputs without overwritting original
- allow user authentification for private playlists
- classify songs into genres
    https://archive.ics.uci.edu/ml/datasets/FMA%3A+A+Dataset+For+Music+Analysis

'''
playlist_url = input("gib nem: ")

with urllib.request.urlopen(playlist_url) as response:
  playlist = response.read().decode('utf-8')
  soup = BS(playlist, "lxml")

#playlist_html = requests.get(playlist_url).text
#soup = BS(playlist_html, 'lxml')  
  
title_attrs = soup.find_all(attrs={"data-title":re.compile(r".*")})
titles = [tag["data-title"] for tag in title_attrs]

titles_str = '\n'.join(titles)

playlist_name = soup.find('title').contents[0]
forbidden_chars_table = str.maketrans('\/*?:"<>|','_________')
playlist_name = playlist_name.translate(forbidden_chars_table)

print(titles_str)
with open(playlist_name + ".txt", "a", encoding="utf-8") as f:
    f.write(titles_str)