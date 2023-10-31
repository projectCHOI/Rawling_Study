# 뉴스 데이터 가져오기 1단계
import requests
from bs4 import BeautifulSoup

def get_news(URL) :
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")
    
#select : 조건에 맞는 모든 테그를 복수계로 가져오고, 결과가 리스트 형태로 리턴
#select_one : 조건을 만족하는 가장 처음의 하나의 요소만 리턴
    
    # 기사 제목 가져오기
    title = soup.select_one("h2#title_area span").text.strip()
    # 기사 날짜 가져오기
    date = soup.select_one("span.media_end_head_info_datestamp_time")['data-date-time']
    #미디어 정보 가져오기 (선택자를 추가해야 함)
    media = soup.select_one("a.media_end_head_top_logo img")['title']
    #기사 내용 가져오기
    content = soup.select_one("div#newsct_article").text.replace("\n","")
    
    #print를 return로 변경
    return (title, date, media, content, URL)

get_news("https://n.news.naver.com/mnews/article/243/0000049609?sid=105")
