from bs4 import BeautifulSoup
import urllib
from requests import get

def speakers(url, year):
	url = url
	year = year
	soup = BeautifulSoup(get(url).content)
	cards = soup.find_all(attrs={"class": "portfolio-it"})
	d = {}
	for card in cards:
		# byline_url = card.a['href']
		d.update({card.find('h4').string:card.a.img['src']})
		# bylines = BeautifulSoup(get(byline_url).content)
		# bylines_card = bylines.find_all(attrs={"class": "portfolio-detail-description-text"})[0]
		# byline = bylines_card.find_all('p')[-1].string
		# with open("speakers.py", "a") as f:
		# 	f.write('{name},\"{description}\", {link}, {year}\n'.format(name=card.find('h4').string, description=card.find_all('span')[-1].string, link=byline_url, year=year))
	count = 0
	# for year in d:
		# if year == "2010":
		# 	continue
	for speaker in d:
		count += 1
		if speaker == "Jodi Lomask/Capacitor":
			continue
		# print(d[speaker])
		# if speaker["speaker_title"] == "Jodi Lomask/Capacitor" or speaker["speaker_title"] == "Mallika Chopra" or speaker["speaker_title"] == "Celli@Berkeley":
		# 	continue
		urllib.request.urlretrieve(d[speaker], speaker + ".jpg")
	# print(d)
	print(count)


speakers("http://tedxberkeley.org/speakers-5", 2015)
speakers("http://tedxberkeley.org/speakers-4", 2014)
speakers("http://tedxberkeley.org/2013-2", 2013)
speakers("http://tedxberkeley.org/2012-2", 2012)
speakers("http://tedxberkeley.org/2011-2", 2011)
speakers("http://tedxberkeley.org/2010-2", 2010)



