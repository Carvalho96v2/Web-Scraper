import scrapy


class MoviesSpider(scrapy.Spider):
    name = "movies"

    def start_requests(self):
        urls = [
            'http://www.imfdb.org/index.php?title=Category:Movie&pagefrom=10+to+Midnight#mw-pages'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        next_200 = response.css('div#mw-pages a::attr(href)').getall() 
        for element in response.css('div#mw-pages div.mw-content-ltr'):
            yield {
                "links" : element.css('a::attr(href)').getall() 
            }
        if next_200 is not None:
            try:
                yield scrapy.Request(response.urljoin(next_200[1]))
            except:
                yield scrapy.Request(response.urljoin(next_200)[0])