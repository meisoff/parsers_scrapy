import scrapy


class GlassesshopSpider(scrapy.Spider):
    name = 'glassesshop'
    allowed_domains = ['www.glassesshop.com']

    # start_urls = ['https://www.glassesshop.com/bestsellers']

    def start_requests(self):
        yield scrapy.Request(url='https://www.glassesshop.com/bestsellers', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36'
        })

    def parse(self, response):
        for product in response.xpath('//div[@id = "product-lists"]/div[contains(@class, "product-list-item")]'):
            item = product.xpath('.//div[@class = "p-title-block"]//div[@class = "row no-gutters"]')
            product_name = item.xpath('.//div/a/text()').get().replace('\n', '').strip()
            product_url = item.xpath('.//div/a/@href').get()
            product_price = item.xpath('//div[@class = "p-price"]/div/span/text()').get()
            product_img = product.xpath('//div[@class = "product-img-outer"]//img/@data-src').get()

            yield {
                'product_name': product_name,
                'product_url': product_url,
                'product_price': product_price,
                'product_img': product_img,
            }

            next_page = response.xpath('//ul[@class = "pagination"]//a[@aria-label = "Next »"]/@href').get()

            if next_page:
                yield response.follow(url=next_page, callback=self.parse, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36'
                })
