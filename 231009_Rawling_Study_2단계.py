# 뉴스 데이터 가져오기 2단계
import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_news_list(keyword, startdate, enddate) :
    li = []
    h = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

    for d in pd.date_range(startdate, enddate) :
        str_d = d.strftime("%Y.%m.%d")
        page = 1
        print(str_d)
        #마지막 페이지를 넘기면 종료 시킴
        while True:
            start = (page-1)*10 + 1
            print(page)
            URL = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query={0}&sort=2&photo=0&field=0&pd=3&ds={1}&de={2}&mynews=0&office_type=0&office_section_code=0&news_office_checked=&office_category=0&service_area=0&nso=so:r,p:from{3}to{4},a:all&start={5}".format(keyword, startdate, enddate, startdate.replace(".",""), enddate.replace(".",""), start)

            res = requests.get(URL,headers = h)
            soup = BeautifulSoup(res.text, "html.parser")

            if soup.select_one(".api_noresult_wrap") :
                break
                
            news_list = soup.select("ul.list_news li")
            
            for item in news_list :
                if len(item.select("div.info_group a")) >= 2 :
                    li.append(get_news(item.select("div.info_group a")[1]['href']))
            page = page + 1
            
    return pd.DataFrame(li, columns=['title', 'date', 'media', 'content', 'URL'])
