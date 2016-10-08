# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class EventItem(scrapy.Item):
    origine_id = scrapy.Field();
    name = scrapy.Field()
    description = scrapy.Field()
    start_time = scrapy.Field()
    end_time = scrapy.Field()
    place = scrapy.Field()
    # attending_count = scrapy.Field()
    # origine = scrapy.Field()
    # cover = scrapy.Field()
