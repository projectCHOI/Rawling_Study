import requests
from bs4 import BeautifulSoup

def get_blog(URL) :
  h = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Referer' : 'https://search.naver.com/search.naver?where=news&query=%ED%85%8C%EC%8A%AC%EB%9D%BC&sm=tab_opt&sort=2&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0&office_category=0&service_area=0', 'cookie':'NNB=KXDWSALR5HLWE; ASID=afc28e77000001821bee653700000062; _ga=GA1.2.852833469.1658355403; _ga_7VKFYR6RV1=GS1.1.1663030713.12.1.1663030726.47.0.0; NFS=2; m_loc=8e6c6458de8107ce6b301a2fdcaac47c270f10d32641f9fdfed1b5b1faac3e2c; NV_WETR_LAST_ACCESS_RGN_M="MDIxMzU1NTA="; NV_WETR_LOCATION_RGN_M="MDIxMzU1NTA="; recent_card_list=2936,3397,2717,3977; nx_ssl=2; nid_inf=-1453188587; NID_AUT=3O547E30xwR+LSPJWBh1H0BeJZ8z7w5GcYoFiB1oouz7XPFXgUYyapi0YaIPu/ed; NID_JKL=G/s4QbAdJVVTz69y/dBkR/9g00VQhbM8nxg71ZvVgyE=; NID_SES=AAABoKkgglCWz6aloghoOZ3uiyN2Gx8Ya6M3siOaeQCtWMn7TXgrPkganW/YVI931ONSrWmpB6IIM3p/mCMfueM9ekkTAuzM2mj8PfOoUbrV7BrzerfHGStcNmmb0QkiSuOy8AH1MwneQ7sJCTZBpPEfIbn9HUQ6S62sMy5oLJ0xqXedXxwQ4TsBa4+6Z6FWpVTIfmTzWMFt/M4pfpxYEbYAVBsfhLIsNPCjHLCrkoDdQPeUS949dDM9Xf8zpucBTRJrB6GwKaQDSeVWs+OgXngp1iusiktNnHZ7hEWDO5gyZCXkA7jV9njHKBDw6b58JD2La4eTPDBjq6xzUHaCAt+L7rGlpQ5FWHh1UF8XcyHGLdi2zQRHHSs9giWGIdbJ61akjlPZM/N8vL9zJZcw8qFmko0EY8RNmF1aUNE7qEcfaEyQNu/tlmIsUeYl5kPbZgL8fUiKMssPunn4ciffRsstEIcRbvtkVUdDKvr5QdQdf5J0o167t5vXBvctqzggQXUYOOBv8Cb9G9W5NcGibg9J3OCd7JMZTNGPV6gFAtga/WJL; page_uid=idY26sprvTVssudbzPwssssssI4-486433; _naver_usersession_=SXc2E3wZ6W9q/0SVHj+cMQ=='}

  tmp = URL.split('/')
  Blog_URL = "https://blog.naver.com/PostView.naver?blogId={0}&logNo={1}".format(tmp[-2], tmp[-1])

  res = requests.get(Blog_URL, headers = h)
  soup = BeautifulSoup(res.text, "html.parser")

  if soup.select_one(".se-title-text") :
    title = soup.select_one(".se-title-text > p > span").text
    category = soup.select_one(".blog2_series > a").text
    nick = soup.select_one(".nick > a").text
    date = soup.select_one(".se_publishDate").text
    content = soup.select_one(".se-main-container").text.replace("\n","")
  elif soup.select_one("h3.se_textarea") :
    title = soup.select_one("h3.se_textarea").text
    category = soup.select_one(".blog2_series > a").text
    nick = soup.select_one(".nick > a").text
    date = soup.select_one(".se_publishDate").text
    content = soup.select_one(".se_doc_viewer").text.replace("\n","")
  else :
    return None

  return (title, category, nick, date, content, URL)

get_blog('https://blog.naver.com/nexongames_inside/223228973996')
