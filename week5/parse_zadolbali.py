import requests
import bs4
from multiprocessing import Pool
import codecs

def parse_page(url):
    text = requests.get(url).text
    parser = bs4.BeautifulSoup(text, 'lxml')
    x = parser.findAll('div', attrs={'class':'text'})
    v = parser.findAll('div', attrs={'class':'rates'})
    return [res.text for res in x]

p = Pool(5)
url_list = ['https://www.anekdot.ru/release/anekdot/month/2018-' + '0' * int(n < 10) + str(n) for n in range(1, 13)]


    
with Pool(10) as p:
    map_results = p.map(parse_page, url_list)

    
p.terminate()
p.join()