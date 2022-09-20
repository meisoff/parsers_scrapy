import scrapy
from scrapy_splash import SplashRequest


class ToscrapeSpider(scrapy.Spider):
    name = 'toscrape'
    allowed_domains = ['quotes.toscrape.com']

    script = '''
        function main(splash, args)
          splash.private_mode_enabled = false
          headers = {
            ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
          }
          splash:set_custom_headers(headers)
          url = args.url
          assert(splash:go(url))
          assert(splash:wait(1))
          return splash:html()
        end 
    '''

    def start_requests(self):
        yield SplashRequest(url="http://quotes.toscrape.com/js", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
        })


    def parse(self, response):
        for item in response.xpath('//div[@class = "quote"]'):
            yield {
                'quote': item.xpath('./span[@class = "text"]/text()').get(),
                'author': item.xpath('.//small/text()').get(),
                'tags': item.xpath('./div[@class = "tags"]/a/text()').getall(),
            }

        next_page = response.xpath('//nav/ul/li/a/@href').get()

        if next_page:
            yield SplashRequest(url=f"http://quotes.toscrape.com{next_page}", callback=self.parse, endpoint="execute", args={
                'lua_source': self.script
            })
