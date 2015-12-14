# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import time
from scrapy import signals
from scrapy.exporters import JsonLinesItemExporter
from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['origine_id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['origine_id'])
            return item

class EventPlacePipeline(object):
    def process_item(self, item, spider):
        if item['place']:
            if 'location' in item['place']:
                item['place'].update(item['place']['location'])
                item['place'].pop('location', None)
        return item

class BGEventPipeline(object):
    def process_item(self, item, spider):
        if item['place']:
            if 'country' in item['place']:
                if(item['place']['country'] == 'Bulgaria'):
                    return item
        else:
            raise DropItem("Not in BG item found: %s" % item)

class JsonLinesExportPipeline(object):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()

        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        dirname = "export_" + spider.name
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        file = open('./%s/%s_events.jsonliese' % (dirname, int(time.time()) ), 'w+b')
        self.files[spider] = file
        self.exporter = JsonLinesItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
