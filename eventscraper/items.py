# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# from scrapy.loader import ItemLoader
# from itemloaders.processors import TakeFirst, MapCompose
# from w3lib.html import remove_tags



class EventscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    eventTitle = scrapy.Field()
    #eventLocation = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    eventLocation = scrapy.Field()
    eventTimeStart = scrapy.Field()
    eventTimeEnd = scrapy.Field()
    eventPrice = scrapy.Field()
    eventOrganizer = scrapy.Field()
    eventImageUrl = scrapy.Field()
    eventTags = scrapy.Field()
    eventUrl = scrapy.Field()
    eventRecurring = scrapy.Field()
    eventDisplay = scrapy.Field()
    eventFeatured = scrapy.Field()
    eventDescription = scrapy.Field()
    pass
