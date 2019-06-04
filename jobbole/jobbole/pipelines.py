# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline

from scrapy import exporters


class JobbolePipeline(object):
    def process_item(self, item, spider):
        return item


class JobboleImagePipline(ImagesPipeline):
    def item_completed(self, results, item, info):
        """重载父类方法"""
        for ok, value in results:
            image_file_path = value["path"]
        item['front_image_path'] = image_file_path
        return item
