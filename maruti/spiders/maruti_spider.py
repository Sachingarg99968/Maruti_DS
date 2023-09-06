import scrapy
from pprint import pprint
import json

class MarutiSpiderSpider(scrapy.Spider):
    name = "maruti-spider"
    allowed_domains = ["marutisuzuki.com"]
    start_urls = ["https://app.mapmyindia.com/MarutiWebAPI/searchdata?state=DELHI&city=new%20delhi&radius=30&category=dealer"]

    def parse(self, response):
        results=response.text
        pprint(results)
