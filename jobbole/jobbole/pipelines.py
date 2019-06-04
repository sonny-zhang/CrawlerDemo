# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import json

from scrapy.exporters import JsonItemExporter


class JobbolePipeline(object):
	def process_item(self, item, spider):
		return item


class JsonWithEncodingPipeline(object):
	def __init__(self):
		self.file = open('article.json', 'w', encoding='utf-8')

	def process_item(self, item, spider):
		lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
		self.file.write(lines)
		return item

	def spider_closed(self, spider):
		self.file.close()


class JsonExporterPipeline(object):
	def __init__(self):
		self.file = open('article.json', 'wb')
		self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
		self.exporter.start_exporting()

	def close_spider(self):
		self.exporter.finish_exporting()
		self.file.close()

	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item


class JobboleImagePipline(ImagesPipeline):

	def item_completed(self, results, item, info):
		"""重载父类方法"""
		for ok, value in results:
			image_file_path = value["path"]
		item['front_image_path'] = image_file_path
		return item
