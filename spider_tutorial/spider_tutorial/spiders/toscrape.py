import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ToscrapeSpider(CrawlSpider):
    name = 'toscrape'
    allowed_domains = ['books.toscrape.com']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://books.toscrape.com', headers={
            'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"), process_request='set_user_agent')
    )

    def set_user_agent(self, request, response):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'title': response.xpath("//h1/text()").get(),
            'product': response.xpath("(//table//tr)[2]/td/text()").get(),
            'price': response.xpath("//p[@class = 'price_color']/text()").get(),
            'description': response.xpath("normalize-space(//article/p/text())").get(),
            'availability': response.xpath("(//table//tr)[6]/td/text()").get(),
        }
