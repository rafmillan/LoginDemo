import requests
from bs4 import BeautifulSoup

data = {
	'usr': 'admin',
	'password': '12345'
}

headers = {
	'Cookie': 'tdsess=TEST_DRIVE_SESSION',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

with requests.Session() as s:
	url = 'http://testing-ground.scraping.pro/login'
	r = s.get(url, headers=headers)
	r = s.post(url, data=data, headers=headers)
	r = s.get('http://testing-ground.scraping.pro/login?mode=welcome', headers=headers)
	#print(r.content)
	soup = BeautifulSoup(r.content, 'html5lib')
	divs = soup.find('div', id='case_login')
	h3 = divs.find('h3')
	if h3.has_attr('class'):
		print(h3['class'][0])

