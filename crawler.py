from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
from urllib.error import HTTPError
import pandas as pd
import urllib.request
import sys

items = pd.read_csv('./movie_poster.csv', names = ['IMAGE_ID', 'URL'], encoding='latin-1')
sys.stdout = open('output.txt', 'w')

nullcheck = 1

for num in range(0, 944) :
    url = items.iloc[num][1]
    id = items.iloc[num][0]
    sys.stdout = open('output.txt', 'a')
    if nullcheck != id : #데이터에서 비어있는 이미지 번호 출력
        print("null", nullcheck)
        nullcheck += 2
        continue
    try : #서버내에 없는 이미지 번호 출력
        urllib.request.urlretrieve(url, str(id) + '.jpg')
        print(id)
    except HTTPError as e :
        err = e.read()
        code = e.getcode()
        print("error",code, id)
    nullcheck += 1

print('Image Crawling is done.')