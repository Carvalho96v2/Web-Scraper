import scrapy


class PistolsSpider(scrapy.Spider):
    name = "pistols"

    def start_requests(self):
        urls = [
            'http://www.imfdb.org/wiki/Category:Pistol'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for pistol in response.css('table'):
            if pistol.css('tbody tr th div[text="Self-Loading"]'):
                yield {
                    'name' : pistol.css('div.gallerytext p a::text').getall()
                }