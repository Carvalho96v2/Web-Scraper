# import libraries
from bs4 import BeautifulSoup as bs
from requests import get
import json

# specify the urls
MOVIES_URL = "http://www.imfdb.org/wiki/Category:Movie"

weapon_urls ={
    "pistols": "http://www.imfdb.org/wiki/Category:Pistol",
    "revolvers": "http://www.imfdb.org/wiki/Category:Revolver"
}

weapon_types = {
    "pistols": ["Self-Loading"],
    "revolvers": ["Revolvers", "Blank-Firing Revolvers"]
}


#specify the categories
movies_page = get(MOVIES_URL)

weapon_pages = {}
for key, value in weapon_urls.items():
    weapon_pages[key] = (get(value))

weapon_soups = {}
for key, value in weapon_pages.items():
    weapon_soups[key] = []
    for v in value:
        weapon_soups[key].append((bs(weapon_pages[key].text, 'html.parser')))

weapon_tables = {}
for key, value in weapon_soups.items():
    weapon_tables[key] = []
    for v in value:        
        weapon_tables[key].append(weapon_soups[key].find_all('table', style = 'text-align: center; text-align:center'))

category_tables = {}
this_weapons_types = []
for key, value in weapon_tables.items():
    category_tables[key] = []
    this_weapons_types = weapon_types[key]
    for this_type in this_weapons_types:
        for table in value:
            for t in table:                                 #ToDo: find a better way to do this one day
                if(t.tr.th.div.text == this_type):
                    category_tables[key].append(table)


weapon_paragraphs = {}
result = []
for key, value in category_tables.items():
    weapon_paragraphs[key] = []
    for v in value:
        for p in v:
            weapon_paragraphs[key].append(p.find_all('p'))

weapon_names = {}
for key, value in weapon_paragraphs.items():
    weapon_names[key] = []
    for v in value:
        for n in v:
            if n.a is not None:
                if n.a.text is not None:
                    weapon_names[key].append(n.a.text)

print(weapon_names)
