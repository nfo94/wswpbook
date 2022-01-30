from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule


class ArticleSpider(CrawlSpider):
    name = "articles"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/'Benevolent_dictator_for_life'"]
    rules = [Rule(LinkExtractor(allow=r".*"), callback="parse_items", follow=True)]

    def parse_items(self, response):
        url = response.url
        title = response.css("h1::text").extract_first()
        text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        lastUpdated = response.css("li#footer-info-lastmod::text").extract_first()
