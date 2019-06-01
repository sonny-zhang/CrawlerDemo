# @Time     : 2019/6/1 10:25
# @Author   : sonny-zhang
# @FileName : main.py
# @github   : @sonny-zhang
import scrapy
import re


class JobboleSpiderSpider(scrapy.Spider):
    name = 'jobbole_spider'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/114690/']

    def parse(self, response):
        # ---------------------------------通过xpath选择器提取字段--------------------------------------
        title = response.xpath('//*[@id="post-114690"]/div[1]/h1/text()').extract_first()
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract_first().strip().replace('·', '').strip()
        praise_number = response.xpath('//span[contains(@class, "vote-post-up")]/h10/text()').extract_first()

        favorite_numbers = response.xpath('//span[contains(@class, "bookmark-btn")]/text()').extract_first()   # 返回'2 收藏'
        match_re = re.match(r'.*(\d+).*', favorite_numbers)
        if match_re:
            favorite_numbers = match_re.group(1)
        else:
            favorite_numbers = '0'

        comment_numbers = response.xpath('//a[@href="#article-comment"]/span/text()').extract_first()
        match_re = re.match(r'.*(\d+).*', comment_numbers)
        if match_re:
            comment_numbers = match_re.group(1)
        else:
            comment_numbers = '0'
        content = response.xpath('//div[@class="entry"]').extract_first()

        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()     # 获取文章标签
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]          # 过滤掉评论
        tags = ','.join(tag_list)       # 将list元素转换成str

        # ---------------------------------通过css选择器提取字段--------------------------------------
        title = response.css('.entry-header h1::text').extract_first()
        create_date = response.css('.entry-meta-hide-on-mobile::text').extract_first().strip().replace('·', '').strip()
        praise_number = response.css('.vote-post-up h10::text').extract_first()
        favorite_numbers = response.css('.bookmark-btn::text').extract_first()
        match_re = re.match(r'.*(\d+).*', favorite_numbers)
        if match_re:
            favorite_numbers = match_re.group(1)
        else:
            favorite_numbers = '0'

        comment_numbers = response.css('a[href="#article-comment"] span::text').extract_first()
        match_re = re.match(r'.*(\d+).*', comment_numbers)
        if match_re:
            comment_numbers = match_re.group(1)
        else:
            comment_numbers = '0'

        content = response.css('div.entry').extract()
        tag_list = response.css('.entry-meta-hide-on-mobile a::text').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]  # 过滤掉评论
        tags = ','.join(tag_list)  # 将list元素转换成str

        pass