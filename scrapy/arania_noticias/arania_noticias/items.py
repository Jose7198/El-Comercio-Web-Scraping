# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst


def deleteBlanks(text):
    return text.strip()

class ComercioNew(scrapy.Item):
    Date = scrapy.Field(
        input_processor = MapCompose(
            deleteBlanks
        )
    )
    Title = scrapy.Field(
        input_processor = MapCompose(
            deleteBlanks
        )
    )
    Views = scrapy.Field()
    Indignado = scrapy.Field()
    Triste = scrapy.Field()
    Indiferente = scrapy.Field()
    Sorprendido = scrapy.Field()
    Contento = scrapy.Field()
    Editor = scrapy.Field(
        input_processor = MapCompose(
            deleteBlanks
        )
    )
    Category = scrapy.Field(
        input_processor = MapCompose(
            deleteBlanks
        )
    )
    Tag = scrapy.Field(
        input_processor = MapCompose(
            deleteBlanks
        )
    )
    Hour = scrapy.Field()
    Total_Reactions = scrapy.Field()
    Views_Reacts_Ratio = scrapy.Field()



class AraniaNoticiasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
