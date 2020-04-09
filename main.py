import requests
from bs4 import BeautifulSoup




#sentence = input('입력: ')
sentence = '부담갖지말고먹어'
url = 'https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy?_callback=jQuery112407704652679626749_1586403615462&q=' + sentence + '&where=nexearch&color_blindness=0&_=1586403615463'
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')
print(soup.find('em').get_text())