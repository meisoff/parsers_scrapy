import scrapy


class MvideoSpider(scrapy.Spider):
    name = 'mvideo'
    allowed_domains = ['www.mvideo.ru']

    def start_requests(self):
        yield scrapy.Request(url='https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36'
        })

    def parse(self, response):
        for good in response.xpath('//div[contains(@class, "product-cards-layout__item")]/mvid-plp-product-card/div'):
            picture = response.urljoin(good.xpath('.//div[@class = "product-picture product-picture--list"]/a/@href')).get()
            title = good.xpath('//div[@class = "product-card--list__description"]//a[@class = "product-title__text"]/text()').get()
            availability = good.xpath('//div[@class = "product-card--list__description"]//div[@class = "product-notification"]/text()').get()
            price_main = good.xpath('//span[@class = "price__main-value"]/text()').get()
            price_sale = good.xpath('//span[@class = "price__sale-value"]/text()').get()
            bonus = good.xpath('//div[@class = "mbonus-block__caption"]/span[1]/text()').get()


            yield {
                'Название': title,
                'Ссылка': picture,
                'Наличие': availability,
                'Основная цена': price_main,
                'Старая цена': price_sale,
                'Бонусы': bonus,
            }

            next_page = response.xpath('//ul[contains(@class, "pagination")]/li/a[contains(@class, "icon ng-star-inserted")]/@href').get()

            if next_page:
                yield response.follow(url=next_page, callback=self.parse, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36'
                })

