import requests
import bs4
def parse_page_votes(url):
    headers = {'User-agent': 'Mozilla/5.0'}
    text = requests.get(url, headers=headers).text
    parser = bs4.BeautifulSoup(text, 'lxml')
    votes = parser.findAll('div', attrs={'class':'rates'})
    return [v['data-r'].split(";") for v in votes]	


