from sqlite3 import Row
from unicodedata import name
from urllib import request
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table = soup.find("table")

templist = []

for tr in table.find_all("tr"):
    tdList = tr.find_all("td")
    row = [i.text.rstrip() for i in tdList]
    templist.append(row)

names = []
distance = []
mass = []
radius = []
lum = []

for i in range(1, len(templist)):
    names.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])
    lum.append(templist[i][7])

df = pd.DataFrame(list(zip(names, distance, mass, radius, lum)), columns=["Star_Name", "Distance", "Mass", "Radius", "Luminosity"])
df.to_csv("Bright Stars.csv")