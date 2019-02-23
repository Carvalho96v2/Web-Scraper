import scrapy
import sys
from imfdb.utils.file_reader import get_tv_shows, get_pistols, update_tv_shows
from imfdb.items import ImgData

class TvImageSpider(scrapy.Spider):
    name = "TvImage"
    sys.stdout = open('logs', 'w+')
    _pistols = get_pistols()

    def start_requests(self):
        urls = get_tv_shows()
        cap = len(urls) if len(urls) > 50 else 50
        for i in range(0, cap):
            try:
                print('Requesting {url}'.format(url=urls[i]))
                yield scrapy.Request(url=urls[i], callback=self.parse)
            except:
                print('Couldnt request {url}'.format(url=urls[i]))
            finally:
                print('Removing {url}'.format(url=urls[i]))
                urls.remove(urls[i])
        update_tv_shows(urls)
        self.start_requests()
                


    def parse(self, response):

        pistols = self._pistols
        guns = response.xpath("//h2/span/text()").getall()
        for index, element in enumerate(guns):
            if element in pistols:
                print('Found {gun}'.format(gun=element))
                xpath_expression = "//div/div[preceding-sibling::h2/span[contains(text(), '{starting_gun}')] and following-sibling::h2/span[contains(text(), '{ending_gun}')]]".format(starting_gun=element, ending_gun=guns[index+1])
                for image in response.xpath(xpath_expression):
                    yield ImgData(image_urls=['http://www.imfdb.org' + image.css('img::attr(src)').extract_first()])
                    #yield {
                    #    "img" : image.css('img::attr(src)').get()
                   #}

