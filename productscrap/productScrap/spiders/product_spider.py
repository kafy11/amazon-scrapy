import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import ProductScrapItem

class ProductsSpider(scrapy.Spider):
    name = 'products'
    f = open("urls.txt", "r")
    start_urls = []
    for l in f:
        start_urls.append(l)

    def parse(self, response):
        items = ProductScrapItem()

        title = response.css('#productTitle::text').extract()
        price = response.xpath('//*[@id="formats"]//a[contains(string(), "Kindle")]//span[contains(text(), "R$")]/text()').extract()

        #Indice precisa ser igual o nome do campo na classe GtscrapItem
        items['title'] = title
        items['price'] = price
        items['url'] = response.request.url

        yield items