from bs4 import BeautifulSoup
import urllib.request
import ssl

import pandas as pd

#Part 1

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('table')

df = pd.read_html(html)[0]
df = df[df["Neighbourhood"] != 'Not assigned'] #Filter
print(df)


# Part 2
import geocoder # import geocoder

# initialize your variable to None
lat_lng_coords = None
latitude = list()
longitude = list()
noneCount = 0
# loop until you get the coordinates
for postal_code in df["Postal Code"]:
    while (lat_lng_coords is None):
        g = geocoder.google('{}, Toronto, Ontario'.format(postal_code))
        lat_lng_coords = g.latlng
        noneCount = noneCount + 1
        if noneCount == 10:
            noneCount = 0
            lat_lng_coords = [1,1]

    print(lat_lng_coords)
    latitude.append(lat_lng_coords[0])
    longitude.append(lat_lng_coords[1])

df["Latitude"] = latitude
df["Longitude"] = longitude

print(df)
	