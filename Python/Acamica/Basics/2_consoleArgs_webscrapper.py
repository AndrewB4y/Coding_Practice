#!/usr/bin/env python3
"""
Simple web scrapper that obtains the titles from the results of
a search in the www.ted.com web page.
"""


import urllib.request
from lxml import html
import sys

if len(sys.argv) != 4:
    raise SystemExit(
        "".join(
            ("Usage: 2_consoleArgs_webscrapper.py",
             "<term to seach> <page_number> <results per page>")
        )
    )

search = sys.argv[1]
page_number = sys.argv[2]
per_page = sys.argv[3]


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
