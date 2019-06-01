# @Time     : 2019/6/1 10:25
# @Author   : sonny-zhang
# @FileName : main.py
# @github   : @sonny-zhang
from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "jobbole_spider"])
