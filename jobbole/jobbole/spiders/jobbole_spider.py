# @Time     : 2019/6/1 10:25
# @Author   : sonny-zhang
# @FileName : main.py
# @github   : @sonny-zhang
import scrapy
import re
from scrapy.http import Request
from urllib import parse


class JobboleSpiderSpider(scrapy.Spider):
    name = 'jobbole_spider'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts']

    def parse(self, response):
        """
        1. 获取文章列表页中的文章url并交给scrapy下载，下载后调用自己制定的解析回调函数
        2. 获取下一页的url并交给scrapy进行下载，下载后交给parse （这里开始递归）
        """
        # 1. 获取文章列表页中的文章url并交给scrapy下载后再次进行解析
        post_urls = response.css('#archive .post-thumb a::attr(href)').extract()
        for post_url in post_urls:
            # 将提取的url交给scrapy去下载，下载后去调用自己制定的解析回调函数; urljoin拼接没有域名的url
            # yield 是把下载任务交给scrapy去下载
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

        # 2. 提取下一页并交给scrapy去下载
        next_url = response.css('.next.page-numbers::attr(href)').extract_first()
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        """提取文章内的字段"""
        # ---------------------------------通过xpath选择器提取字段--------------------------------------
        # title = response.xpath('//*[@id="post-114690"]/div[1]/h1/text()').extract_first()
        # create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract_first().strip().replace(
        #     '·', '').strip()
        # praise_number = response.xpath('//span[contains(@class, "vote-post-up")]/h10/text()').extract_first()
        #
        # favorite_numbers = response.xpath('//span[contains(@class, "bookmark-btn")]/text()').extract_first()  # 返回'2 收藏'
        # match_re = re.match(r'.*(\d+).*', favorite_numbers)
        # if match_re:
        #     favorite_numbers = int(match_re.group(1))
        # else:
        #     favorite_numbers = 0
        #
        # comment_numbers = response.xpath('//a[@href="#article-comment"]/span/text()').extract_first()
        # match_re = re.match(r'.*(\d+).*', comment_numbers)
        # if match_re:
        #     comment_numbers = int(match_re.group(1))
        # else:
        #     comment_numbers = 0
        # content = response.xpath('//div[@class="entry"]').extract_first()
        #
        # tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()  # 获取文章标签
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]  # 过滤掉评论
        # tags = ','.join(tag_list)  # 将list元素转换成str

        # ---------------------------------通过css选择器提取字段--------------------------------------
        title = response.css('.entry-header h1::text').extract_first()
        create_date = response.css('.entry-meta-hide-on-mobile::text').extract_first().strip().replace('·', '').strip()
        praise_number = response.css('.vote-post-up h10::text').extract_first()
        favorite_numbers = response.css('.bookmark-btn::text').extract_first()
        match_re = re.match(r'.*(\d+).*', favorite_numbers)
        if match_re:
            favorite_numbers = int(match_re.group(1))
        else:
            favorite_numbers = 0

        comment_numbers = response.css('a[href="#article-comment"] span::text').extract_first()
        match_re = re.match(r'.*(\d+).*', comment_numbers)
        if match_re:
            comment_numbers = int(match_re.group(1))
        else:
            comment_numbers = 0

        content = response.css('div.entry').extract()
        tag_list = response.css('.entry-meta-hide-on-mobile a::text').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]  # 过滤掉评论
        tags = ','.join(tag_list)  # 将list元素转换成str

        pass
