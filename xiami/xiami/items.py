# Define here the models for your scraped items
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class XiamiItem(Item):
    account = Field()
    song_name = Field()
    artist = Field()
    song_rank = Field()
