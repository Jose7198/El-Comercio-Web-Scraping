import scrapy
import numpy
import pandas as pd
import csv

from arania_noticias.items import ComercioNew
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class SpiderNews(scrapy.Spider):

    name = 'news'

    urls = []

    with open('urls.csv', 'r', encoding='utf-8') as urls_csv:
        csv_reader = csv.reader(urls_csv, delimiter=',')
        for row in csv_reader:
            urls.append(row[1])

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url = url)
    
    def parse(self, response):
        date_selector = response.css('div.date')

        info_loader = ItemLoader(
            item = ComercioNew(),
            selector = date_selector
        )

        info_loader.default_output_processor = TakeFirst()

        info_loader.add_css(
            'Date',
            'div::text'
        )

        title_selector = response.css('div.title')

        info_loader.selector = title_selector

        info_loader.add_css(
            'Title',
            'h1::text'
        )

        views_selector = response.css('div.social-nav')

        info_loader.selector = views_selector

        info_loader.add_css(
            'Views',
            'div.pageviews::text'
        )

        reactions_selector = response.css('div.rating>div.score') 

        reactions_names = ['Indignado', 'Triste', 'Indiferente', 'Sorprendido', 'Contento']

        for i in range(0,5):

            info_loader.selector = reactions_selector[i]

            info_loader.add_css(
                reactions_names[i],
                '.number::text'
            )
        
        editor_selector = response.css('div.right-col>div.info')

        info_loader.selector = editor_selector

        info_loader.add_css(
            'Editor',
            'div.signature>div::text'
        )

        info_selector = response.css('div.breadcrumbs')

        info_loader.selector =  info_selector

        info_loader.add_css(
            'Category',
            'a::text'
        )

        info_loader.add_css(
            'Tag',
            'a.highlighted::text'
        )

        yield info_loader.load_item()




        

        
