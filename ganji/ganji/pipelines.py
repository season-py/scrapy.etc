# coding=utf-8
import json
from scrapy import signals
from scrapy.exceptions import DropItem
from scrapy.contrib.exporter import XmlItemExporter, CsvItemExporter, JsonItemExporter
from scrapy import log
import datetime


class GanjiPipeline(object):

    def __init__(self):
        self.target_files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def gen_filename(self, spider):
        return '.'.join([spider.name, datetime.datetime.now().strftime('%Y%m%d%H%M%S'), 'csv'])

    def spider_opened(self, spider):
        target_file = open(self.gen_filename(spider), 'wb')
        self.target_files[spider] = target_file
        self.exporter = CsvItemExporter(target_file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        target_file = self.target_files.pop(spider)
        target_file.close()

    def process_item(self, item, spider):
        if not (item.get('price') and item.get('summary')):
            raise DropItem('not price or summary')
        self.exporter.export_item(item)
        return item
