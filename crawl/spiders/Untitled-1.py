from scrapy.spiders import Spider
from scrapy_splash import SplashRequest
 
from ..items import CrawlItem

class MySpider(Spider):
    name = 'found_error'
    start_urls = ['http://192.168.3.105/simpac/warning/c3k_warn.plc'] #FIRST LEVEL

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url = url, endpoint = "render.html", callback= self.parse)

    # 1. SCRAPING
    def parse(self, response):
        item = CrawlItem()
        
        for text in response.xpath("/html/body/center[1]/table"):
            item['error_text'] = text.xpath(' /html/body/center[1]/table/tbody/tr[2]/td[2]/div/text()').extract_first()
            item['error_type'] = text.xpath('/html/body/center[1]/table/tbody/tr[2]/td[4]/text()').extract_first()

            yield item
# scrapy crawl found_error -o data.json