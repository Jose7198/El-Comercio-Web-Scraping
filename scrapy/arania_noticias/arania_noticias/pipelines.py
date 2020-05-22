# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class FillingFieldssPipeline(object):
    
    def parseDate(self, item):
        complete_date = item['Date']
        hour = complete_date[-5:]
        only_date = complete_date[:-6]
        item['Hour'] = hour
        item['Date'] = only_date
        return item

    def countReactions(self, item):
        item['Total_Reactions'] = item['Indignado'] + item['Triste'] + item['Indiferente'] + item['Sorprendido'] + item['Contento']
        return item

    def calculateRatio(self, item):
        ratio = item['Views'] / item['Total_Reactions']
        item['Views_Reacts_Ratio'] = ratio
        return item

    def process_item(self, item, spider):
        complete_date = item['Date']
        hour = complete_date[-5:]
        if(':' in hour):
            only_date = complete_date[:-6]
            item['Hour'] = hour
            item['Date'] = only_date
        item['Total_Reactions'] = int(item['Indignado']) + int(item['Triste']) + int(item['Indiferente']) + int(item['Sorprendido']) + int(item['Contento'])
        ratio = item['Total_Reactions'] / int(item['Views'])
        item['Views_Reacts_Ratio'] = ratio
        return item


class AraniaNoticiasPipeline(object):
    def process_item(self, item, spider):
        return item
