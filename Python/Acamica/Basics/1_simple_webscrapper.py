#!/usr/bin/env python3
"""
Simple web scrapper that obtains the titles from the results of
a search in the www.ted.com web page.
"""


import urllib.request
from lxml import html


search = "artificial intelligence"
page_number = 1
per_page = 20


u = urllib.request.urlopen(
    'https://www.ted.com/search?page={}&per_page={}&q={}'
    .format(
        page_number,
        per_page,
        search.replace(" ", "+")
    )
)

data = u.read()

# Extract the titles from the results

doc = html.document_fromstring(data)

for title in doc.cssselect("article.search__result h3 a"):
    print(title.text_content())