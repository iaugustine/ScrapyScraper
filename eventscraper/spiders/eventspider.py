import scrapy
import time
from ..items import EventscraperItem
#from bs4 import BeautifulSoup

class EventspiderSpider(scrapy.Spider):
    name = 'eventspider'
    
    
    def start_requests(self):
        event_types = ['parties','music--events','fashion--events',
                       'performances','festivals','food-and-drink--festivals',
                       'standup_comedy']
    
        allowed_domains = ['https://www.eventbrite.com']

        # for event in event_types:
        #     time.sleep(2)
        #     print(event, '\n')
        #     for i in range(1,51):
        #         yield scrapy.Request(url=f'https://www.eventbrite.com/d/ny--new-york/{event}/?page={i}',
        #                 callback = self.parse)
        for i in range(1,2):
            yield scrapy.Request(url=f'https://www.eventbrite.com/d/ny--new-york/standup_comedy/?page={i}',
                    callback = self.parse)

        # Write code to push item to 


    def parse(self, response):
        
        time.sleep(1)
        eventurls = response.xpath('//div[@class="search-event-card-rectangle-image"]//div[@class="eds-event-card-content__primary-content"]/a/@href').extract()
        print(len(eventurls))
        if len(eventurls)>0:
            time.sleep(1)
            for url in eventurls:
                yield scrapy.Request(url=url,
                                    callback=self.eventparse)
            
    
    def eventparse(self, response):
        time.sleep(2)
        item = EventscraperItem()

        item['eventTitle'] = response.xpath('//h1[@class="listing-hero-title"]').css('::text').extract() 
        item['eventLocation'] = response.xpath('//*[@id="event-page"]/main/div[1]/div[2]/div/div[3]/section[2]/section/div/div/p').css('::text').get().strip()
        try:

            timestamps = response.xpath('//*[@id="event-page"]/main/div[1]/div[2]/div/section[1]/div[1]/div/div/div[2]/div/div[1]//meta/@content').extract() 
            item['eventTimeStart'] = timestamps[0]
            item['eventTimeEnd'] = timestamps[1]
        except:
            print('No timestamps')


        item['eventPrice'] = response.xpath('//*[@id="event-page"]/main/div[1]/div[2]/div/div[1]/div/div[2]/div/div[3]/div').css('::text').get().strip()
        item['eventOrganizer'] = response.xpath('//*[@id="event-page"]/main/div[1]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/a').css('::text').get().strip()
        item['eventImageUrl'] = response.xpath('//div[contains(@class, "--no-gutters listing-hero--image-container")]/div[2]/picture/@content').extract()
        item['eventTags'] =  response.xpath('//*[@id="event-page"]/main/div[1]/div[2]/div/section[1]/div[1]/div/div/div[1]/div[3]/div[2]').css('section span a span::text').extract()
        item['eventUrl'] = response.url
        item['eventRecurring'] = False
        item['eventDisplay'] = True
        item['eventFeatured'] = False

        
        #location = response.xpath('//*[@id="event-page"]/main/div[1]/div[2]/div/section[1]/header/div/div/div/div[2]/div[2]/div//p').extract()[:-1] 
        item['eventDescription'] = response.xpath('//*[@id="event-page"]/main/div[1]/div[2]/div/section[1]/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]').extract()

        yield item
        
        
        
        

