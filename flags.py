from bs4 import BeautifulSoup
import requests
import urllib.request
import os

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

url="https://www.countryflags.io/"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "html.parser")
countries = soup.find_all("div", class_="item_country")
supported_countries = []
home_folder = './WORLD_FLAGS'
sizes = [16,24,32,48,64]
styles = ['flat','shiny']

for country in countries:
	country_id = country.find_all('p')[0].text
	country_name = country.find_all('p')[1].text

	if country_id == 'AH':
		country_name = 'Artsakh'
	elif country_id == 'AK':
		country_name = 'Abkhazia'
	elif country_id == 'EU':
		country_name = 'European Union'
	elif country_id == 'IC':
		country_name = 'Canary Islands'
	elif country_id == 'NY':
		country_name = 'Northern Cyprus'
	elif country_id == 'XK':
		country_name = 'Kosovo'

	supported_countries.append({
		'id': country_id,
		'name': country_name,
		'full_name': f'({country_id}) {country_name}'
	})

if not os.path.exists(f'{home_folder}'):
		os.mkdir('WORLD_FLAGS')

for country in supported_countries:
	print(f' * Downloading flags of {country["name"]} ...')
	country_folder = home_folder + f'\\{country["full_name"]}'
	os.mkdir(country_folder)
	for style in styles:
		style_folder = home_folder + f'\\{country["full_name"]}\\{style}'
		os.mkdir(style_folder)
		for size in sizes:
			urllib.request.urlretrieve(f'http://www.countryflags.io/{country["id"].lower()}/{style}/{str(size)}.png', style_folder + f'\\{str(size)}.png')
