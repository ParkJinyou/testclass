# 크롤링과 스크래핑

# crawling 불특정 대략 긁어오기
# scraping 특정 주제로만 긁어오기

# requests 인터넷 주소로 접근
# BeautifulSoup 가죠온 데이터를 보기 좋게 정돈 > 구문 추출 용이
# 인터넷 페이지의 3요소 HTML/CSS/JS

import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.naver'
param= {'code': '191597'}
response = requests.get(url,params=param)
html = response.text
soup = BeautifulSoup(html,'html.parser')

review_list = soup.find_all('div',class_='score_reple')

for review in review_list :
    print(review.find('p').text.strip())





'''response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,'html.parser')
print(soup)'''



