from bs4 import BeautifulSoup
import requests as rs
import time
from konlpy.tag import Mecab
from konlpy.utils import pprint

prev = ''
kkma = Kkma()

for i in range(0,100):
    response = rs.get('http://coinpan.com/free')
    soup = BeautifulSoup(response.text, 'html.parser')
    board = soup.findAll('table')
    board_tr = board[10].findAll('tr')[6:]
    title = board_tr[0].find('a').text.strip()
    link = board_tr[0].find('a')['href']
    if prev==title:
        continue
    prev = title
    pprint(kkma.nouns(title))
    time.sleep(0.5)
