import scrapy
import numpy
import pandas as pd

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class SpiderFile(scrapy.Spider):
    
    name = 'file'

    comercio_url = 'https://www.elcomercio.com/tag/ecuador/'

    urls = []

    for i in range(1,1397):
        urls.append(comercio_url + str(i))

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url = url)
    
    def parse(self, response):
        url = response.css('a.title::attr(href)').extract()
        links = []
        for link in url:
            links.append(response.urljoin(link))
        
        url_series = pd.Series(links)
        
        df = url_series.to_frame(name='URLs')
        df.to_csv('./urls.csv',mode='a', header=False)



