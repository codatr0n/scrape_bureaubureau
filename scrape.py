import requests
from urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import json

# Suppress SSL certificate warning from urllib3
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

base_url = 'https://www.bureaubureau.dk'
start_url = 'https://www.bureaubureau.dk/soeg/bureautype/webbureau'

response = requests.get(start_url, verify=False)
soup = BeautifulSoup(response.text, features='lxml')
last_page = int(
    soup.select('.soegpager ul .last a')[0]['href'].split('page=')[1])

# url_list = [start_url + '?page=' + str(i) for i in range(1, 2)]
url_list = [start_url + '?page=' + str(i) for i in range(1, last_page + 1)]

agency_dict = {}
agency_count = 0

for url in url_list:
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, features='lxml')

    for agency in soup.select('.bureauTitle a'):
        agency_name = agency.text
        print('Agency name: {}'.format(agency_name))
        agency_dict[agency_name] = {}

        bb_agency_url = base_url + agency['href']
        print('BB URL: {}'.format(bb_agency_url))
        agency_dict[agency_name]['bb url'] = bb_agency_url

        agency_response = requests.get(bb_agency_url, verify=False)
        agency_soup = BeautifulSoup(agency_response.text, features='lxml')

        # extract agency url from BB agency page
        agency_url = agency_soup.select('a.btn-block')[0]['href']
        print('Agency URL: {}'.format(agency_url))
        agency_dict[agency_name]['web url'] = agency_url

        # extract tags from BB agency page
        agency_tags = []
        for tag in agency_soup.select('.tags-list li a'):
            if len(tag.text) > 0:
                agency_tags.append(tag.text)
        for tag in agency_soup.select('#more-links-1 li a'):
            if len(tag.text) > 0:
                agency_tags.append(tag.text)

        print('Tags: {}'.format(agency_tags), end='\n\n')
        agency_dict[agency_name]['tags'] = agency_tags

        agency_count += 1

print('Scraped {count} agencies from {url}'.format(count=agency_count,
                                                   url=start_url))

with open('agencies.json', 'w') as fp:
    json.dump(agency_dict, fp, indent=4)
