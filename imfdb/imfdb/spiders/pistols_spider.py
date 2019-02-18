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
        #for pistol in response.css('table'):
         #   if pistol.css('div[text="Self-Loading"]'):
                yield {
                    'name' : response.css('div.gallerytext p a::text').getall()
                }