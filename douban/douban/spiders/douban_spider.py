# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    # 默认解析方法
    def parse(self, response):
        # 循环电影的条目
        movie_list = response.xpath('//div[@class="article"]//ol[@class="grid_view"]/li')
        for i_item in movie_list:
            # 将item文件导进来
            douban_item = DoubanItem()
            # 写详细的xpath数据解析
            douban_item['serial_number'] = i_item.xpath('.//em/text()').extract_first()
            douban_item['movie_name'] = i_item.xpath(
                './/div[@class="hd"]//span[@class="title"][1]//text()').extract_first()
            content = i_item.xpath('.//div[@class="bd"]/p[1]/text()').extract()
            # 遇到多行的数据的，就要进行数据的处理
            for i_content in content:
                content_s = "".join(i_content.split())
                douban_item['introduce'] = content_s
            douban_item['star'] = i_item.xpath('.//div[@class="star"]/span[2]/text()').extract_first()
            douban_item['evaluate'] = i_item.xpath('.//div[@class="star"]/span[4]/text()').extract_first()
            douban_item['describe'] = i_item.xpath('.//div[@class="bd"]//span[@class="inq"]/text()').extract_first()
            # 需要将数据yield到piplines里去
            yield douban_item
        # 解析下一页的规则，取[下一页]的xpath; 当[下一页]的xpath为False时整个爬虫停止
        next_link = response.xpath('//span[@class="next"]/link/@href').extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request('https://movie.douban.com/top250' + next_link, callback=self.parse)
