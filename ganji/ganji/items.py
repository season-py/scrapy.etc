# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class GanjiItem(Item):
    url = Field()
    publisher = Field()
    identity = Field()
    telephone = Field()
    price = Field()
    summary = Field()
