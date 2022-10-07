import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        h1_tag = response.xpath("//h1/a/text()").extract()
        quote_text = response.xpath('//*[@class="quote"]/*[@class="text"]/text()').extract()
        author_class =  response.xpath('//*[@class="author"]/text()').extract()

        yield {'H1 tag' : h1_tag, 'Quote' : quote_text, 'Author' : author_class}
