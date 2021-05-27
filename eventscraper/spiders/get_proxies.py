import scrapy


class GetProxiesSpider(scrapy.Spider):

    name = 'get_proxies'
    proxies = []
    useragents = []

    def start_requests(self):
        #allowed_domains = ['https://www.us-proxy.org/']
        start_urls = ['https://www.us-proxy.org//']
    
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parseProxies)

    def parseProxies(self, response):
        proxies = response.xpath('//*[@id="proxylisttable"]/tbody//tr/td[1]').css('::text').extract()
        print('Proxies\n', proxies)

        yield scrapy.Request(url='https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/', callback=self.parseUserAgents)

    def parseUserAgents(self, response):
        useragents = response.xpath('//*[@id="content-base"]/section[2]/div/div/table/tbody//tr/td[1]/a/text()').extract()
        
        print('useragents\n', useragents)
        print('Proxies\n', proxies)

        


        
