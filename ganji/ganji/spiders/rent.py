import re
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from ..items import GanjiItem

TextExtract = lambda x: x and x[0] or ''


class GanjiSpider(CrawlSpider):

    name = "ganji"
    allowed_domains = ["ganji.com"]
    start_urls = [
        "http://fz.ganji.com/fang1/gulou",
    ]
    rules = [Rule(SgmlLinkExtractor(
        allow=('com/fang1/tuiguang-\d+', )),
        follow=True,
        callback='parse_html')]

    def recursive_extract(self, sel, summary):
        summary.append(''.join(sel.xpath('text()').extract()))
        for sub_sel in sel:
            self.recursive_extract(sub_sel.xpath('*'), summary)

    def loop_extract(self, sel):
        summary = []
        while len(sel) > 0:
            summary.append(''.join(sel.xpath('text()').extract()))
            sel = sel.xpath('*')
        return ''.join(summary).replace(' ', '').replace('\n', '').replace('\r\n', '')

    def clean_label(self, sel):
        return re.sub('<.*?>|\n| |', '', TextExtract(sel.extract()))

    def parse_html(self, response):
        sel = Selector(response)
        ganji = GanjiItem()
        ganji['url'] = sel.response.url
        ganji['publisher'] = TextExtract(sel.xpath(
            '//div[@class="basic-info-contact"]/div[@class="contact-person tel-number clearfix"]/span[@class="contact-col"]/i[@class="fc-4b"]/text()').extract()).replace(' ', '')
        ganji['identity'] = TextExtract(sel.xpath(
            '//div[@class="basic-info-contact"]/div[@class="contact-person tel-number clearfix"]/span[@class="contact-col"]/i[@class="fc-red"]/text()').extract()).replace(' ', '')
        ganji['telephone'] = TextExtract(sel.xpath(
            '//div[@class="basic-info-contact"]/div[@class="contact-telphone clearfix"]/span[@class="contact-col"]/em[@class="contact-mobile"]/text()').extract()).replace(' ', '')
        ganji['price'] = TextExtract(sel.xpath(
            '//ul[@class="basic-info-ul"]/li/b[@class="basic-info-price"]/text()').extract())
        ganji['summary'] = self.clean_label(sel.xpath(
            '//div[@class="col-cont"]/div[@class="summary"]/div[@class="summary-cont"]'))
        return ganji
