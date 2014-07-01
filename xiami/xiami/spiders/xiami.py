from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from ..items import XiamiItem

TextExtract = lambda x: x and x[0] or None


class XiamiSpider(CrawlSpider):

    name = "xiami"
    allowed_domains = ["xiami.com"]
    start_urls = [
        # "http://www.xiami.com/",
        # "http://www.xiami.com/space/lib-song/u/631812?spm=a1z1s.6626009.229054153.3.iPbq8R",
        # "http://www.xiami.com/relation/talentcollect",
        # "http://www.xiami.com/u/7236969?spm=a1z1s.6889497.1392354889.11.nYh7zH",
        "http://www.xiami.com/u/271?spm=a1z1s.6843761.226669214.6.qaY83y",
    ]
    rules = [Rule(SgmlLinkExtractor(allow=('/space/lib-song/', 'www.xiami.com/u/\d+$', )), follow=True, callback='parse_html')]

    def parse_html(self, response):
        sel = Selector(response)
        account = TextExtract(sel.xpath("//div[@class='buddy50']/a/@title").extract())
        table_trs = sel.xpath("//div[@class='c695_l_content']/table/tbody/tr")
        for tr in table_trs:
            xiami = XiamiItem()
            xiami["account"] = account
            xiami["song_name"] = TextExtract(tr.xpath("td[@class='song_name']/a[1]/text()").extract())
            xiami["artist"] = TextExtract(tr.xpath("td[@class='song_name']/a[2]/text()").extract())
            xiami["song_rank"] = TextExtract(tr.xpath("td[@class='song_rank']/p/input/@value").extract())
            yield xiami
