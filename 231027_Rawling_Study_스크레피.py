#스크레피
import scrapy

class NewsSpider(scrapy.Spider):
    mame = 'news'
    #allowed_domains = ['naver.com']
    start_urls = ['이곳엔 url']

    def parse(self, response):
        for idx, movie in enumerate(response.css('이곳엔 리뷰').getall()):
            print(idx + 1, movie)
            