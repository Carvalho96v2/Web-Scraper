import scrapy
import sys

class TvSpider(scrapy.Spider):
    name = "tv"
    sys.stdout = open('tv_show logs', 'w+') 
    def start_requests(self):
        urls = [
            'http://www.imfdb.org/index.php?title=Category:Television&pagefrom=20th+of+December+%2820-e+dekabrya%29#mw-pages'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        next_200 = response.css('div#mw-pages a::attr(href)').getall() 
        print(next_200)
        for element in response.css('div#mw-pages div.mw-content-ltr'):
            yield {
                "links" : element.css('a::attr(href)').getall() 
            }
        if next_200 is not None:
            try:
                yield scrapy.Request(response.urljoin(next_200[1]))
            except:
                yield scrapy.Request(response.urljoin(next_200)[0])