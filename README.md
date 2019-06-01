# CrawlerDemo
> 爬虫技术的各种demo
## 构建
1. 在Python虚拟环境里使用pipenv
2. 根据Scrapy自带的template(模板)构建一个Scrapy项目(可以自己定义模板)
3. 进入构建的项目，创建默认的Scrapy工程(运行爬虫是以工程为单位)

## 调试
1. 在Python虚拟环境里运行：  
 `scrapy shel  http://www.baidu.com/`
2. 开始解析response：  
`resposne.xpath(xxxx).extract_first()`  
`resposne.css(xxxx).extract_first()`  
`resposne.css(xxxx).extract()[0]`  这种方式需要判断返回的数组为空的情况，建议使用前面的方式 

## douban
资料：https://www.imooc.com/video/17523  
这个demo是采用scrapy技术，对豆瓣top250的movie信息进行爬取，是作者根据
课程的实践，如果做过这个demo，就不要再看这个代码了  

>实现内容：  

- [x] 获取信息：电影名字、排行、介绍、评论人数、星数、评价
- [ ] 设置代理：IP代理
- [x] 设置UA：用固定[User-Agent]池，使用random随机取

## jobbole
> 实现内容:

- [x] 包含css选择器和xpath选择器的使用  