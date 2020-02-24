from urllib.parse import urljoin

from scrapy.utils import spider
import re
from learning.items import PyCoderItem


class PyCoderSpider(spider.Spider):
    name = 'rsue'
    start_urls = ['https://rsue.ru/universitet/novosti/index.php', ]

    def parse(self, response):
        article_list = response.xpath('//div[@class="column is-3"]')
        print(article_list)

        for article in article_list:
            article_link = article.xpath('.//div[@id="news-title"]/a/@href').get()
            article_link = urljoin(response.url, article_link)
            yield response.follow(article_link, callback=self.article_parse)

        next_page = response.xpath('//a[@class="modern-page-next"]/@href').get()
        next_page = urljoin(response.url, next_page)
        yield response.follow(next_page, callback=self.parse)

    def article_parse(self, response):
        item = PyCoderItem()
        item['link'] = response.url 
        item['title'] = response.xpath('/html/body/div[4]/div/h1/text()').get()
        date = response.xpath('//*[@id="date-news"]/text()').get()
        item['date'] = re.sub('\s+', ' ', date)
       # item['picture'] = response.xpath('/html/body/div[5]/div/div/div[2]/img/@src').get()
        item['picture'] = response.xpath('//div[@id="main_image-news"]/img/@src').get()
        test = response.xpath('//div[@id="text-news"]/p/text()').getall()
        test1 = ' '.join(test)
        item['text'] = re.sub('\s+', ' ', test1)
        yield item