import scrapy


class QuotesAdvancedSpider(scrapy.Spider):
    name = 'quotes_advanced'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    

    
    def parse(self, response):
    
        quote_container = response.xpath('//*[@class="quote"]')
        for quote in quote_container :
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@class="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@class="keywords"]/@content').extract_first()

            #Shows in scrapy shell (saves no output)
            print ('\n')
            print (text)
            print (author)
            print ('Tags: ' + tags)
            print ('\n')


        next_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_url = response.urljoin(next_url)
        yield scrapy.Request(absolute_next_url)