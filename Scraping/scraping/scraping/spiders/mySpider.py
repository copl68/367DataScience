import scrapy


class QuotesSpider(scrapy.Spider):
    name = "food"
    start_urls = [
        'https://www.cookingclassy.com/recipes/',
    ]

    def parse(self, response):
        for recipe in response.css('liv.li-a'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('div.li-a selectorgadget_rejected a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)