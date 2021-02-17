from bs4 import BeautifulSoup
import urllib.request
import ssl

import pandas as pd

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('table')

df = pd.read_html(html)[0]
print(df)

	